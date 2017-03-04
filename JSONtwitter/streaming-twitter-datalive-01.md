import twython
from twython import Twython

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''


twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
results = twitter.search(q='twitter')
if results.get('statuses'):
    for result in results['statuses']:
        print result['id_str']