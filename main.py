#!/usr/bin/python

import config
import random
import twitter

api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key=config.access_token_key,
                  access_token_secret=config.access_token_secret)

es = "e" * random.randint(1,130)
Status = "Wah" + es + "y!"
if random.randint(0,1) == 1:
    Status = "Wah".upper() + es.upper() + "y!".upper()

status = api.PostUpdate(Status)
print(status.text)
