import random

target = random.randint(1,100)

while True:
    userchoice = int(input("Guess the target between 1-100: "))
    if(userchoice == target):
        print("You guessed correctly !!")
        break
    if(userchoice < target):
        print("Your no. is small , take a bigger guess")
        
    if(userchoice > target):
        print("Your no. is big, take a smaller guess")
    
    
print("Game Over !!")