#################################
# MARKOV GENERATOR BOT          #
#################################
# Generates a Markov chain when #
# prompted to by /u/slukaj      #
#################################   
# USR: /u/slukaj_markovbot      #
# PSW: 6UysNPWt                 #
#################################

import praw, time
from collections import Counter
from operator import itemgetter

user_agent = "Markov Chain Generator that monitors /u/slukaj | V0.1"
r = praw.Reddit(user_agent=user_agent)

r.login(username="slukaj_markovbot",password="6UysNPWt")
print("Login sucessful")

already_done = [] # list of all posts handled by /u/slukaj_markovbot

user = "slukaj"
slukaj = r.get_redditor(user)
print("Got /u/slukaj")

