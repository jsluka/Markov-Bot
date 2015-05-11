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
# PSW: 6UysNPWt                 #
#################################

import praw, time, sys
from collections import Counter
from operator import itemgetter
from random import choice

def reddit_login():
    user_agent = "Markov Chain Generator that monitors /u/slukaj | V0.1"
    r = praw.Reddit(user_agent=user_agent)

    r.login(username="slukaj_markovbot",password="6UysNPWt")
    print("Login sucessful")

    already_done = [] # list of all posts handled by /u/slukaj_markovbot

    user = "slukaj"
    slukaj = r.get_redditor(user)
    print("Got /u/slukaj")

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
    file = open("dictionary.txt","r")
    rawstring = file.read()
    file.close()
    wordlist = rawstring.split()
    dictionary = build_dictionary(wordlist)
    gibberish = generate_gibberish(dictionary,35)
    print(gibberish)

if __name__ == "__main__":
    main()

