# Owned
__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence Assignment-01"
__email__ = "qaiserabbas889@yahoo.com"
#===============================================================
# {code}
response = ["Hi, This is Food ChatBot by Qaiser!",
            "Yes Sir, I am here to assist you for any problem",
            "sure Sir! Ask us anything about Food Ordering",
            "We provide Snacks, Fast food, Burgers and Pizzas with Fresh Salad and Apitizers",
            "It's sound good. Here is Menu--> 1) Zinger Roll 2) French Fries 3) Fish 4) Burger",
            "Anything else ?",
            "What ?",
            "Done, anything else ?",
            "Yes, we do",
            "Anything more ?", ]

print("***********************************************")
print("***Welcome to Food ChatBot from Qaiser Abbas***")
print("***********************************************")

while True:
    quest2 = input("Client: ")

    if ("Hi" in quest2):
        print("BOT : " + response[0])

    elif ("Can you assist me?" in quest2):
        print("BOT : "+response[1])

    elif ("i want to place order" in quest2):
        print("BOT : "+response[2])

    elif ("what do you provide" in quest2):
        print("BOT : "+response[3])

    elif ("i would like to have fast food" in quest2):
        print("BOT : "+response[4])

    elif ("i would like to have Fish" in quest2):
        print("BOT : "+response[5])

    elif ("Yes" in quest2):
        print("BOT : "+response[6])
        

    elif ("1 soft drink" in quest2):
        print("BOT : "+response[7])

    elif ("do you provide desserts?" in quest2):
        print("BOT : "+response[8])

    elif ("and 1 Pies" in quest2):
        print("BOT : "+response[9])

    elif ("no thank you" in quest2):
        print("BOT : "+response[10])

    else:
        print("The price is Rs 399 only/")
