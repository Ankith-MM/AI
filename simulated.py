import random
import math

N = 8

def cost(state):
    conflicts = 0

    for i in range(N):
        for j in range(i + 1, N):
            if state[i] == state[j]:
                conflicts += 1
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts

def print_board(state):
    for row in range(N):
        for col in range(N):
            if state[col] == row:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

def random_neighbor(state):
    neighbor = state.copy()
    col = random.randint(0, N - 1)
    row = random.randint(0, N - 1)

    while row == neighbor[col]:
        row = random.randint(0, N - 1)

    neighbor[col] = row
    return neighbor

def simulated_annealing(current):
    T = 100.0
    cooling_rate = 0.95
    max_iterations = 100000

    for _ in range(max_iterations):
        if cost(current) == 0:
            return current

        next_state = random_neighbor(current)
        delta_E = cost(next_state) - cost(current)

        if delta_E < 0:
            current = next_state
        else:
            probability = math.exp(-delta_E / T)

            if random.random() < probability:
                current = next_state

        T *= cooling_rate

        if T < 0.0001:
            T = 100.0

    return current if cost(current) == 0 else None

print("Enter row positions of 8 queens (0-7):")
print("Example: 0 0 0 0 0 0 0 0")

try:
    initial = list(map(int, input("Enter positions: ").split()))

    if len(initial) != N or any(x < 0 or x >= N for x in initial):
        print("Invalid input! Enter exactly 8 integers between 0 and 7.")
    else:
        initial_conflicts = cost(initial)

        print("\nInitial arrangement:")
        print_board(initial)
        print("Initial conflicts:", initial_conflicts)

        if initial_conflicts == 0:
            print("\nThe initial arrangement is already a solution!")
            solution = initial
        else:
            print("\nSolving using Simulated Annealing...")
            solution = simulated_annealing(initial)

        if solution is not None:
            print("\nFinal arrangement:")
            print_board(solution)
            print("Final conflicts:", cost(solution))
        else:
            print("\nNo solution found. Please try again.")

except ValueError:
    print("Invalid input! Please enter integers only.")
