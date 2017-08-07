import tweepy
import sys
import re
import textblob

search = sys.argv[1]
count_max = int(sys.argv[2])

# Connect to twitter API using tweepy lib
def get_api(cfg):
    auth = tweepy.OAuthHandler( cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)

# twitter API credentials
cfg = {
    "consumer_key"        : "get-consumer_key-here",
    "consumer_secret"     : "get-consumer_secret_here",
    "access_token"        : "get_access_token_here",
    "access_token_secret" : "get_access_token_secret_here"
    }

api = get_api(cfg)
count = 0
positive = 0
negative = 0
neutral = 0
def get_tweet_sentiment(tweet):
    tweet = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
    analysis = textblob.TextBlob(tweet)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'

def to_perc(count):
    value = (count/count_max)*100
    return round(value,2)

def search_tweets():
    tweets = []
    count = 0
    positive = 0
    negative = 0
    neutral = 0
    try:
        get_tweets = api.search(q=search, count=count_max)
        for tweet in get_tweets:
            #print(tweet.text)
            count = int(count) + 1
            each_tweet = {}

            each_tweet['text'] = tweet.text
            each_tweet['user'] = tweet.user.screen_name


            each_tweet['sentiment'] = get_tweet_sentiment(tweet.text)
            if each_tweet['sentiment'] == "positive":
                positive = positive +1
            if each_tweet['sentiment'] == "negative":
                negative = negative +1
            if each_tweet['sentiment'] == "neutral":
                neutral = neutral +1

            print(each_tweet)


    except tweepy.TweepError as e:
            print("Error : " + str(e))
    result_line = "positive sentiment {}% negative sentiment {}% neutral sentiment {}%"\
                    .format(to_perc(positive),to_perc(negative),to_perc(neutral))

    print(result_line)