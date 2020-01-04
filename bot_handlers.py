import logging

NOTSET = 0  # param of logging __init__.py


class TelegramLogsHandler(logging.Handler):
    """Handler which send logs in Telegram.

    :param bot: telegram bot object
    :param chat_id: int, id of chat
    """

    def __init__(self, bot, chat_id, level=NOTSET):
        logging.Handler.__init__(self, level=level)
        self.bot = bot
        self.chat_id = chat_id

    def emit(self, record):
        log_entry = self.format(record)
        self.bot.send_message(chat_id=self.chat_id, text=log_entry)
