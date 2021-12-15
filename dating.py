#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Dec 15, 2021
# This program is made for gold diggers.
# It asks the user if they are rich or good looking.
# It then tells them if they can date some guy's
# grandchild.


def main():
    # set variables
    age_string = input("Enter your age: ")
    print("")

    # error checking
    try:
        age = int(age_string)
    except Exception:
        print("Invalid input.")
        quit()

    # display results
    if age > 25 and age < 40:
        print("You may date.")
    else:
        print("You may not date.")


if __name__ == "__main__":
    main()
