from collections import deque

# Goal state
goal = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


def solve_puzzle(start):
    queue = deque()
    queue.append((start, []))

    visited = set()
    visited.add(start)

    while queue:
        current, path = queue.popleft()

        # Check whether goal is reached
        if current == goal:
            return path + [current]

        # Find blank position
        blank = current.index(0)

        row = blank // 3
        col = blank % 3

        # Possible movements: Up, Down, Left, Right
        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < 3 and 0 <= new_col < 3:

                new_blank = new_row * 3 + new_col

                new_state = list(current)

                # Swap blank with adjacent number
                new_state[blank], new_state[new_blank] = \
                    new_state[new_blank], new_state[blank]

                new_state = tuple(new_state)

                if new_state not in visited:
                    visited.add(new_state)
                    queue.append((new_state, path + [current]))

    return None


def display(state):
    print(state[0], state[1], state[2])
    print(state[3], state[4], state[5])
    print(state[6], state[7], state[8])


# Initial puzzle
start = (1, 2, 3,
         4, 0, 6,
         7, 5, 8)

solution = solve_puzzle(start)

if solution:
    print("8-PUZZLE SOLUTION")
    print("-----------------")

    for i, state in enumerate(solution):
        print("\nStep", i)
        display(state)

    print("\nTotal moves:", len(solution) - 1)

else:
    print("No solution exists.")
