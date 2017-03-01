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
#search = twitter.get_place_trends(id=28743736)
#tweets = search['statuses']
ind=2295401
mum=2295019
mumbai = twitter.get_place_trends(id=2295401)
trend_array = []

if mumbai:
    for trend in mumbai[0].get('trends', []):
        trend_array.append(trend['name'])
    for i in trend_array:
        print i
    #print trend_array
       # print trend