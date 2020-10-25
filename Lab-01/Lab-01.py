__author__ = "Qaiser Abbas"
__copyright__ = "Copyright 2020, Artificial Intelligence lab-01"
__email__ = "qaiserabbas889@yahoo.com"

# Python Program - Calculate Grade of Student

print("Please enter 'x' for exit.");
print("Enter marks obtained in 5 subjects: ");
subject1 = input();
if subject1 == 'x':
    exit();
else:
    subject1 = int(subject1);
    subject2 = int(input());
    subject3 = int(input());
    subject4 = int(input());
    subject5 = int(input());
    sum = subject1 + subject2 + subject3 + subject4 + subject5;
    average = sum/5;
    if(average>=85 and average<=100):
    	print("Your Grade is A+");
    elif(average>=80 and average<85):
    	print("Your Grade is A-");
    elif(average>=75 and average<80):
    	print("Your Grade is B+");
    elif(average>=71 and average<75):
    	print("Your Grade is B-");
    elif(average>=51 and average<=60):
    	print("Your Grade is C+");
    else:
    	print("Your Grade is F");