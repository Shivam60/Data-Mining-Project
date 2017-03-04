import twython
from twython import Twython
#consumer_key=""
#consumer_secret=""
#access_token_key="-"
#access_token_secret=""
APP_KEY = ''
APP_SECRET = ''
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
