class Solution:
    def solve(self, board):
        state_dict = {}
        flatten = []

        # Flatten the board into a tuple
        for row in board:
            flatten += row
        flatten = tuple(flatten)

        state_dict[flatten] = 0

        # Check if already in solved state
        if flatten == (0, 1, 2, 3, 4, 5, 6, 7, 8):
            return 0

        return self.get_paths(state_dict)

    def get_paths(self, state_dict):
        cnt = 0
        while True:
            current_nodes = [node for node in state_dict if state_dict[node] == cnt]
            if not current_nodes:
                return -1  # No solution found

            for node in current_nodes:
                next_moves = self.find_next(node)
                for move in next_moves:
                    if move not in state_dict:
                        state_dict[move] = cnt + 1
                        if move == (0, 1, 2, 3, 4, 5, 6, 7, 8):  # Goal state
                            return cnt + 1

            cnt += 1

    def find_next(self, node):
        moves = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
            6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
        }

        results = []
        pos_0 = node.index(0)  # Find position of zero (empty space)

        for move in moves[pos_0]:
            new_node = list(node)
            new_node[move], new_node[pos_0] = new_node[pos_0], new_node[move]
            results.append(tuple(new_node))

        return results


# Example usage
ob = Solution()
matrix = [
    [3, 1, 2],
    [4, 7, 5],
    [6, 8, 0]]

print(ob.solve(matrix))