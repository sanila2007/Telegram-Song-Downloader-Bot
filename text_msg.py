import pyrogram

START_TEXT_MSG = '🤖 Hello user!\n\n📩 I can download songs for you. Just send me the song name in below format:\n\n*/song*  _song name_  or\n*/song*  _musician name - song name_\n\n' 
                 'to download some songs. 🎶\n\n■ If you cannot understand how this bot work you can learn it by [clicking this](https://t.me/sanilaassistant_bot) \n\n' 
                 '■ First [start](https://t.me/sanilaassistant_bot)> Learn Bots > Chose Song downloader\n\n✨ Developer: Sanila Ranatunga\n✨ Feedback: [Submit by clicking](https://t.me/sanilaassistant_bot)'


CONFIRMATION_TEXT_MSG = "✅ Song downloaded successfully!\n\n◉ [Give feedback](https://t.me/sanilaassistant_bot)\n◉ [Learn Bot](https://t.me/sanilaassistant_bot)"

SPOTIFY_INPUT_ERROR_TEXT_MSG = "‼️ *Oops! The bot doesn't support Spotify links!*\n" 
                               'Try: "*/song* _song name_"\n' 
                               'or: "*/song* _musician name - song name_"\n\n' 
                               '■ If you cannot understand how this bot work you can learn it by [clicking this.](https://t.me/sanilaassistant_bot) \n\n' 
                               '■ First [start](https://t.me/sanilaassistant_bot)> Learn Bots > Chose Song downloader'

INVALID_COMMAND_ERROR_TEXT_MSG = '‼️ *Oops! Invalid command!*\n' 
                                 'Try: "*/song* _song name_"\n' 
                                 'or: "*/song* _musician name - song name_"\n\n' 
                                 '■ If you cannot understand how this bot work you can learn it by [clicking this.](https://t.me/sanilaassistant_bot) \n\n' 
                                 '■ First [start](https://t.me/sanilaassistant_bot)> Learn Bots > Chose Song downloader'

TOO_LONG_ERROR_TEXT_MSG = '‼️ *Oops! Video too long to convert!*\n' 
                          'Order something 30 minutes or less.\n\n'
                          '■ If you cannot understand how this bot work you can learn it by [clicking this.](https://t.me/sanilaassistant_bot) \n\n' 
                          '■ First [start](https://t.me/sanilaassistant_bot)> Learn Bots > Chose Song downloader'
