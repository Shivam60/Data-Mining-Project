
from twython import TwythonStreamer
from twython import Twython
import datetime
import json

now = datetime.datetime.now()
outfn = "twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year)

class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            tweet_val.update({'text':data['text']})
            tweet_val.update({'created_at':data['created_at']})
            tweet_val.update({'location':data['user']['location']})
            tweet_val.update({'time_zone':data['user']['time_zone']})
            tweet_val.update({'lang':data['user']['lang']})
            tweet_val.update({'geo_enabled':data['user']['geo_enabled']})
            tweet_val.update({'source':data['source']})
            tweet_val.update({'coordinates':data['coordinates']}) 
            tweet_val.update({'locatentitiesion':data['entities']}) 
            print tweet_val
            try: 
                with open(outfn,'a') as outfile:
                    json_obj=json.dump(tweet_val,outfile,sort_keys='True',indent=4)
            except IOError:
                print('An error occured trying to read the file.')
            except:
                print('An error occured.')
            finally:   
                outfile.close()
            tweet_val.clear()
    def on_error(self,status_code,data):
        print status_code

try:
    open(outfn,'w')
except IOError:
    print('An error occured trying to read the file.')
except:
    print('An error occured.')

APP_KEY = 'HWXEFpnCXr7hnHqm946JRAeev'
APP_SECRET = 'hgfwxD3NEgP9rEFWr5vFR8KPR9Q9aT7jSQfOQpMfUunfPv7j6j'
OAUTH_TOKEN = '219146133-mjBvMnWJRzylketWtyzajcXMT3terBFCXcWiJJ7V'
OAUTH_TOKEN_SECRET = 'TI2xPJulbr8GDmuqwyomIlfcWwiMcuLkLkuoDndMz9xt6'

woeid=2295401 #india

tweet_val={}
trend_array = []
twittertrend=Twython(app_key=APP_KEY,app_secret=APP_SECRET,oauth_token=OAUTH_TOKEN,oauth_token_secret=OAUTH_TOKEN_SECRET)

place = twittertrend.get_place_trends(id=woeid)
if place:
    for trend in place[0].get('trends', []):
        trend_array.append(trend['name'])
for i in trend_array:
    print i
track=raw_input("Enter Trend TO search For: ")
stream=MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET,10)
stream.statuses.filter(track=track)
