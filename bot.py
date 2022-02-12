import os
import youtube_dl
import telepotpro
from random import randint
from multiprocessing import Process
from youtubesearchpython import VideosSearch
from dotenv import load_dotenv
from os.path import join, dirname

dotenv_place = join(dirname(__file__), ".env")
load_dotenv(dotenv_place)

TOKEN = os.environ.get("TOKEN")
bot = telepotpro.Bot(TOKEN)


class song:
    def __init__(self, user_get, reply):
        self.chat = Chat
        self.user_get = user_get[6:]

    def search_songs(self, user_get):
        return VideosSearch(user_get, limit=1).result()

    def get_title(self, results):
        return results["results"][0]["title"]

    def get_duration(self, results):
        results = results["results"][0]["duration"].split(":")
        time_minutes_duration = int(results[0])
        split_count = len(results)

        return time_minutes_duration, split_count

    def download_songs(self, file_name, link):
        ydl_opts = {
            'outtmpl': './' + file_name,
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
            'prefer_ffmpeg': True
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=True)

        pass


class Chat:
    def __init__(self, reply):
        self.chat_id = reply["chat"]["id"]
        self.user_get = reply["Text"]
        self.user_get = self.user_get.replace["@songdownload507_bot", ""]
        self.user_name = reply["from"]["first_name"]
        self.message_id = reply["message_id"]

        self.message = {
            'start': '🤖 Hello, ' + self.user_name + '!\n\n'
                                                     'You can download songs using this bot. Send me the song name in below format.\n\n'
                                                     '"*/song* _song name_"  or\n'
                                                     '"*/song* _musician name - song name_"\n\n'
                                                     'to download some songs. 🎶',

            'spotify_input_error': "‼️ *Oops! The bot doesn't support Spotify links!*\n"
                                   'Try: "*/song* _song name_"\n'
                                   'or: "*/song* _musician name - song name_"',

            'invalid_command': '‼️ *Oops! Invalid command!*\n'
                               'Try: "*/song* _song name_"\n'
                               'or: "*/song* _musician name - song name_"',

            'too_long': '‼️ *Oops! Video too long to convert!*\n'
                        'Order something 30 minutes or less.'

        }

        self.check_input(self.user_get, reply)

        pass

    def send_message(self, content):
        return bot.sendMessage(self.chat_id, content, reply_to_message_id=self.message_id, parse_mode="Markdown")

    def delete_message(self, message):
        chat_id = message["chat"]["id"]
        message_id = message["message_id"]
        bot.deleteMessage((chat_id, message_id))

        pass

    def send_audio(self, file_name):
        bot.sendAudio(self.chat_id, audio=open(file_name, "rb"), reply_to_message_id=self.message_id)

        pass

    def process_request(self, user_get):
        results = song.search_songs(self, user_get[6:])

        time_minutes_duration, split_count = song.get_duration(self, results)

        if int(time_minutes_duration) < 30 and split_count < 3:
            file_name = song.get_title(self, results) + ' -@songdownload397_bot ' + str(randint(0, 999999)) + '.mp3'
            file_name = file_name.replace('"', '')

            self.send_message(f"🎵 {song.get_title(self, results)}\n🔗 {song.get_link(self, results)}")
            downloading_message = self.send_message('⬇️ Downloading... \n_(this may take a while.)_')

            song.download_songs(self.file_name, song.get_link(self, results))

            try:
                self.send_audio(file_name)
                self.delete_message(downloading_message)
                self.send_message('✅ Song downloaded!\nFeel the song🎵')
                print("\nDownloaded successfully!\n")

            except:
                print("\nError")

            os.remove(file_name)
            pass

    def check_input(self, user_get, reply):
        if user_get.startswith('/start'):
            self.send_message(self.messages['start'])

        elif user_get.startswith('/song') and user_get[6:] != '':
            if 'open.spotify.com' in user_get[6:]:
                self.send_message(self.messages['spotify_input_error'])

            else:
                # Valid command
                self.process_request(user_get)

        else:
            # Invalid command
            self.send_message(self.messages['invalid_command'])

        pass

        def start_new_chat(msg):
            Process(target=Chat, args=(reply,)).start()

        bot.message_loop(start_new_chat, run_forever=True)
