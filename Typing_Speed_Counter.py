'''Typing speed counter using python'''

from random import *
from time import *
from math import floor

sentences = [
    'Please take your dog, Cali, out for a walk - he really needs some exercise!']


def fun():
    while True:
        print('First read this ==>')
        print('-'*100)
        random_sentence = choice(sentences)

        # splitting a sentence into many words
        list_of_words = random_sentence.split()

        print(random_sentence)

        print('-'*100)

        count = 0
        list_of_wrong_words = []
        list_of_ture_words = []

        option = input("If you want to start press 1 :").strip()
        if option == '1':
            timer1 = perf_counter()
            write = input("Write from here : ")
            list_of_input_words = write.split()
            timer2 = perf_counter()
            timer = timer2-timer1

            for word in list_of_input_words:
                if word not in list_of_words:
                    count = count+1
                    list_of_wrong_words.append(word)
                else:
                    list_of_ture_words.append(word)

        else:
            print("You entered wrong number!!! Try again..")

        if option == '1':
            length = len(list_of_ture_words)
            second_per_word = timer/length
            words_per_minute = floor((1/second_per_word)*60)

            print(
                f"There are {len(list_of_words)} words in the sentence and you incorrect {len(list_of_wrong_words)} words {list_of_wrong_words}")
            print(
                f"You correct {len(list_of_ture_words)} word and these words are ", list_of_ture_words)
            print(f"Your typing speed is {second_per_word} second per word")
            print(f"Your typing speed is {words_per_minute} words per minute")

            print()
            continunity = input(
                "Do you want to play again? (Yes/No) :").strip()
            if continunity.lower() == 'no':
                break

            print('-'*100)


fun()
