#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 3:
        print("none")
        return
    keyword = sys.argv[1]
    search_string = sys.argv[2]

    count = search_string.count(keyword)
    if count == 0:
        print("none")
    else:
        print(count)
main()