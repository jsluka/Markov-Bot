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
# PSW:                          #
#################################

import praw, time, sys
from collections import Counter
from operator import itemgetter
from random import choice 
#from random import choice

user_agent = "Markov Chain Generator that monitors /u/slukaj | V0.3"
r = praw.Reddit(user_agent=user_agent)
slukaj = r.get_redditor("slukaj") 
dictionary = {}

already_done = [] # list of all posts handled by /u/slukaj_markovbot

def reddit_login():
    r.login(username="slukaj_markovbot",password="")
    print("Login sucessful")

def check_comments():
    comments = slukaj.get_comments(sort='new',time='all',limit=25)
    for thing in comments:
        if "/u/slukaj_markovbot" in str(thing.body):
            if not already_replied(thing):
                reply_to_comment(thing)
    print("Checked comments...") 

def already_replied(thing):
    if str(thing.id) in already_done:
        return True
    else:
        return False

def reply_to_comment(thing):
    add_to_done_list(str(thing.id))
    thing.reply(generate_gibberish(40))

def add_to_done_list(idstring):
    already_done.append(idstring)
    with open("processedcomments.txt","a") as f:
        f.write(idstring+"\n")
    print("Writing file...")

def build_dictionary(wordlist):
    for i, word in enumerate(wordlist):
        try:
            first, second, third = wordlist[i],wordlist[i+1],wordlist[i+2]
        except IndexError:
            break #Ignores the last two words
        key = (first,second)
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(third)

def generate_gibberish(length):
    key = choice(list(dictionary.keys()))
    #key = ("it","was")
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
    sentence = ' '.join(li)
    sentence = sentence[0:].capitalize() + sentence[:0] + "..."
    return sentence

def read_data():
    file = open("dictionary.txt","r")
    rawstring = file.read()
    file.close()
    with open("processedcomments.txt","r") as proc:
        for line in proc:
            already_done.append(line[:len(line)-1])
    wordlist = rawstring.split()
    build_dictionary(wordlist)

def logic_loop():
    while True:
        print("Tick...")
        check_comments()
        time.sleep(605)

def main():
    reddit_login()
    read_data()
    logic_loop()
        
if __name__ == "__main__":
    main()
