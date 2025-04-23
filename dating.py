#!/usr/bin/env python3
# Created by: Viviana Hurtado
# Date: April, 2025
# This program approve of you dating their grandchild if
# you are older than 25 AND younger than 40. Write a program
# where the user enters their age and then the program tells
#  you if you can date their grandchild.

def main():
    user_age_str = input("Enter your age: ")


    try:
        user_age = int(user_age_str)
        if user_age >= 25 and user_age <= 40:
            print("You can date")
        else:
            print("You can't date")
    except:
        print(user_age_str, "is not an integer")




if __name__ == "__main__":
    main()
