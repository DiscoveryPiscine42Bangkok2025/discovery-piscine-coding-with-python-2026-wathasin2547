#!/usr/bin/env python3
def checkmate(board):
    rows = board.strip().split('\n')
    if not rows:
        print("Fail")
        return
    grid = [list(r) for r in rows]
    height = len(grid)
    width = len(grid[0]) if height > 0 else 0

    k_r, k_c = -1, -1
    for r in range(height):
        for c in range(width):
            if grid[r][c] == 'K':
                k_r, k_c = r, c
                break

    if k_r == -1:
        print("Fail")
        return

    def is_path_clear(start_r, start_c, end_r, end_c):
        dr = end_r - start_r
        dc = end_c - start_c

        step_r = 0 if dr == 0 else (1 if dr > 0 else -1)
        step_c = 0 if dc == 0 else (1 if dc > 0 else -1)
        
        curr_r, curr_c = start_r + step_r, start_c + step_c

        while (curr_r != end_r) or (curr_c != end_c):
            if grid[curr_r][curr_c] != '.':
                return False
            curr_r += step_r
            curr_c += step_c
        return True


    for r in range(height):
        for c in range(width):
            piece = grid[r][c]
            if piece == '.' or piece == 'K':
                continue

            if piece == 'P':
                if r - 1 == k_r and (c - 1 == k_c or c + 1 == k_c):
                    print("Success")
                    return

            elif piece == 'R':

                if r == k_r or c == k_c:
                    if is_path_clear(r, c, k_r, k_c):
                        print("Success")
                        return

            elif piece == 'B':

                if abs(r - k_r) == abs(c - k_c):
                    if is_path_clear(r, c, k_r, k_c):
                        print("Success")
                        return

            elif piece == 'Q':
                is_rook_move = (r == k_r or c == k_c)
                is_bishop_move = (abs(r - k_r) == abs(c - k_c))
                
                if is_rook_move or is_bishop_move:
                    if is_path_clear(r, c, k_r, k_c):
                        print("Success")
                        return

    print("Fail")