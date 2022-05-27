#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: May 2022
# This program will use a function to print out the
#   the percentages of school marks


def mark_calculation():
    # this function will calculate the percentages

    school_mark = input("Enter in your school mark (ex: 3+): ")
    # school mark calculation

    if school_mark == "4+":
        return "97%"
    elif school_mark == "4":
        return "90%"
    elif school_mark == "4-":
        return "83%"
    elif school_mark == "3+":
        return "78%"
    elif school_mark == "3":
        return "75%"
    elif school_mark == "3-":
        return "70%"
    elif school_mark == "2+":
        return "68%"
    elif school_mark == "2":
        return "65%"
    elif school_mark == "2-":
        return "62%"
    elif school_mark == "1+":
        return "58%"
    elif school_mark == "1":
        return "55%"
    elif school_mark == "1-":
        return "50%"
    elif school_mark == "R":
        return "30%"
    else:
        return "-1"


def main():
    # This will call the other function

    print(mark_calculation())


if __name__ == "__main__":
    main()
