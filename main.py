#!/usr/bin/python

import config
import random
import twitter

api = twitter.Api(consumer_key=config.consumer_key,
                  consumer_secret=config.consumer_secret,
                  access_token_key=config.access_token_key,
                  access_token_secret=config.access_token_secret)

Status = "Waheey!"
fall = random.randint(0,3)

if fall == 0:
	Status = "Waheey!"
elif fall == 1:
	Status = "Waheey! @ectplvzm"
elif fall == 2:
	Status = "Waheey! @CubeDachs"
elif fall == 3:
	Status = "Waheey! @ExNGBLU"

status = api.PostUpdate(Status)
print(status.text)
