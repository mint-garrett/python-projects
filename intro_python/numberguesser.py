#numberguesser

import random
import time


#"loading screen"
print("the number is between 0 and 100.")
print("picking a number....")
time.sleep(2)
print("start guessing")

### asks for your first guess
guess = int(input("guessed number is: "))
## sets a correct value between 0-100
correct = random.randint(0,100)
guess_count = 0

##while loop to keep guessing going
while guess != correct:
    guess_count += 1
    if guess < correct:
        guess = int(input("you aren't right. guess higher: "))
    else:
        guess= int(input("you aren't right. guess lower: "))


print(f"correct guess of {correct}. you used {guess_count} guesses")
