__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-03"
__email__ = "qaiserabbas889@yahoo.com"

response = ["Hi, How may I help you?", "I hope you enjoy this conversation. \nGood bye take care.",
            "RAM is Random-access memory is a form of computer memory that can be read and changed in any order, typically used to store working data and machine code.", 
            "Sorry, I didn't get you!", 
            "Computer is an Electronic machine that accept data as input and provide output by processing that data.",
            "You can google it to find more."]

print("Hi I am a Computer Specialist Ask me anything.")
while True:
    quest1 = input("YOU : ")

    if ("hi" in quest1 or "hello" in quest1):
        print("BOT : " + response[0])

    elif ("bye" in quest1 or "exit" in quest1):
        print("BOT : "+response[1])
        break

    elif ("what" in quest1 and "ram" in quest1 or "RAM" in quest1):
        print("BOT : "+response[2])

    elif ("what" in quest1 and "COMPUTER" in quest1 or "computer" in quest1):
        print("BOT : "+response[4])

    elif ("why" in quest1 or "keyborad" in quest1 or "ROM" in quest1 or "hardisk" in quest1):
        print("BOT : "+response[5])

    else:
        print("Sorry, I didn't get you!")