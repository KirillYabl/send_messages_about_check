# Dvmn.org work results checker (chatbot)

[dvmn](https://dvmn.org) don't send mails which work was checked? No problem, this bot will send you this info.

### How to install

##### Local

You need to create `.env` file and write in file parameters `DVMN_TOKEN` and `BOT_TOKEN`.

`DVMN_TOKEN` - secret token for [dvmn](https://dvmn.org) API. For getting this token you need do authorization in site and go on [this](https://dvmn.org/api/docs/) page, where you can find token.

`BOT_TOKEN` - secret token for your telegram bot. Just use [this](https://core.telegram.org/bots#creating-a-new-bot) instruction (use VPN to open this link in Russia).

After you got `BOT_TOKEN` you need to write to you bot in telegram any message (`/start` for example).

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

##### Deploy on heroku

For deploy this bot on [heroku](https://heroku.com) you need to do next:

1) Sign up in heroku
2) Create app
3) Clone this repository and download on heroku with GitHub method (tab `Deploy` in heroku app)
4) Add `Config Vars` in `Settings` tab in heroku app
    1) `DVMN_TOKEN` - secret token for [dvmn](https://dvmn.org) API. For getting this token you need do authorization in site and go on [this](https://dvmn.org/api/docs/) page, where you can find token.

    2) `BOT_TOKEN` - secret token for your telegram bot. Just use [this](https://core.telegram.org/bots#creating-a-new-bot) instruction (use VPN to open this link in Russia).
    
### How to use

##### Run in Local

Open command line (in windows `Win+R` and write `cmd` and `Ok`). Go to directory with program or just write in cmd:

`python <PATH TO PROGRAM>\main.py`

##### Deploy on heroku

Run bot in `Resources` tab in heroku app. `Procfile` for run in repo already.

### References

[dvmn.or API](https://dvmn.org/api/docs/)

[telegram bots documentation](https://core.telegram.org/bots#creating-a-new-bot)

[heroku](https://heroku.com)

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
