# Dvmn.org work results checker (chatbot)

[dvmn](https://dvmn.org) don't send mails which work was checked? No problem, this bot will send you this info.

### How to install

##### Local

You need to create `.env` file and write in file parameters `DVMN_TOKEN` and `BOT_TOKEN`.

`DVMN_TOKEN` - secret token for [dvmn](https://dvmn.org) API. For getting this token you need do authorization in site and go on [this](https://dvmn.org/api/docs/) page, where you can find token.

`BOT_TOKEN` - secret token for your telegram bot. Just use [this](https://core.telegram.org/bots#creating-a-new-bot) instruction (use VPN to open this link in Russia).

After you got `BOT_TOKEN` you need to write to you bot in telegram any message (`/start` for example).

###### Without Docker

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r src/requirements.txt
```

###### With Docker
[Docker Desktop should be installed](https://docs.docker.com/desktop/)

Then build docker image:
```
docker build -t dvmn_checker_bot .
```

Ofcourse you can change name `dvmn_checker_bot` to your name and add tags, if you want. Like `dvmn_checker_bot:v1`

Or you can pull ready to use image:
```
docker pull kiablunovskii/dvmn_checker_bot
```

### How to use

##### Without Docker

Open command line (in windows `Win+R` and write `cmd` and `Ok`). Go to directory with program or just write in cmd:

```
python <PATH TO PROGRAM>\main.py
```

##### With docker

Open command line (in windows `Win+R` and write `cmd` and `Ok`). Go to directory with program and write in cmd:

```
docker run -dp 5000:5000 --env-file ./.env dvmn_checker_bot
```

You can drop `d` option if you want to watch logs.

Or (if you pulled my repository) you can pull ready to use image:
```
docker run -dp 5000:5000 --env-file ./.env kiablunovskii/dvmn_checker_bot
```

### References

[dvmn.or API](https://dvmn.org/api/docs/)

[telegram bots documentation](https://core.telegram.org/bots#creating-a-new-bot)

[Docker](https://www.docker.com/)

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).
