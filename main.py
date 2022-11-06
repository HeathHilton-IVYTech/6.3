# Heath Hilton
# 11/06/2022

# Program: 6.3 - Guess my number in range

# The program is going to slowly guess a number
guess_me = 5

for number in range(10):
    if number < guess_me:
        print("Too Low")
    elif number == guess_me:
        print("Found it!")
    elif number > guess_me:
        print("Oops")
exit()
