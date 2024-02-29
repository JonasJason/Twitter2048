"""
import tweepy
import config

client = tweepy.Client(bearer_token=config.BEARER_TOKEN, access_token=config.API_KEY, access_token_secret=config.API_SECRET)

users = client.get_users(usernames=["Community2048"])

for user in users:
    print(user)

"""
import tweepy
import config

# Replace these values with your own API keys and access tokens
consumer_key = 'your_consumer_key'
consumer_secret = 'your_consumer_secret'
access_token = 'your_access_token'
access_token_secret = 'your_access_token_secret'

# Authenticate with Twitter
auth = tweepy.OAuthHandler(config.API_KEY, config.API_SECRET)
auth.set_access_token(config.ACCESS_TOKEN, config.ACCESS_SECRET)

# Create the API object
api = tweepy.API(auth)



# Specify the text of the tweet
tweet_text = "Which programming language do you prefer?"

# Specify the options for the poll
options = ["Python", "JavaScript", "Java", "C++"]

# Concatenate the options into a string
options_string = ','.join(options)

# Post the tweet with the poll
try:
    api.update_status(status=f"{tweet_text} ({options_string})", tweet_mode="extended", auto_populate_reply_metadata=True)

    print("Poll posted successfully!")

except tweepy.TweepyException as e:
    print("Error posting the poll:", e)