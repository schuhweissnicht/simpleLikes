import pyfiglet
import tweepy
import random
import time

auth = tweepy.OAuthHandler('OAUTH_TOKEN','OAUTH_SECRET')
auth.set_access_token('CONSUMER_KEY','CONSUMER_SECRET')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

t = random.randint(12,28)

txt = pyfiglet.figlet_format("Twitter Bot", font="slant")

search = 'YOUR KEYWORD'
likes = 9

print(txt)

for tweet in tweepy.Cursor(api.search, search).items(likes):
    try:
        print(f'likes a tweet from search: {search}')
        tweet.favorite()
        time.sleep(t)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break

    if EOFError(429):
        time.sleep(1200) #20 minutes
