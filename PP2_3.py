
def q1(): 
  #Write Assignment code here
word = input("In: ")
if word.endswith("ife"):
    print("-ives")
elif word.endswith("ey"):
    print("-eys")
elif word.endswith("y"):
    print("-ies")
else:
    print("-s")

def q2(): 
  #Write Assignment code here
num = int(input("In: "))

if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")


#Do not alter the following code
#Comment out the following code when running your tests

q1()
q2()
