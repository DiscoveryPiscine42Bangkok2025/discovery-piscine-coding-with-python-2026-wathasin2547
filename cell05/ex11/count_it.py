"""ex11_count_it.py"""
#!/usr/bin/env python3
import sys
def main():
    if len(sys.argv) < 2:
        print("none")
    else:
        total_params = len(sys.argv) - 1
        print("parameters: " + str(total_params))
        for param in sys.argv[1:]:
            length = len(param)
            print(param + ": " + str(length))
main()