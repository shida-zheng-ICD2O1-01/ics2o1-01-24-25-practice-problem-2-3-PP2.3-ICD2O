'''

    Lesson: Else If
    Author: Mr. Kalisz
    Date Created: Oct 16, 2024
    Date Last Modified: Oct 16, 2024

'''

# If

num = 15

if num < 20:
    print("run if statment")

# Else

num = 15

if num < 20:
    print("run if statment")
else: #if statement is false
    print("run the else statement")

# Else If

#only 1 will run.
if num < 50:
    print("run if statment")
elif num < 30: #not(num < 20) and num < 30
    #num >= 20 and num < 30
    print("first elif")
elif num < 40: #not(num < 20) and not(num < 30) and num < 40
    #num >= 20 and num >= 30 and num < 40
    #num >= 30 and num < 40
    print("second elif")
else: #all if and elif statements are false -> num >= 40
    print("run the else statement")

#Creates an unreachable elif statement
if num < 50: #Includes all values from < 20 as well as 20-49
    print()
elif num < 20: #all numbers less than 20 are less than 50
    print()
elif num == 25:
    print()

#fix it
if num == 25: #Includes all values from < 20 as well as 20-49
    print()
elif num < 20:
    print()
elif num < 50:
    print()

#Most specific to least specific
#smallest range, to the largest range