import praw
import time
from config import *
from datetime import datetime

while True: 
 reddit = praw.Reddit(
    client_id=ClientId,
    client_secret=ClientSecret,
    password=PWD,
    user_agent=UserAgent,
    username=UserName,
 )

 subreddit = reddit.subreddit(stalksub) 

 now = datetime.now()
 subs = reddit.subreddit(stalksub).subscribers

 title=BOTMSG, subs 
 body=BOTMSG, subs
 reddit.subreddit(PostOnSub).submit(title=title, selftext=body)
 now = datetime.now()
 current_time = now.strftime("%H:%M")
 print("success", current_time)
 time.sleep(3600) #time between checks is set to one minute (3600 seconds) 
