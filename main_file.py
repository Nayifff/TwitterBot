#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  8 19:22:02 2018

@author: Naif
"""

import tweepy
import time

FILE_NAME = 'last_seen_id.txt'


auth = tweepy.OAuthHandler('')
auth.set_access_token('')
api = tweepy.API(auth,wait_on_rate_limit=True)

# This file to retrieve last seen 

def reply_tweets():
    print('retrieving and replying to tweets...')
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    # NOTE: We need to use tweet_mode='extended' below to show
    # all full tweets (with full_text). Without it, long tweets
    # would be cut off.
    mentions = api.mentions_timeline(
                        last_seen_id,
                        tweet_mode='extended')
    for mention in reversed(mentions):
        print(str(mention.id) + ' - ' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#nayif' in mention.full_text.lower():
            print('Someone sent #Nayif')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                    '  ' + 'This is Naifs bot. #Nayif is away. Please wait a bit', mention.id)

while True:
    reply_tweets()
    time.sleep(20)
