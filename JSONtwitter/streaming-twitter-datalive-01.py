import twython
from twython import Twython,TwythonError

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = '-'
OAUTH_TOKEN_SECRET = ''
twitter = Twython(app_key=APP_KEY, app_secret=APP_SECRET,oauth_token=OAUTH_TOKEN, oauth_token_secret=OAUTH_TOKEN_SECRET)

try:
    search_results = twitter.search(q='#test1001shk', count=1000)

except TwythonError as e:
    print e

for tweet in search_results['statuses']:
    print 'Tweet from @%s Date: %s' % (tweet['user']['screen_name'].encode('utf-8'),tweet['created_at'])
    print tweet['text'].encode('utf-8'), '\n'
