from checkmate import checkmate

def main():
    board1 = """\
R...
.K..
..P.
....\
"""
    print("Testing 1: ")
    checkmate(board1)

    board2 = """\
..
.K\
""" 
    print("\nTesting 2: ")
    checkmate(board2) 

    board3 = """\
R.P.K
.....\
"""
    print("\nTesting 3 (Blocked):")
    checkmate(board3)

main()