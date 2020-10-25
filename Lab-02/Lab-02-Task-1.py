__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-02"
__email__ = "qaiserabbas889@yahoo.com"

q=int(input("Enter the number of stars in central line\n"))

for i in range(1,(q+1)):
 print(" "*(q-i),"* "*i)