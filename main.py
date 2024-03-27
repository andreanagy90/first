import my_module


def check(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            num = int(user_input)
            if 1 <= num <= 8:
                return num
            else:
                print("Try again")
        else:
            print("Error, please enter Valid Number to 1 - 8")


def software():
    run = True
    while run:
        start = check("Please select a number between 1-8 :\n"
                  "1. Calculator:\n"
                  "2. Lotto :\n"
                  "3. Create Shop list:\n"
                  "4. Game:\n"
                  "5. Area calculator:\n"
                  "6. Vowel detector:\n"
                  "7. Registration:\n"
                  "8. >>>Exit<<<:\n")
        if start == 1:
            my_module.calculator()
        elif start == 2:
            my_module.lotto()
        elif start == 3:
            my_module.shopping()
        elif start == 4:
            my_module.game()
        elif start == 5:
            my_module.area()
        elif start == 6:
            my_module.vowels_detector()
        elif start == 7:
            my_module.registration()
        elif start == 8:
            print("Thank you. See you later!")
            break
        else:
            print( start)


software()