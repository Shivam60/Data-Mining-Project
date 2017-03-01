from twython import TwythonStreamer
from twython import Twython

APP_KEY = 'HWXEFpnCXr7hnHqm946JRAeev'
APP_SECRET = 'hgfwxD3NEgP9rEFWr5vFR8KPR9Q9aT7jSQfOQpMfUunfPv7j6j'
OAUTH_TOKEN = '219146133-mjBvMnWJRzylketWtyzajcXMT3terBFCXcWiJJ7V'
OAUTH_TOKEN_SECRET = 'TI2xPJulbr8GDmuqwyomIlfcWwiMcuLkLkuoDndMz9xt6'

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            print data['text'].encode('utf-8')
    def on_error(self,status_code,data):
        print status_code

stream=MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
stream.statuses.filter(track=['economy', 'abvp', 'bjp'])
