#!/usr/bin/env python3

# Created by: Rohnin Barrette
# Created on: Sep 2021
# This program shows the user all of the numbers squared
# leading up to and including the inputted number


def main():
    # This program shows the user all of the numbers squared
    # leading up to and including the inputted number

    # this is to keep track of how many times you go through the loop
    counter = 0
    answer = 0

    # input
    user_string = input("please enter a positive integer: ")

    # process and output
    try:
        user_input = int(user_string)
        if user_input >= 0:
            for counter in range(11):
                answer = counter * user_input
                print("{0} x {1} = {2}".format(user_input, counter, answer))
        else:
            print("please enter a positive number.")
    except:
        print("invalid input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
