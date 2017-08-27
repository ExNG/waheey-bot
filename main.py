#!/usr/bin/env python3

import twitter

api = twitter.Api(consumer_key='',
                  consumer_secret='',
                  access_token_key='',
                  access_token_secret='')

status = api.PostUpdate('Waheey!')
print(status.text)
