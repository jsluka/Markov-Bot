#################################
# With much thanks to:          #
# https://pythonadventures.wordpress.com/2014/01/23/generating-pseudo-random-text-using-markov-chains/ #
#################################
# MARKOV GENERATOR BOT          #
#################################
# Generates a Markov chain when #
# prompted to by /u/slukaj      #
#################################   
# USR: /u/slukaj_markovbot      #
# PSW: 6UysNPWt                         #
#################################

import praw, time, sys
from collections import Counter
from operator import itemgetter
from random import choice

user_agent = "Markov Chain Generator that monitors /u/slukaj | V0.2"
r = praw.Reddit(user_agent=user_agent)
slukaj = r.get_redditor("slukaj")

already_done = [] # list of all posts handled by /u/slukaj_markovbot

def reddit_login():
    r.login(username="slukaj_markovbot",password="")
    print("Login sucessful")

def check_comments():
    comments = slukaj.get_comments(sort='new',time='all',limit=5)
    for thing in comments:
        if "/u/slukaj_markovbot" in str(thing.body):
            print("Found a comment!")
            if not already_replied(thing):
                reply_to_comment(thing)
    print("Checked comments...") 

def already_replied(thing):
    if thing.id in already_done:
        print("Already done.")
        return True
    else:
        print("Not yet done!")
        return False

def reply_to_comment(thing):
    print("Replying to comment!")
    already_done.append(thing.id)
    thing.reply("I don't know!")

def build_dictionary(wordlist):
    d = {}
    for i, word in enumerate(wordlist):
        try:
            first, second, third = wordlist[i],wordlist[i+1],wordlist[i+2]
        except IndexError:
            break #Ignores the last two words
        key = (first,second)
        if key not in d:
            d[key] = []
        d[key].append(third)
    return d

def generate_gibberish(dictionary,length):
    key = ("it","was")
    li = []
    first, second = key
    li.append(first)
    li.append(second)
    if(length < 3):
        return 0
    for i in range(0,length):
        try:
            third = choice(dictionary[key])
        except KeyError:
            break
        li.append(third)
        key = (second, third)
        first, second = key
    return ' '.join(li)

def main():
    reddit_login()
    check_comments()
    file = open("dictionary.txt","r")
    rawstring = file.read()
    file.close()
    wordlist = rawstring.split()
    dictionary = build_dictionary(wordlist)
    gibberish = generate_gibberish(dictionary,35)
    print(gibberish)
        
if __name__ == "__main__":
    main()

