#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) < 3:
        print("none")
    else:
        all_params = sys.argv[1:]
        for param in reversed(all_params):
            print(param)
main()