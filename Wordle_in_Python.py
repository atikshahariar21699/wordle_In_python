## The whole code was written by Md. Atik Shahariar
## ide Pycharm professional, with python 3.10
##the 5_letter_words.txt  file was collected from  https://github.com/charlesreid1/five-letter-words/blob/master/sgb-words.txt

import random

## This function reads the 5_letter_words.txt file and returns a list of all the words in the file.
def word_list():
    path="5_letter_words.txt"  ##put text the file path in here
    wordlist = []
    with open(path, 'r') as file:
        for line in file:
            for word in line.split():
                wordlist.append(word)
    return wordlist



#this function takes a list of words as a parameter and returns a random word from this list
def random_word(wordlist):
    return random.choice(wordlist)



#This function takes two parameters, a guess and a word list and returns True if the guess word is in the word list and False otherwise.
def  is_real_word(guess, wordlist):
    if(guess in wordlist):
        return True
    else:
        return False




##This function takes two parameters. The first is the guessed word and the second is the word the user has to find. check_guess() returns a string containing the following characters:
##X for each character in the guess that is at the correct position.
##O for each character in the guess that is in the word but not at the correct position.
##_ for each character in the guess that is not part of the word. For example, check_guess("birds", "words") should return __XXX.
##If a letter is used twice in the guessed word and exists only once in the word to be found, then only one letter in the return string is marked. In case one of the two letters is positioned correctly, then this letter is marked with an X in the return string. For example, check_guess("carat", "train") should return _OO_O. Another example, check_guess("taunt", "train") should return XO_O_

def check_guess(guess, find):
    list_guess = list(guess)     ##converting string to list
    list_find = list(find)     ##converting string to list
    string_xo = "_____"        ##This string will hold the output pattern. by defaut it is considered that, the guess word doesnot match with the find word at all so pattern is "_____"

    for i in range(len(list_guess)):      ##this loop finds if any character of the guess word and the find word has has same value while having SAME index number
        if (list_guess[i] == list_find[i]):
            string_xo = string_xo[0:i] + 'X' + string_xo[i + 1:]    ##replaces '_' character of the string_xo string with character 'X'
            list_find[i] = ' '   ## raplace the character at the fllowing index of list_find list with space , to avoid comparing with the same element over and over again

    for i in range(len(list_guess)):     ##this loop finds if any character of the guess word and the find word has has same value while having DIFFERENT index number
        for j in range(len(list_find)):
            if (list_guess[i] == list_find[j] and string_xo[i]=='_'):
                string_xo = string_xo[0:i] + 'O' + string_xo[i + 1:]     ##replaces '_' character of the string_xo string with character 'O'
                list_find[j] = ' '    ## raplace the character at the fllowing index of list_find list with space , to avoid comparing with the same element over and over again
    print(string_xo);
    #print(list_find);
    return string_xo



##This function takes a word list as a parameter. The function asks the user for a guess, converts the guess to lower case and checks if the guess is in the word list. If this is the case, the guess is returned. Otherwise, the function asks the user for another guess.

def next_guess(wordlist):
    user_input=input("Please enter a guess: ")
    user_input=user_input.lower()
    while (is_real_word(user_input,wordlist)==False):  ## while loop keeps running until a word from the word list is gussed
        print("That's not a real word!")
        user_input = input("Please enter a guess: ")
        user_input = user_input.lower()
    return user_input





#this function
#Uses the functions word_list and random_word to select a random 5 letter word.
#Asks the user for a guess using the next_guess function.
#Checks each guess using the check_guess function and shows the result to the user.
#Checks if the users guessed the right word with six guesses or less. If yes, the user wins and the function prints You won!. Otherwise the user loses and
#the function prints You lost! as well as The word was: followed by the word the user had to find.

def play():
    wordlist=word_list()
    randomword=random_word(wordlist)  #selects a random word from the word list
    ##print(randomword)
    count=0
    win_probability=False    ## false means users has not won or lost yet
    while(win_probability==False and count<6):    ##until user wins or looses or tries six times the while loop keeps running,
        count=count+1
        if(check_guess(next_guess(wordlist),randomword)=="XXXXX"):    ## if user gusses the word correctly he/she wins
            print("You won!")
            win_probability=True
        elif(count==6 and win_probability==False):   ## users tries 6 times still could not guess correctly, he/she looses
            win_probability = True
            print("You lost!")
            print("The word was: "+randomword)

play()

#check_guess("fungi","jujus")
#check_guess("hands","banal")
#check_guess("hands","jenny")
#check_guess("spats","heals")
#check_guess("carat", "train")
#check_guess("taunt", "train")