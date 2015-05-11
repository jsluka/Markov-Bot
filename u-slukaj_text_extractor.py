#################################
# COMMENT MINER                 #
#################################

import praw, time
from collections import Counter
from operator import itemgetter

user_agent = "Comment minor that monitors /u/slukaj | V0.1"
r = praw.Reddit(user_agent=user_agent)

user = "slukaj"
slukaj = r.get_redditor(user)
print("Got /u/slukaj")

print("Getting comments...")
comments = slukaj.get_comments(limit=1000)
file = open("dictionary.txt","w")

for thing in comments:
    comment_string = str(thing.body)
    file.write(comment_string.lower())
file.close()

print("Dictionary written.")
