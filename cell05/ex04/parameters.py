#!/usr/bin/env python3
import sys
def main():
    total_args = len(sys.argv)
    number_of_params = total_args - 1
    print("Number of parameters: " + str(number_of_params) + ".")
main()