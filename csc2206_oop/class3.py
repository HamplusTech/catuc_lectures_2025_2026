# this program finds the maximum of two numbers

def max_2_numbers():
    first_number = input("Please enter the first number\n")
    second_number = input("Please enter the second number\n")

    if first_number > second_number:
        print ("The maximum is ", first_number)
    else:
        print("The maximum is ", second_number)

def number_check():
    user_num = input("Please enter any number < 11\n")
    user_num = int(user_num)

    if user_num > 5 and user_num < 11:
        print("The number is greater than 5 ")
    elif user_num > 0 and user_num < 11:
        print("The number is greater than 0")
    else:
        print("The number is either less than 0 or greater than 10")

def colour_check():
    print("Please enter any three colours - RED, GREEN OR BLUE")
    colour = input()

    if colour.upper() == "RED":
        print("You type RED colour")

    elif colour.upper() == "BLUE":
        print("You type BLUE colour")
    elif colour.upper() == "GREEN":
        print("You type GREEN colour")

    else:
        print("You typed a different colour")
