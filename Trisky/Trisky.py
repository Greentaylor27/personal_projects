#!/usr/bin/python3
import random

def Trisky():

    Question_1 = {
        "Option_1" : "Is your Commander colour identity mono-coloured?",
        "Option_2" : "Is your Commander colour identity multi-coloured?",
        "Option_3" : "Is your Commander colour identity colourless?"
    }
    
    Question_2a = {
        "Option_1" : "Is your Commander White?",
        "Option_2" : "Is your Commander Blue?",
        "Option_3" : "Is your Commander Black?",
        "Option_4" : "Is your Commander Red?",
        "Option_5" : "Is your Commander Green?"
    }

    Random_question = random.choice(list(Question_1.values()))
    Answer_1 = input(Random_question + ": ")
    if Answer_1.lower() not in ["yes", "no", "n", "y"]:
        print("Invalid answer")

if __name__ == '__main__':
    Trisky();
