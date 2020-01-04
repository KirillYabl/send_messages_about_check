# Dvmn.org work results checker (chatbot)

[dvmn](https://dvmn.org) don't send mails which work was checked? No problem, this bot will send you this info.

### How to install

You need to create `.env` file and write in file parameters `DVMN_TOKEN` and `BOT_TOKEN`.

`DVMN_TOKEN` - secret token for [dvmn](https://dvmn.org) API. For getting this token you need do authorization in site and go on [this](https://dvmn.org/api/docs/) page, where you can find token.

`BOT_TOKEN` - secret token for your telegram bot. Just use [this](https://core.telegram.org/bots#creating-a-new-bot) instruction (use VPN to open this link in Russia).

After you got `BOT_TOKEN` you need to write to you bot in telegram any message (`/start` for example).

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### How to use

Just run.

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
