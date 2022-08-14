# import random
# x = True
# print("--------------Welcome to the Dice Rolling Simulator--------------")
# while x:
#     print(random.randint(1,6))
#     roll = input("Do you want to continue(y/n)")
#     if roll.lower() == 'y':
#         continue
#     else:
#         break


import random
print("--------------Welcome to the Dice Rolling Simulator--------------")
a = "y"
while(a=="y"):
    # Random numbers to be generated between the inclusive range of 1 and 6
    n = random.randint(1,6)
    
    if(n==1):
        print("-----------")
        print("|         |")
        print("|    0    |")
        print("|         |")
        print("-----------") 
    elif(n==2):
        print("-----------")
        print("|         |")
        print("|  0   0  |")
        print("|         |")
        print("-----------")   
    elif(n==3):
        print("-----------")
        print("|  0      |")
        print("|    0    |")
        print("|      0  |")
        print("-----------")  
    elif(n==4):
        print("-----------")
        print("|  0   0  |")
        print("|         |")
        print("|  0   0  |")
        print("-----------")   
    elif(n==5):
        print("-----------")
        print("|  0   0  |")
        print("|    0    |")
        print("|  0   0  |")
        print("-----------")      
    elif(n==6):
        print("-----------")
        print("|  0   0  |")
        print("|  0   0  |")
        print("|  0   0  |")
        print("-----------") 
              
    a = input("Do you want to continue? y/n : ")