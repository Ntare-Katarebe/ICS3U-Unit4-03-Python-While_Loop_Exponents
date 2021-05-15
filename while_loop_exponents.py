#!/usr/bin/env python3

# Created by: Ntare Katarebe
# Created on: May 2021
# This program adds up positive integers
#    with numbers inputted from the user

def main():
    # this function adds up positive numbers

    # input
    positive_string = input("Enter an integer >= 0: ")

    # process

    # output
    try:
        positive_integer = int(positive_string)
        if positive_integer == 0:
            print("{}² = 0".format(positive_integer))
        elif positive_integer < 0:
            print("You did not enter a positive integer")
        else:
            for loop_counter in range(positive_integer + 1):
                print("{}² = {}".format(loop_counter, loop_counter ** 2))
    except Exception:
        print("{} is not an number".format(positive_string))
    finally:
        print("")


if __name__ == "__main__":
    main()
