import pyfiglet
import tweepy
import random
import time

auth = tweepy.OAuthHandler('OAUTH_TOKEN','OAUTH_SECRET')
auth.set_access_token('CONSUMER_KEY','CONSUMER_SECRET')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

user = api.me()

t = random.randint(26, 41)

search = 'YOUR KEYWORD'
likes = 9


txt = pyfiglet.figlet_format(f'{search}', font="slant")

print(txt)

for tweet in tweepy.Cursor(api.search, search).items(likes):
    try:
        tweet.favorite()
        print(f'• likes a tweet from search: {search}')
        time.sleep(t)
    except tweepy.TweepError as e:
        print(e.reason)
        print(f'• failed to like a tweet from search: {search}')
        time.sleep(t)
    except StopIteration:
        break
