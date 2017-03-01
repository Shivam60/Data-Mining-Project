import twython
from twython import Twython
APP_KEY = 'HWXEFpnCXr7hnHqm946JRAeev'
APP_SECRET = 'hgfwxD3NEgP9rEFWr5vFR8KPR9Q9aT7jSQfOQpMfUunfPv7j6j'
OAUTH_TOKEN = '219146133-mjBvMnWJRzylketWtyzajcXMT3terBFCXcWiJJ7V'
OAUTH_TOKEN_SECRET = 'TI2xPJulbr8GDmuqwyomIlfcWwiMcuLkLkuoDndMz9xt6'
twitter = Twython(app_key=APP_KEY, 
            app_secret=APP_SECRET,
            oauth_token=OAUTH_TOKEN, 
            oauth_token_secret=OAUTH_TOKEN_SECRET)
search = twitter.search(q='#oscars',count=10)
tweets = search['statuses']
i=0

for tweet in tweets:
  print i+1
  i+=1
  print tweet['user']['time_zone'], '\n', tweet['text'], '\n\n\n'