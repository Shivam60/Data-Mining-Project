import twython
from twython import Twython
APP_KEY = '1a2J9sDvexWIbJxl0RfdknihM'
APP_SECRET = 'WOIlIzt9wUrrB1U286bi75B0YRxzqwYo4rMDHwTyeUtTB8VFRs'
OAUTH_TOKEN = '219146133-XWOI8QFUfsNeIitwifJDmUDBPR7JLyx9qdIBP4Z2'
OAUTH_TOKEN_SECRET = 'b6tS8wgqlZBv0Rx7hs434dNdUMFfwrdA2HvGwihVKgmTg'
twitter = Twython(app_key=APP_KEY, 
            app_secret=APP_SECRET,
            oauth_token=OAUTH_TOKEN, 
            oauth_token_secret=OAUTH_TOKEN_SECRET)
print twitter.get_user_timeline()
#search = twitter.search(q='#omg',count=100)
#tweets = search['statuses']

#for tweet in tweets:
 # print tweet['id_str'], '\n', tweet['text'], '\n\n\n'