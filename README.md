<h1 align="center"> Telegram-Song-Downloader-Bot</h1>
<h3 align="center">Very powerful song downloader bot for telegram📶</h3>
<p align="center">
<a href="https://python.org"><img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python"></a>
<br>
  <img src="https://img.shields.io/github/stars/sanila2007/Telegram-Song-Downloader-Bot?style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/forks/sanila2007/Telegram-Song-Downloader-Bot?style=for-the-badge" alt="Forks">
  <img src="https://img.shields.io/github/watchers/sanila2007/Telegram-Song-Downloader-Bot?style=for-the-badge" alt="Watchers">
<br>
  <img src="https://img.shields.io/github/license/sanila2007/Telegram-Song-Downloader-Bot?style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/repo-size/sanila2007/Telegram-Song-Downloader-Bot?style=for-the-badge" alt="Repository Size">
  <img src="https://img.shields.io/github/contributors/sanila2007/Telegram-Song-Downloader-Bot?style=for-the-badge" alt="Contributers">
  <img src="https://img.shields.io/github/issues/github/sanila2007/Telegram-Song-Downloader-Bot?style=for-the-badge" alt="Issues">
<br>
<br>
</p>

## Click to reach <a href="https://t.me/songdownload597_bot">Song Dwonload bot</a> 💫

<<br>

## Config

`BOT_TOKEN` = Enter your bot token in sample.env when deploying it

```
sample.env

TOKEN = "INSERT_YOUR_BOT_TOKEN_HERE"
```
<br>

## Commands

```
/start = Use this command to start the bot

/song = Use this command to download songs
               Example: /song "Enter the song name here"

/help = This command is coming soon on next update...

```
<br>

## You can change your /start message

```
First go to bot.py and change as your choice! But you need to fork it first and don't forget to star🌟 

class Chat:
    def __init__(self, msg):
        self.chat_id = msg['chat']['id']
        self.user_input = msg['text']
        self.user_input = self.user_input.replace('@songdownload597_bot', '')
        self.user_name = msg['from']['first_name']
        self.message_id = msg['message_id']

        self.messages = {
            'start':'🤖 Hello, '+ self.user_name +'!\n\n'
                    '📩 I can download songs for you. Just send me the song name in below format:\n\n'
                    '"*/song*  _song name_"  or\n'
                    '"*/song*  _musician name - song name_"\n\n'
                    'to download some songs. 🎶',

```

<br>

## Screenshots
<br>
<img src="Screenshot (20).png">
<br>
<img src="Screenshot (18).png">
<br>
<img src="Screenshot (19).png">

## What's New in this version 1.9v✨
 - Increase the downoading speed by x3🚅
 - Added youtube link🔗
 - Added a greet message after complete downloading📩
 - Minor bug fixes📶
 - Optimizations

<br>

## Deployment Methods

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sanila2007/Telegram-Song-Downloader-Bot)

## Developer 🤗

[Sanila Ranatunga](https://github.com/sanila2007)
