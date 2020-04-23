# Import required packages
from account import id, secret, appName, username
import praw # Python Reddit API Wrapper
import pandas as pd 
import datetime as dt

# Reddit and subreddit instances
reddit = praw.Reddit(client_id=id, \
                     client_secret=secret, \
                     user_agent=appName, \
                     username=username)

submission = reddit.submission(id='g6gz0e')
title = submission.title
body = submission.selftext

text_to_classify = title + body