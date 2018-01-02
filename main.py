#!/usr/bin/python

import config
import random
import twitter

api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key=config.access_token_key,
                  access_token_secret=config.access_token_secret)

# generate string with a random amound of e's
es = "e" * random.randint(1,130)

# create the tweet string
# there's a small chance of the string being capitalized
if random.randint(0,1) == 1:
    Status = "Wah".upper() + es.upper() + "y!".upper()
else:
    Status = "Wah" + es + "y!"

# Post the tweet
status = api.PostUpdate(Status)
print(status.text)
