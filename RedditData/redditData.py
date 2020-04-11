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

subreddit = reddit.subreddit('india')

# Getting the top 100 posts in the subreddit
top_subreddit = subreddit.top(limit=1000)

# Parsing and Downloading the data
topics_dict = {"title":[], "id":[], "url": [], "body":[], "flair":[]}

for submission in top_subreddit:
    topics_dict["id"].append(submission.id)
    topics_dict["title"].append(submission.title)
    topics_dict["body"].append(submission.selftext)
    topics_dict["flair"].append(submission.link_flair_text)
    topics_dict["url"].append(submission.url)

topics_data = pd.DataFrame(topics_dict)
topics_data.to_csv('RedditData/Data/raw.csv', index=False) 
