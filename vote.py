#!/usr/bin/env python3

# Created by: Liam Hearty
# Created on: October 2019
# This program tells you if you are eligible to vote.


def main():
    print("This program tells you if you are eligible to vote.")
    age = input("Enter your age: ")
    try:
        age = int(age)
        if age < 18:
            print("You are not eligible to vote.")
        elif int(age) >= 18:
            print("You are eligible to vote.")
    except ValueError:
        print("Please input a whole number.")


if __name__ == "__main__":
    main()
