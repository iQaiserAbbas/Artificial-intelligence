__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-02"
__email__ = "qaiserabbas889@yahoo.com"

def samsung(value):
    x = 1
    while x <= value:
        if x % 3 == 0 and x % 5 == 0:
            print("SAMSUNG")
        elif x % 3 == 0:
            print("SAM")
        elif x % 5 == 0:
            print("SUNG")
        else:
            print(x)
        x += 1
    
samsung(100)