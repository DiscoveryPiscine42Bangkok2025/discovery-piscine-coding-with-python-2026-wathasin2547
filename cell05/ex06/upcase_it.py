#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) == 2:
        txt = sys.argv[1]
        print(txt.upper())
    else:
        print("none")
main()