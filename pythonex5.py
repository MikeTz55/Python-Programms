import datetime
from twython import Twython # pip install twython

CONSUMER_KEY = '20ysHnnnb82HXkT1rckKkbFB3'
CONSUMER_SECRET = 'dJMuUHZl7PwKies3Q0IdwwxDRrJg0tZ897F1xNrBu22bIwJGEI'
ACCESS_KEY = '834777543328808961-4Jxmdxhn3rDLrwDq6UuO4sXHo284e2T'
ACCESS_SECRET = 'V8fdxkZXaYYRmymshBTQMkJnEqMkOZwJuowT6usB1C01o'



def Count_the_words(user_name):
    number_of_tweets = 10
    twitter = Twython(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
    lis = [467020906049835008] ## this is the latest starting tweet id
    user_timeline = twitter.get_user_timeline(screen_name=user_name,count=200, include_retweets=False)
    tweet_count = 0
    total_word_counts = 0
    for tweet in user_timeline:
        tweet_count = tweet_count + 1
        #print tweet_count, ".", tweet['text']  ## print the tweet
        temp = tweet['text']
        word_counts_on_tweet = len(temp.split())
        total_word_counts = total_word_counts + word_counts_on_tweet
        if tweet_count == number_of_tweets:
            return total_word_counts
            break
        else:
            lis.append(tweet['id']) ## append tweet id's

if __name__ == '__main__':
        PrintHeaderInfo()
        username_a = raw_input('User, please give me the username from Twitter(R)...')
        print "User's :",username_a, "most common word is : ", 
