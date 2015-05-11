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

#r.login(username="slukaj_markovbot",password="6UysNPWt")
#print("Login sucessful")

#already_done = [] # list of all posts handled by /u/slukaj_markovbot

user = "slukaj"
slukaj = r.get_redditor(user)
print("Got /u/slukaj")

words = list()

print("Getting comments...")
comment_limit = 1000
comments = slukaj.get_comments(limit=comment_limit)
comment_list = []
for thing in comments:
    comment_string = str(thing.body)
    comment_list.append(comment_string.lower())

print("Generating dictionary...")
markov_dictionary = {}
for comment in comment_list:
    split_comment = comment.split()
    if(len(split_comment)>=3):
        for i in range(0,len(split_comment)-1):
            if(i!=len(split_comment)-2):
                keytuple = split_comment[i]+" "+split_comment[i+1]+" "+split_comment[i+2]
                if keytuple in markov_dictionary:
                    markov_dictionary[keytuple] += 1
                else:
                    markov_dictionary[keytuple] = 1

print("Done. Dictionary ready!")
print("-----------------------")
print("Size of dictionary: "+str(len(markov_dictionary)))
print("Writing dictionary file")

f = open("dictionary.txt",'w')
for entry in markov_dictionary:
    f.write(entry+" "+str(markov_dictionary[entry])+"\n")
f.close()
print("File written")
