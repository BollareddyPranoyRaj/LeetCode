class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [["."] * n for i in range(n)]
        ans = []

        def is_safe(res, r, c):
            i = r
            while i > -1:
                if res[i][c] == 'Q':
                    return False
                i -= 1

            i, j = r, c
            while i > -1 and j < n:
                if res[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            i, j = r, c
            while i > -1 and j > -1:
                if res[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            return True

        def bt(row):
            if row == n:
                ans.append(["".join(r) for r in res])
                return

            for col in range(n):
                if is_safe(res, row, col):
                    res[row][col] = 'Q'
                    bt(row + 1)
                    res[row][col] = '.'

        bt(0)
        return ans