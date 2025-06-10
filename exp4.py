class Solution:
    def solve(self, board):
        start = tuple(sum(board, []))
        if start == (0,1,2,3,4,5,6,7,8): return 0
        visited = {start: 0}
        goal = (0,1,2,3,4,5,6,7,8)
        q = [start]
        moves = {
            0:[1,3], 1:[0,2,4], 2:[1,5], 3:[0,4,6], 4:[1,3,5,7],
            5:[2,4,8], 6:[3,7], 7:[4,6,8], 8:[5,7]
        }

        while q:
            curr = q.pop(0)
            zero = curr.index(0)
            for m in moves[zero]:
                nxt = list(curr)
                nxt[zero], nxt[m] = nxt[m], nxt[zero]
                nxt = tuple(nxt)
                if nxt not in visited:
                    visited[nxt] = visited[curr] + 1
                    if nxt == goal: return visited[nxt]
                    q.append(nxt)
        return -1

# Example usage
ob = Solution()
matrix = [[3, 1, 2], [4, 7, 5], [6, 8, 0]]
print(ob.solve(matrix))
