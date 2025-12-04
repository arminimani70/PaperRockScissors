import sys
import random
your_input = input("please enter your choice :\n1. paper\n2. rock\n3. scissors\n") 
if your_input.isdigit(): 
    your_choice = int(your_input) 
    if (your_choice < 0 or your_choice > 3):
        print("you must enter a valid number between 1 and 3") 
        sys.exit() 
    computer_value = random.choice("123") 
    computer_choice = int(computer_value) 

    print("your choice is " + your_input + " and computer choice is " + computer_value)
else:
    print("you must enter a valid number between 1 and 3")

if your_choice == 1 and computer_choice == 3:
    print("you win!")
elif your_choice == 2 and computer_choice == 1:
    print("you win!")       
elif your_choice == 3 and computer_choice == 2:
    print("you win!")
elif your_choice == computer_choice:
    print("it's a tie!")
else:
    print("computer wins!")
