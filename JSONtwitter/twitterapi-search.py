import twython
from twython import Twython
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = '-'
OAUTH_TOKEN_SECRET = ''
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
