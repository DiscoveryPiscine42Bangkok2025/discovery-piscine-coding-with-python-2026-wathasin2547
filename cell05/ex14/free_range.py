#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) != 3:
        print("none")
    else:
        start_num = int(sys.argv[1])
        end_num = int(sys.argv[2])

        result_array = list(range(start_num, end_num + 1))

        print(result_array)

if __name__ == "__main__":
    main()