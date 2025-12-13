import random as j
print("This is a number guessing game.\nThe User have 3 lives.\nTo end game, Type 0, Type 1 to play")
print()
lives = 3
while (lives >= 0):
    data = int(input())
    print()
    if data == 0:
        break
    elif data > 1 or data < 0:
        print ("I don't understand your answer")
        print()
    elif data == 1:
        while True:
            if lives > 0:
                cn = j.randrange(0, 11)
                un = int(input("Enter any number from 0 to 10\n"))
                print()
                if cn == un:
                    print(f"Success!\nComputer Number - {cn}\nUser Guess - {un}")
                    lives += 1
                    print("Congrats! A live has been added to your lives for guessing right.\nTotal available lives - ", lives)
                    print()
                else:
                    lives = lives - 1
                    print(f"Failure!\nComputer Number - {cn}\nUser Guess - {un}")
                    print("You Have loss a life! Remaining - ", lives)
                    print()
            else:
                print("-"*10)
                print("GAME OVER")
                print("-"*10)
                break
