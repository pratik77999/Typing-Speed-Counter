'''Typing speed counter using python'''

from random import *
from time import *
from math import floor

sentences=['Please take your dog, Cali, out for a walk - he really needs some exercise!','What a beautiful day it is on the beach, here in beautiful and sunny Hawaii.','Rex Quinfrey, a renowned scientist, created plans for an invisibility machine.','Do you know why all those chemicals are so hazardous to the environment?','You never did tell me how many copper pennies where in that jar; how come?','Max Joykner sneakily drove his car around every corner looking for his dog.','The two boys collected twigs outside, for over an hour, in the freezing cold!','When do you think they will get back from their adventure in Cairo, Egypt?','Trixie and Veronica, our two cats, just love to play with their pink ball of yarn.','We climbed to the top of the mountain in just under two hours; isn’t that great?','This is the date your letter was completed and is ready for mailing.  It should be aligned with the left margin.  The date should be at least three spaces below the heading.']

def fun():
    while True:
        print('First read this ==>')
        print('-'*100)
        random_sentence=choice(sentences)

        #splitting a sentence into many words
        list_of_words=random_sentence.split()          

        print(random_sentence)

        print('-'*100)

        count=0
        list_of_wrong_words=[]
        list_of_ture_words=[]

        option=input("If you want to start press 1 :").strip()
        if option=='1':
            timer1=perf_counter()
            write=input("Write from here : ")
            list_of_input_words=write.split()
            timer2=perf_counter()
            timer=timer2-timer1

            for word in list_of_input_words:
                if word not in list_of_words:
                    count=count+1
                    list_of_wrong_words.append(word)
                else:
                    list_of_ture_words.append(word)

        else:
            print("You entered wrong number!!! Try again..")

        if option=='1':
            length=len(list_of_ture_words)
            second_per_word=timer/length
            words_per_minute=floor((1/second_per_word)*60)

            print(f"There are {len(list_of_words)} words in the sentence and you incorrect {len(list_of_wrong_words)} words {list_of_wrong_words}")
            print(f"You correct {len(list_of_ture_words)} word and these words are ",list_of_ture_words)
            print(f"Your typing speed is {second_per_word} second per word")
            print(f"Your typing speed is {words_per_minute} words per minute")

            print()
            continunity=input("Do you want to play again? (Yes/No) :").strip()
            if continunity.lower()=='no':
                break

            print('-'*100)
fun()



