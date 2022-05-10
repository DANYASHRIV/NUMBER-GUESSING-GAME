import random
no=random.randint(1,9)
print ("number guessing")
score=0
print("choose any number from 1 to 9")
while score < 5:
    number = int(input("enter you guess number:- "))
    if number == no:
        print("CONGRATULATION YOU WON !!")
        break
    elif number < no:
        print("Your guess was too low: Guess a number higher than", number)
    else:
        print("Your guess was too high: Guess a number lower than", number)
    score = score + 1

if not score<5:
    print("YOU LOSE!!! The number is", no)
