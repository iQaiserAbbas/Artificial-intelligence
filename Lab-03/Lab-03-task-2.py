__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-03"
__email__ = "qaiserabbas889@yahoo.com"


response = ["Hi, Welcome!",
            "Please Introduce Yourself and tell me for what job are you applying for?", 
            "I hope you enjoy this conversation. \nGood bye take care.", 
            "what is web development?",
            "what is software development?",
            "what are your weeknesses?",
            "Why I hire you for this post?"]

print("Hi I am your Mentor for practicing Inteview Question.")

while True:
    quest2 = input("YOU : ")

    if ("hi" in quest2 or "hello" in quest2):
        print("BOT : " + response[0] + " \n" +response[1])

    elif ("bye" in quest2 or "exit" in quest2):
        print("BOT : "+response[2])
        break

    elif ("web develop" in quest2):
        print("BOT : "+response[3])  

    elif ("software" in quest2):
        print("BOT : "+response[4]) 

    elif ("development" in quest2):
        print("BOT : "+response[5])

    elif ("perfect" in quest2 or "motivated" in quest2 or "hardworking" in quest2 or "work hard" in quest2):
        print("BOT : "+response[6])
    
    else:
        print("Great, So what else you know about the post.")