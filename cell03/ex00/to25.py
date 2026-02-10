#!/usr/bin/env python3
def main():
    print("Enter a number less than 25")
    user_input = input()
    n = int(user_input)

    if n > 25:
        print("Error")
    else:
        while n <= 25:
            print("Inside the loop, my variable is " + str(n))
            n += 1
main()