from twython import TwythonStreamer
from twython import Twython
import datetime
import json

now = datetime.datetime.now()
outfn = "twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year)

with open(outfn) as file:
    data=json.load(file)
print data
