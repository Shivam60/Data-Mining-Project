import twython
from twython import Twython

APP_KEY = '1a2J9sDvexWIbJxl0RfdknihM'
APP_SECRET = 'WOIlIzt9wUrrB1U286bi75B0YRxzqwYo4rMDHwTyeUtTB8VFRs'
OAUTH_TOKEN = '219146133-XWOI8QFUfsNeIitwifJDmUDBPR7JLyx9qdIBP4Z2'
OAUTH_TOKEN_SECRET = 'b6tS8wgqlZBv0Rx7hs434dNdUMFfwrdA2HvGwihVKgmTg'


twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
results = twitter.search(q='twitter')
if results.get('statuses'):
    for result in results['statuses']:
        print result['id_str']