from collections import defaultdict


def isValid(board):
    rows = [0] * 9
    cols = [0] * 9
    sqrs = [0] * 9

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            val = int(board[row][col]) - 1
            if (1 << val) & rows[row]:
                return False
            if (1 << val) & cols[col]:
                return False
            if (1 << val) & sqrs[(row // 3) * 3 + (col // 3)]:
                return False

            rows[row] |= 1 << val
            cols[col] |= 1 << val
            sqrs[(row // 3) * 3 + (col // 3)] |= 1 << val
    print(rows)
    print(cols)
    print(sqrs)

    return True


board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"],
]

print(isValid(board))
# tracker = 0
# tracker |= 1 << ord("A")
# tracker |= 1 << 2
# tracker |= 1 << 6
# print(tracker)
# isValid(board)

# def isValid(board):
#     rows = defaultdict(set)
#     cols = defaultdict(set)
#     sqr = defaultdict(set)
#
#     for row in range(9):
#         for col in range(9):
#             if board[row][col] == ".":
#                 continue
#             if (
#                 board[row][col] in rows[row]
#                 or board[row][col] in cols[col]
#                 or board[row][col] in sqr[(row // 3, col // 3)]
#             ):
#                 return False
#             cols[col].add(board[row][col])
#             rows[row].add(board[row][col])
#             sqr[(row // 3, col // 3)].add(board[row][col])
#
#     return True
