from twython import TwythonStreamer
from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = '-'
OAUTH_TOKEN_SECRET = ''

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            print data['text'].encode('utf-8')
    def on_error(self,status_code,data):
        print status_code

stream=MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
stream.statuses.filter(track=['economy', 'abvp', 'bjp'])
