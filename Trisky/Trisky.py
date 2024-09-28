#!/usr/bin/python3
import random

def Trisky():

    Question_1 = {
        "Option_1" : "Is your Commander mono-coloured?",
        "Option_2" : "Is your Commander multi-coloured?"
    }

    Random_question = random.choice(list(Question_1.values()))
    Answer_1 = input(Random_question + ": ")
    if Answer_1.lower() not in ["yes", "no", "n", "y"]:
        print("Invalid answer")

if __name__ == '__main__':
    Trisky();
