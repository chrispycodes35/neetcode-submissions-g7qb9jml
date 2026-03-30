
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def dfs(r, c, i):
            # i = index in word we are trying to match
            if i == len(word):
                return True

            # out of bounds, wrong letter, or already used in this path
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                board[r][c] != word[i]
            ):
                return False

            # mark cell as used for this path
            temp = board[r][c]
            board[r][c] = "#"

            # try all 4 directions
            found = (
                dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1)
            )

            # restore cell for other paths
            board[r][c] = temp

            return found

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True

        return False