from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import datetime
import re
import json
from collections import Counter
from nltk import FreqDist
now = datetime.datetime.now()
tweet=[]
outfn = "twitter_TEXT_data_%i.%i.%i.txt" % (now.month, now.day, now.year)
infn = "twitter_user_data_%i.%i.%i.txt" % (now.month, now.day, now.year)

with open(infn, 'r') as data_file:
    json_data = data_file.read()

punctuation = list(string.punctuation)
stop = stopwords.words('english') + punctuation + ['rt', 'via','http','https','\u0e37']
data = json.loads(json_data)
clear_text=[]
a=[]
d=[]
for i in data:
    b=re.sub('([\\][\\][u][\d][\e][\d+]+)',"",i['text'])
  #  b=re.sub('([//t.co//]+[\d\w+]+)',"",i['text'])
    c=word_tokenize(b)
    for j in c:
        if j.lower() not in stop: 
            d.append(j.lower())
#    clear_text.append(d)
#print clear_text
#print list(final)
fdist = FreqDist(d)
fdist.plot()
print fdist.most_common(10)
#print fdist1.most_common()
