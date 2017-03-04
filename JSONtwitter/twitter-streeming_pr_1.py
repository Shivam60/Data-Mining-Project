
from twython import TwythonStreamer
from twython import Twython
import datetime
import json

APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = '-'
OAUTH_TOKEN_SECRET = ''

woeid=2295401 #india
tweet_val={}
trend_array = []


now = datetime.datetime.now()
outfn = "twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year)
json_arr=[]
tweet_val={}
class MyStreamer(TwythonStreamer):
    def on_success(self,data):
        if 'text' in data:
            if(data['user']['lang']=='en'):
                tweet_val.update({'text':data['text']})
                tweet_val.update({'created_at':data['created_at']})
                tweet_val.update({'location':data['user']['location']})
                tweet_val.update({'time_zone':data['user']['time_zone']})
                tweet_val.update({'lang':data['user']['lang']})
                tweet_val.update({'geo_enabled':data['user']['geo_enabled']})
                tweet_val.update({'source':data['source']})
                tweet_val.update({'coordinates':data['coordinates']}) 
                tweet_val.update({'entities':data['entities']}) 
            print tweet_val,len(tweet_val)
            json_arr.append(tweet_val.copy())
            if len(json_arr)>1000:
                self.disconnect()
    def on_error(self,status_code,data):
        print status_code
twittertrend=Twython(app_key=APP_KEY,app_secret=APP_SECRET,oauth_token=OAUTH_TOKEN,oauth_token_secret=OAUTH_TOKEN_SECRET)

place = twittertrend.get_place_trends(id=woeid)
'''
if place:
    for trend in place[0].get('trends', []):
        trend_array.append(trend['name'])
for i in trend_array:
      print i

track=raw_input("Enter Trend To search For: ")
'''
try:
    stream=MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
    stream.statuses.filter(track='logan')
except:
    print 1
    pass

print json_arr
try:
    with open(outfn,'w') as outfile:
        json_obj=json.dump(json_arr,outfile,sort_keys='True',indent=4)
except IOError:
    print('An error occured trying to read the file.')  
except:
    print('An error occured.')
finally:
    outfile.close()
