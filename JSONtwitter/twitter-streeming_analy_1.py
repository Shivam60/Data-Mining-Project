from twython import TwythonStreamer
from twython import Twython
import datetime
import json
import re
now = datetime.datetime.now()
outfn = "twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year)

with open(outfn, 'r') as data_file:
    json_data = data_file.read()

data = json.loads(json_data)
loc=[]
for i in data:
    a=re.sub('([\\][\\][u][\d][\e][\d+]+)',"",i['text'])
    print a