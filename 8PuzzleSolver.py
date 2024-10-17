import heapq

# Utility function to calculate the Manhattan Distance heuristic
def manhattan_distance(state, goal):
    distance = 0
    for i in range(1, 9):
        x1, y1 = divmod(state.index(i), 3)
        x2, y2 = divmod(goal.index(i), 3)
        distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

# Function to get the neighboring states (valid moves)
def get_neighbors(state):
    neighbors = []
    index = state.index(0)  # Position of the empty tile (0)
    x, y = divmod(index, 3)
    
    # Move directions: Up, Down, Left, Right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_index = new_x * 3 + new_y
            new_state = list(state)
            new_state[index], new_state[new_index] = new_state[new_index], new_state[index]
            neighbors.append(tuple(new_state))
    
    return neighbors

# A* Algorithm to solve the 8-puzzle
def a_star(start, goal):
    # Priority queue for the A* search
    open_list = []
    heapq.heappush(open_list, (0 + manhattan_distance(start, goal), 0, start, []))
    
    visited = set()
    
    while open_list:
        # Pop the state with the lowest f(n) = g(n) + h(n)
        _, cost, current_state, path = heapq.heappop(open_list)
        
        if current_state in visited:
            continue
        
        # If the goal state is reached, return the path and cost
        if current_state == goal:
            return path + [current_state], cost
        
        visited.add(current_state)
        
        # Explore neighbors
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                new_cost = cost + 1  # Each move costs 1
                heapq.heappush(open_list, (new_cost + manhattan_distance(neighbor, goal), new_cost, neighbor, path + [current_state]))
    
    return None  # If no solution is found

# Initial state and goal state
start_state = (1, 3, 5, 8, 0, 2, 4, 7, 6)  # The 8-puzzle starting configuration
goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)   # The goal configuration

# Solve the puzzle
solution, cost = a_star(start_state, goal_state)

# Print the solution path
if solution:
    print(f"Solution found with cost {cost}:")
    for state in solution:
        print(state[:3])
        print(state[3:6])
        print(state[6:])
        print()
else:
    print("No solution found.")
