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
tweet="#ACM taking a workshop on api, tweeted via @twython"
twitter.update_status(status=tweet)
tweets=twitter.search(q="#ACM",count=10)
results=tweets['statuses']
for i in results:
    print i['text']