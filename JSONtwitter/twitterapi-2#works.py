import twython
from twython import Twython
APP_KEY = ''
APP_SECRET = ''
OAUTH_TOKEN = '-'
OAUTH_TOKEN_SECRET = ''
twitter = Twython(app_key=APP_KEY, 
            app_secret=APP_SECRET,
            oauth_token=OAUTH_TOKEN, 
            oauth_token_secret=OAUTH_TOKEN_SECRET)
j=0
tweet_total=[]
tweet_limit=1000
max_attempt=100
next_max_id=0

for i in range(max_attempt):
    if(tweet_limit<len(tweet_total)):
        break
    if(i==0):        
        search = twitter.search(q='#ABVP',count=100)
    else:
        search=twitter.search(q='#ABVP',include_entities='true',max_id=next_max_id)
    for result in search['statuses']:
        print j
        j=j+1
        print result['user']['screen_name'],result['text']
        #key=result['screen_name']
        #val=result['text']
        #tweet_total.update(key,str(val))
    try:
        next_results_url_params = search['search_metadata']['next_results']
        next_max_id= next_results_url_params.split('max_id=')[1].split('&')[0]
    except:
        break
    #print tweet_total
