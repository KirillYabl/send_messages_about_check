import os
import logging

import requests
import telegram
import dotenv

from bot_handlers import TelegramLogsHandler

logger = logging.getLogger('dvmn bot')


def raise_response_errors(response):
    """Check response for errors.
    raise error if some error in response
    :param response: requests response object
    """
    # check HTTPError
    response.raise_for_status()
    # some sites can return 200 and write error in body
    if 'error' in response.json():
        raise requests.exceptions.HTTPError(response.json()['error'])


def get_chat_id(bot_token):
    """Get bot chat_id in telegram.

    This function very suitable. It must be used, when you write to bot today.
    If ypu didnt write today, you will get empty result.
    Also this function must used ONLY for your personal bots, because it get
    first chat_id from updates.

    :param bot_token: str, bot Token
    :return: int, id of chat
    """
    url = f'https://api.telegram.org/bot{bot_token}/getUpdates'
    response = requests.get(url=url)
    raise_response_errors(response)

    try:
        chat_id = response.json()['result'][0]['message']['chat']['id']
    except IndexError:
        raise ValueError('Please, write to bot for initialize chat.')

    return chat_id


def get_list_of_work_checks_in_json(token, timestamp):
    """Get dvmn check works info in JSON.
    Func using long pooling API method.
    :param url: str, api token
    :param url: str, timestamp of last check. If first response must be ''
    :return: dict, json of response
    """
    headers = {'Authorization': 'Token {}'.format(token)}
    params = {'timestamp': timestamp}

    response = requests.get(url='https://dvmn.org/api/long_polling/', params=params, headers=headers)
    raise_response_errors(response)

    return response.json()


def send_result_of_check(response, bot, chat_id):
    """Send result of check work in dvmn by bot and using devman api and telegram.
    :param response: dict, response in json
    :param bot: Bot, telegram bot object
    :param chat_id: str, id of chat
    """
    attempt = response['new_attempts'][0]
    is_negative = attempt['is_negative']  # True if negative result
    lesson_title = attempt['lesson_title']  # user friendly name of lesson
    lesson_url = attempt['lesson_url']  # relative url to lesson without dvmn.org

    if is_negative:
        text = f'К сожалению работа "{lesson_title}" не принята. Подробнее https://dvmn.org{lesson_url}'
        bot.send_message(chat_id=chat_id, text=text)
    else:
        text = f'Поздравляю! Работа "{lesson_title}" успешно принята преподователем! https://dvmn.org{lesson_url}'
        bot.send_message(chat_id=chat_id, text=text)


if __name__ == '__main__':
    restart = False
    while True:
        try:
            restart_msg = 're' if restart else ''  # Restarted after critical error or started
            logging.basicConfig(format='%(asctime)s  %(name)s  %(levelname)s  %(message)s', level=logging.DEBUG)
            dotenv.load_dotenv()
            dvmn_token = os.getenv('DVMN_TOKEN')
            bot_token = os.getenv('BOT_TOKEN')
            chat_id = os.getenv('CHAT_ID')

            bot = telegram.Bot(token=bot_token)

            # Initialize chat_id if bot using firsttime
            if chat_id is None:
                chat_id = get_chat_id(bot_token=bot_token)
                with open('.env', 'a') as env:
                    env.write(f'\nCHAT_ID={chat_id}')

            tg_handler = TelegramLogsHandler(bot=bot, chat_id=chat_id, level=logging.INFO)
            logger.addHandler(tg_handler)
            logger.debug('Got env params')
            logger.debug('Telegram bot created')
            logger.debug('Got and saved id of chat')
            logger.info(f'Bot {restart_msg}started')

            timestamp = ''
            while True:
                try:
                    response = get_list_of_work_checks_in_json(token=dvmn_token, timestamp=timestamp)
                    if response['status'] == 'found':
                        timestamp = response['last_attempt_timestamp']
                        logger.debug('Found. Timestamp={}'.format(timestamp))
                        send_result_of_check(response, bot, chat_id)
                    elif response['status'] == 'timeout':
                        timestamp = response['timestamp_to_request']
                        logger.debug('TimeOut. Timestamp={}'.format(timestamp))
                except requests.exceptions.ReadTimeout:
                    logger.debug('Read timeout. Making new request.')
                except requests.exceptions.ConnectionError:
                    logger.error('Connection error. Waiting connection.')
        except Exception:
            # If critical error happens. Bot send message to user and write traceback in log
            logger.exception('Critical error in ')
            restart = True
