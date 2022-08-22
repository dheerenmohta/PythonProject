import collections
from typing import List


class Solution:
    @staticmethod
    def sudoku_solver(board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(len(board) - 1):
            for c in range(len(board[0]) - 1):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows) or (board[r][c] in cols) or (board[r][c] in squares[(r // 3, c // 3)]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True


if __name__ == '__main__':
    print(Solution.sudoku_solver([["1", "2", " 3"],
                                  ["4", "5", "6"],
                                  ["7", "8", "9"]]))
