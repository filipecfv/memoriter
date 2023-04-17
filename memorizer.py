"""
Name: brute-force-poetry-memorizer 
Version: 0.1
Last modified: 2023-IV-17
Description: a simple command line poetry (or list itens) memorizer
             inspired by Alexandre Soares Silva's memorization method   
Author: github.com/filipecfv 
License: GPL-3.0
"""

# Beginning

import os
import sys

if os.name == 'posix':
    clear = lambda : os.system('clear')
else:
    clear = lambda : os.system('cls')

def memorize(file):
    open_poem(file)

def open_poem(file):
    poem = open(file, "r").read()
    remove_extra_spaces(poem)

def remove_extra_spaces(poem):
    poem = poem.strip()
    initial_view(poem)

def initial_view(poem):
    clear()
    print(poem)
    input('\n\n\n>>> Memorize [enter]')
    clear()
    extract_lines_from_the_poem(poem)

def extract_lines_from_the_poem(poem):
    lines = poem.split('\n')
    remove_line_spaces(poem, lines)

def remove_line_spaces(poem, lines):
    lines = [l.strip() for l in lines]
    set_counters(poem, lines)

def set_counters(poem, lines):
    counter = 0
    v = 0
    memorized = []
    print_incremental_lines(poem, lines, memorized, counter, v)

def print_incremental_lines(poem, lines, memorized, counter, v):
    memorized.append('{}. '.format(counter+1) + lines[counter])
    print("Memorize: \n\n" + "\n".join(memorized))
    recall(poem, lines, memorized, counter, v)

def recall(poem, lines, memorized, counter, v):
    input("\n\n>>> Recall [Enter]")
    clear()
    memory_test(poem, lines, memorized, counter, v)

def memory_test(poem, lines, memorized, counter, v):  
    if input('{}. '.format(v+1)).strip() == lines[v]:
        print('\n\n\n>>> Correct!')
        input('>>> Press enter to continue')
        clear()
        approved(poem, lines, memorized, counter, v)
    else:
        fail_message(poem, lines, v)

def approved(poem, lines, memorized, counter, v):
        if v < counter:
            print('\n'.join(memorized[:v+1]))
            v = v + 1
            memory_test(poem, lines, memorized, counter, v)
        else: 
            counter_update(poem, lines, memorized, counter, v)
    
def counter_update(poem, lines, memorized, counter, v):
    clear()
    if counter + 1 == len(lines): 
        final_message()
    else: 
        counter = counter + 1
        v = 0
        clear()
        print_incremental_lines(poem, lines, memorized, counter, v)

def fail_message(poem, lines, v):
    print('\n\n>>> Incorrect')
    print('Correct answer:\n    ' + lines[v])
    retry(poem)

def retry(poem):
    answer = input('\n\nRetry? [y/n]  ')
    if answer == 'y':
        memorize(sys.argv[2])
    elif answer == 'n':
        print("Okay, looser! :P")
    else:
        clear()
        retry(poem)

def final_message():
    print('Congrats!')

def help():
    help = open('help', 'r').read()
    print(help)

def main():
    if len(sys.argv) <= 1: 
        print("Sorry: you haven't provided a function")
    else: 
        if sys.argv[1] == "memorize":
            memorize(sys.argv[2])
        elif sys.argv[1] == "help":
            help()
            
if (__name__ == "__main__"):
    main() 

# end
