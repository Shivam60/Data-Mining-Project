import twython
from twython import Twython
#consumer_key="HWXEFpnCXr7hnHqm946JRAeev"
#consumer_secret="hgfwxD3NEgP9rEFWr5vFR8KPR9Q9aT7jSQfOQpMfUunfPv7j6j"
#access_token_key="219146133-mjBvMnWJRzylketWtyzajcXMT3terBFCXcWiJJ7V"
#access_token_secret="TI2xPJulbr8GDmuqwyomIlfcWwiMcuLkLkuoDndMz9xt6"
APP_KEY = '1a2J9sDvexWIbJxl0RfdknihM'
APP_SECRET = 'WOIlIzt9wUrrB1U286bi75B0YRxzqwYo4rMDHwTyeUtTB8VFRs'
twitter = Twython(APP_KEY, APP_SECRET)
auth = twitter.get_authentication_tokens()
OAUTH_TOKEN = auth['oauth_token']
OAUTH_TOKEN_SECRET = auth['oauth_token_secret']
#print OAUTH_TOKEN, OAUTH_TOKEN_SECRET
print "your url is: " + auth['auth_url']
print "enter PIN"
oauth_verifier=input()

twitter = Twython(APP_KEY, APP_SECRET,OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
final_step = twitter.get_authorized_tokens(oauth_verifier)
OAUTH_TOKEN = final_step['oauth_token']
OAUTH_TOKEN_SECRET = final_step['oauth_token_secret']
print twitter.verify_credentials()