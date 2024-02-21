import random
original = random.randint(100,1000)
print(original)
print("Welcome , you have 10 tries to guess the number.Good luck!")
for i in range(10):
    guess = int(input("Please make a guess:"))
    if guess==original:
        print("Congrats!You've guessed the number!")
        break
    elif guess < original :
        print("your guess is less than the number.")
    else:
         print("Your guess is greater than the number.")

    print("You have", 10-(i+1),"tries left.")

if (10-(i+1))==0:
    print("The correct number was:",original)
