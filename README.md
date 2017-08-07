Simple-Twitter-Sentiment

This program is to get percentage of positive, negative and neutral tweet reponses for a keyword search on Twitter.

Dependencies:
 -tweepy-3.5.0
 -textblob-0.11.1

It requires two commandline arguments, search-keyword and number of maximum tweets to pull.

Sample run:

python twitter_sentiments.py "Donald Trump" 100
positive sentiment 43.0% negative sentiment 32.0% neutral sentiment 25.0%