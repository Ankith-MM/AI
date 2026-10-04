def print_board(state):
   
    for i in range(0, 9, 3):
        print(" ".join(str(x) if x != 0 else "_" for x in state[i:i+3]))
    print()


def get_neighbors(state):
    
    zero_idx = state.index(0)
    row, col = zero_idx // 3, zero_idx % 3
    neighbors = []

    
    moves = [(-1, 0, 'Up'), (1, 0, 'Down'), (0, -1, 'Left'), (0, 1, 'Right')]

    for dr, dc, move_name in moves:
        nr, nc = row + dr, col + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_idx = nr * 3 + nc
            state_list = list(state)
            state_list[zero_idx], state_list[new_idx] = state_list[new_idx], state_list[zero_idx]
            neighbors.append((tuple(state_list), move_name))

    return neighbors


def is_solvable(initial_state, goal_state):
    
    def count_inversions(state):
        arr = [x for x in state if x != 0]
        inversions = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] > arr[j]:
                    inversions += 1
        return inversions

    return (count_inversions(initial_state) % 2) == (count_inversions(goal_state) % 2)


def dfs(initial_state, goal_state, max_depth=20):
  
    stack = [(initial_state, [initial_state], [])]

    while stack:
        current, path, moves = stack.pop()

        if current == goal_state:
            return path, moves

        if len(path) - 1 < max_depth:
            for neighbor, move in get_neighbors(current):
                if neighbor not in path:
                    stack.append((neighbor, path + [neighbor], moves + [move]))

    return None, None


def ids(initial_state, goal_state, max_limit=30):
   vely increases the depth limit until a solution is found.
    
    for limit in range(max_limit + 1):
        stack = [(initial_state, [initial_state], [], 0)]

        while stack:
            current, path, moves, current_depth = stack.pop()

            if current == goal_state:
                return path, moves, limit

            if current_depth < limit:
                for neighbor, move in get_neighbors(current):
                    if neighbor not in path:
                        stack.append((neighbor, path + [neighbor], moves + [move], current_depth + 1))

    return None, None, None


def main():
    print("=== 8-Puzzle Solver ===")
    print("Enter numbers 0 to 8 separated by space (0 represents the blank space).")

    try:
        raw_input = input("Enter initial state (e.g., 1 2 3 4 0 6 7 5 8): ").strip()
        initial_state = tuple(map(int, raw_input.split()))

        if len(initial_state) != 9 or set(initial_state) != set(range(9)):
            print("Error: Input must contain exactly 9 unique digits from 0 to 8.")
            return

        goal_input = input("Enter goal state (press Enter for default '1 2 3 4 5 6 7 8 0'): ").strip()
        if goal_input:
            goal_state = tuple(map(int, goal_input.split()))
        else:
            goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    except ValueError:
        print("Invalid input format. Please enter space-separated numbers.")
        return

    print("\nInitial State:")
    print_board(initial_state)
    print("Goal State:")
    print_board(goal_state)

    if not is_solvable(initial_state, goal_state):
        print("This configuration is unsolvable!")
        return

    print("Choose Search Algorithm:")
    print("1. Depth-First Search (DFS)")
    print("2. Iterative Deepening Search (IDS)")
    choice = input("Enter option (1 or 2): ").strip()

    if choice == '1':
        print("\nRunning DFS...")
        path, moves = dfs(initial_state, goal_state)
        if path:
            print(f"Solution found in {len(moves)} steps!")
            print("Move sequence:", " -> ".join(moves))
            print("\nStep-by-step path:")
            for idx, state in enumerate(path):
                print(f"Step {idx}:")
                print_board(state)
        else:
            print("No solution found within depth limit.")

    elif choice == '2':
        print("\nRunning IDS...")
        path, moves, depth_found = ids(initial_state, goal_state)
        if path:
            print(f"Optimal solution found at depth {depth_found} with {len(moves)} steps!")
            print("Move sequence:", " -> ".join(moves))
            print("\nStep-by-step path:")
            for idx, state in enumerate(path):
                print(f"Step {idx}:")
                print_board(state)
        else:
            print("No solution found within search limit.")

    else:
        print("Invalid algorithm selection.")


if __name__ == "__main__":
    main()
