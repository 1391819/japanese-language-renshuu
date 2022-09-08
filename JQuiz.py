#!/usr/bin/python3.8
# -*-coding: utf8 -*-

# Japanese Verbs Quiz
# Last update: 18/11/2020 - Lesson 18

import os
import random
import time

total_verbs = "110"
last_lesson = "19"
next_lesson = "20"

lessons_array = ["２０", "２１", "２２", "２３", "２４", "２５"]
options_array = ["１", "２", "３", "４", "５"]

os.system('cls')
print("Japanese Verbs Quiz/Review")
print("\nLast lesson: " + last_lesson)
print("\nTotal amount of verbs: " + total_verbs)
print("\n- IMPORTANT -")
print("\n1) Please set your keyboard to Japanese 「ひらがな」 before starting!")
print("2) If you have any problems with the application just contact me at roberto.nacu@gmail.com")
input("\nPress ENTER once you are ready to go...")

def main():

    os.system('cls')
    print("Would you like to:\n\n１) Review verbs studied till now (L4-L" + last_lesson + ")\n２）Practice verbs from new lessons (L" + next_lesson + "-L25)\n３）Close the program")
    print("\nMore details:\n\n１）\n\tYou will be doing a general review of the verbs from all the past lessons.\n\tYou will be asked how many verbs you would like to review.\n\tYou can decide whether to review the verbs' ます -form, their て -form, their ない -form, their Dictionary form or all of them."\
          ,"\n２）\n\tYou will be asked which one of the next lessons you would like to practice.\n\tYou will be reviewing only verbs from only one lesson (could be useful before a VQ).\n\tYou will practice only the verbs' ます -form and the group they are part of.")
    what_to_review = input("\nEnter　１、２ or ３: ")

    # Single-lesson practice
    if(what_to_review == "２"):

        which_lesson_to_review = 0
        while(which_lesson_to_review not in lessons_array):
            os.system('cls')

            print("Please choose the lesson you would like to review [２０、２１、２２、２３、２４、２５]: ")
            which_lesson_to_review = input("\nAnswer: ")

        filename = "data/data" + which_lesson_to_review + ".txt"

        with open(filename,"r", encoding='utf8') as f:
            question = [line.split("/") for line in f]
            used_verbs = [] # Used to not ask the same verb two times
            i = 0
            score = 0

            os.system('cls')

            print("Rules:\n\n1) Each question has 2 parts: the verb's ます -form and the group it is part of. You get 0.50 points for each correctly answered part (up to 1 point for each question)")
            print("2) Once you get 100%, take a 5 minutes break (you could study the remaining vocabularies in the meanwhile) and then try taking the quiz again. Keep doing this until you feel like you memorised all the verbs!")
            print("3) Although this quiz helps you memorise the lesson's verbs, please practice writing them on paper as well!")

            stop = input("\nPress ENTER once you are ready...")
            os.system('cls')

            print("###################################### QUIZ STARTS! ######################################\n")

            while i<len(question):

                answer1_right = False
                answer2_right = False

                while True:
                    num = random.randint(0,len(question)-1)
                    if(question[num][0] not in used_verbs):
                        break

                used_verbs.append(question[num][0])

                print("\nQ" + str(i+1) + ")\ta) What is the ます -form of 「", question[num][0], "」?")
                answer = input("\n\t\tAnswer: ")
                if (answer == str(question[num][1])):
                    print("\n\t\t\tCongratulations! That's right!")
                    score += 1
                else:
                    print("\n\t\t\tWrong! The correct answer was : ", question[num][1])

                print("\n\tb) Which group (１、２、３) is the verb part of?")
                answer = input("\n\t\tAnswer: ")

                if (answer == str(question[num][2])):
                    print("\n\t\t\tCongratulations! That's right!\n")
                    answer1_right = True
                else:
                    print("\n\t\t\tWrong! The correct answer was : " + question[num][2] + "\n")

                if(answer1_right):
                    score += 0.5
                if(answer2_right):
                    score += 0.5

                i += 1


        f.close()

        if score>1:
            sc_pl = "points"
        else:
            sc_pl = "point"

        print("\n##########################################################################################")

        print("\n\nRESULTS:\n\n ", i, "questions, ", score, sc_pl, " \n--> Your score is: ", '{:.2f}'.format((score*100/i)), "%!\n")

        print("\n##########################################################################################")

        print("\n\nPress ENTER  to proceed...")
        input()

        main()

    # General review (all lessons)
    elif(what_to_review == "１"):

        with open("data/data.txt","r", encoding='utf8') as f:
            question = [line.split("/") for line in f]
            used_verbs = [] # Used to not ask the same verb two times
            i = 0
            score = 0
            review_choice = 0

            while(review_choice not in options_array):

                os.system('cls')
                print("Please choose what you would like to review: ")
                print("\n１) ます -form")
                print("\n\tYou'll be given the English meaning of the verb and you need to enter its ます -form.")
                print("\n２) て -form")
                print("\n\tYou'll be given the English meaning of the verb and you need to enter a) the group it is part of and b) its て -form.")
                print("\n３) ない -form")
                print("\n\tYou'll be given the English meaning of the verb and you need to enter a) the group it is part of and b) its ない -form.")
                print("\n４) Dictionary form")
                print("\n\tYou'll be given the English meaning of the verb and you need to enter a) the group it is part of and b) its Dictionary form.")
                print("\n５) General review(ます, て, ない and Dictionary forms)")
                print("\n\tYou'll be given the English meaning of the verb and you need to enter a)its ます -form, b) the group it is part of, c) its て -form, d) its ない -form and e) its Dictionary form.")
                review_choice = input("\nEnter １、２、３、４　or ５: ")

            # ます -form review
            if(review_choice == "１"):

                loop = "0"
                while(int(loop) < 1 or int(loop) > int(total_verbs)):

                    os.system('cls')
                    print("How many verbs would you like to review? (tot. verbs: " + total_verbs + ")")
                    loop = input("\nAnswer: ")

                os.system('cls')

                print("Rules:\n\n1) You get 1 point for each correct answer.\n2) All questions are randomized.")
                print("3) If there is a word in brackets next to the verb (e.g., 「tell [an address]」) you MUST type the word, the particle and the verb!")
                print("4) Although this quiz helps you review verbs, please practice writing them on paper as well when you have time!")

                stop = input("\nPress ENTER once you are ready...")
                os.system('cls')

                print("###################################### QUIZ STARTS! ######################################\n")

                while i<int(loop):

                    while True:
                        num = random.randint(0,len(question)-1)
                        if(question[num][0] not in used_verbs):
                            break

                    used_verbs.append(question[num][0])


                    print("\nQ" + str(i+1) + ")\tWhat is the ます -form of 「", question[num][0], "」?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][1])):
                        print("\n\t\t\tCongratulations! That's right!\n")
                        score += 1
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][1] + "\n")

                    i += 1

            # て -form review
            elif(review_choice == "２"):

                loop = 0
                while(int(loop) < 1 or int(loop) > int(total_verbs)):

                    os.system('cls')
                    print("How many verbs would you like to review? (tot. verbs: " + total_verbs + ")")
                    loop = input("\nAnswer: ")

                os.system('cls')

                print("Rules:\n\n1) Each question has 2 parts: the group the verb is part of and its て -form.\n2) You get 0.50 points for each correctly answered part (up to 1 point for each question).\n3) All questions are randomized.")
                print("4) If there is a word in brackets next to the verb (e.g., 「tell [an address]」) you DO NOT NEED to type the word and the particle. Just type the verb using the requested form!")
                print("5) Although this quiz helps you review verbs, please practice writing them on paper as well when you have time!")

                stop = input("\nPress ENTER once you are ready...")
                os.system('cls')

                print("###################################### QUIZ STARTS! ######################################\n")

                while i<int(loop):

                    while True:
                        num = random.randint(0,len(question)-1)
                        if(question[num][0] not in used_verbs):
                            break

                    used_verbs.append(question[num][0])

                    answer1_right = False
                    answer2_right = False

                    print("\nQ" + str(i+1) + ")\ta) Which group (１、２、３) is 「", question[num][0], "」 part of?")
                    answer = input("\n\t\tAnswer: ")

                    if (answer == str(question[num][2])):
                        print("\n\t\t\tCongratulations! That's right!")
                        answer1_right =True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][2])

                    print("\n\tb) What is its て -form?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][3])):
                        print("\n\t\t\tCongratulations! That's right!\n")
                        answer2_right = True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][3] + "\n")

                    if(answer1_right):
                        score += 0.5
                    if(answer2_right):
                        score += 0.5

                    i += 1
            # ない -form review
            elif(review_choice == "３"):

                loop = 0
                while(int(loop) < 1 or int(loop) > int(total_verbs)):

                    os.system('cls')
                    print("How many verbs would you like to review? (tot. verbs: " + total_verbs + ")")
                    loop = input("\nAnswer: ")

                os.system('cls')

                print("Rules:\n\n1) Each question has 2 parts: the group the verb is part of and its ない -form.\n2) You get 0.50 points for each correctly answered part (up to 1 point for each question).\n3) All questions are randomized.")
                print("4) If there is a word in brackets next to the verb (e.g., 「tell [an address]」) you DO NOT NEED to type the word and the particle. Just type the verb using the requested form!")
                print("5) Although this quiz helps you review verbs, please practice writing them on paper as well when you have time!")

                stop = input("\nPress ENTER once you are ready...")
                os.system('cls')

                print("###################################### QUIZ STARTS! ######################################\n")

                while i<int(loop):

                    while True:
                        num = random.randint(0,len(question)-1)
                        if(question[num][0] not in used_verbs):
                            break

                    used_verbs.append(question[num][0])

                    answer1_right = False
                    answer2_right = False

                    print("\nQ" + str(i+1) + ")\ta) Which group (１、２、３) is 「", question[num][0], "」 part of?")
                    answer = input("\n\t\tAnswer: ")

                    if (answer == str(question[num][2])):
                        print("\n\t\t\tCongratulations! That's right!")
                        answer1_right =True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][2])

                    print("\n\tb) What is its ない -form?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][4])):
                        print("\n\t\t\tCongratulations! That's right!\n")
                        answer2_right = True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][4] + "\n")

                    if(answer1_right):
                        score += 0.5
                    if(answer2_right):
                        score += 0.5

                    i += 1
            # Dictionary review
            elif(review_choice == "４"):

                loop = 0
                while(int(loop) < 1 or int(loop) > int(total_verbs)):

                    os.system('cls')
                    print("How many verbs would you like to review? (tot. verbs: " + total_verbs + ")")
                    loop = input("\nAnswer: ")

                os.system('cls')

                print("Rules:\n\n1) Each question has 2 parts: the group the verb is part of and its Dictionary form.\n2) You get 0.50 points for each correctly answered part (up to 1 point for each question).\n3) All questions are randomized.")
                print("4) If there is a word in brackets next to the verb (e.g., 「tell [an address]」) you DO NOT NEED to type the word and the particle. Just type the verb using the requested form!")
                print("5) Although this quiz helps you review verbs, please practice writing them on paper as well when you have time!")

                stop = input("\nPress ENTER once you are ready...")
                os.system('cls')

                print("###################################### QUIZ STARTS! ######################################\n")

                while i<int(loop):

                    while True:
                        num = random.randint(0,len(question)-1)
                        if(question[num][0] not in used_verbs):
                            break

                    used_verbs.append(question[num][0])

                    answer1_right = False
                    answer2_right = False

                    print("\nQ" + str(i+1) + ")\ta) Which group (１、２、３) is 「", question[num][0], "」 part of?")
                    answer = input("\n\t\tAnswer: ")

                    if (answer == str(question[num][2])):
                        print("\n\t\t\tCongratulations! That's right!")
                        answer1_right =True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][2])

                    print("\n\tb) What is its Dictionary form?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][5])):
                        print("\n\t\t\tCongratulations! That's right!\n")
                        answer2_right = True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][5] + "\n")

                    if(answer1_right):
                        score += 0.5
                    if(answer2_right):
                        score += 0.5

                    i += 1
            # General review
            elif(review_choice == "５"):

                loop = 0
                while(int(loop) < 1 or int(loop) > int(total_verbs)):

                    os.system('cls')
                    print("How many verbs would you like to review? (tot. verbs: " + total_verbs + ")")
                    loop = input("\nAnswer: ")

                os.system('cls')

                print("Rules:\n\n1) Each question has 5 parts: the verb's ます -form, the group it is part of, its て -form, its ない -form and its Dictionary form. \n2) You get 0.20 points for each correctly answered part (up to 1 point for each question).\n3) All questions are randomized.")
                print("4) If there is a word in brackets next to the verb (e.g., 「tell [an address]」) you MUST type the word, the particle and the verb ONLY if the question is regarding the verb's ます -form.")
                print("5) For the verb's て, ない and Dictionary forms you just need to type the verb using the requested form!")
                print("6) Although this quiz helps you review verbs, please practice writing them on paper as well when you have time!")

                stop = input("\nPress ENTER once you are ready...")
                os.system('cls')


                print("###################################### QUIZ STARTS! ######################################\n")

                while i<int(loop):

                    while True:
                        num = random.randint(0,len(question)-1)
                        if(question[num][0] not in used_verbs):
                            break

                    used_verbs.append(question[num][0])

                    answer1_right = False
                    answer2_right = False
                    answer3_right = False
                    answer4_right = False
                    answer5_right = False

                    # Asking ます -form
                    print("\nQ" + str(i+1) + ")\ta) What is the ます -form of 「", question[num][0], "」?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][1])):
                        print("\n\t\t\tCongratulations! That's right!")
                        answer1_right = True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][1])

                    # Asking group
                    print("\n\tb) Which group (１、２、３) is it part of?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][2])):
                        print("\n\t\t\tCongratulations! That's right!")
                        answer2_right =True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][2])

                    # Asking て -form
                    print("\n\tc) What is its て -form?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][3])):
                        print("\n\t\t\tCongratulations! That's right!")
                        answer3_right = True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][3])

                    # Asking ない -form
                    print("\n\td) What is its ない -form?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][4])):
                        print("\n\t\t\tCongratulations! That's right!\n")
                        answer4_right = True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][4] + "\n")

                    # Asking Dictionary form
                    print("\n\te) What is its Dictionary form?")
                    answer = input("\n\t\tAnswer: ")
                    if (answer == str(question[num][5])):
                        print("\n\t\t\tCongratulations! That's right!\n")
                        answer5_right = True
                    else:
                        print("\n\t\t\tWrong! The correct answer was : ", question[num][5] + "\n")

                    if(answer1_right):
                        score += 0.20
                    if(answer2_right):
                        score += 0.20
                    if(answer3_right):
                        score += 0.20
                    if(answer4_right):
                        score += 0.20
                    if(answer5_right):
                        score += 0.20

                    i += 1

        f.close()

        if score>1:
            sc_pl = "points"
        else:
            sc_pl = "point"

        print("\n##########################################################################################")

        print("\n\nRESULTS:\n\n ", i, "questions, ", score, sc_pl, " \n--> Your score is: ", '{:.2f}'.format((score*100/i)), "%!\n")

        print("\n##########################################################################################")

        print("\n\nPress ENTER  to proceed...")
        input()

        main()
    elif(what_to_review == "３"):
        os._exit(0)

while True:
    main()
