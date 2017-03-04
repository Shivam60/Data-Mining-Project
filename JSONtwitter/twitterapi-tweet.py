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
tweet="#ACM taking a workshop on api, tweeted via @twython"
twitter.update_status(status=tweet)
tweets=twitter.search(q="#ACM",count=10)
results=tweets['statuses']
for i in results:
    print i['text']
