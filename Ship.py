
def sea_battle(grid, shots):
    ships = {}
    attacked = set()
    result = []
    dots = set()

    for i in range(len(grid)):
        for j in range(len(grid[0])):
              # if grid[i][j].isalpha():
                if grid[i][j] not in ships:
                    ships[grid[i][j]] = set()
                ships[grid[i][j]].add((i, j))

    for shot in shots:
        x, y = shot
        if (x, y) in attacked:
            result.append("Already attacked")
        elif grid[x][y] == ".":
            result.append("Missed")
            #dots.add((x, y))
        else:
            ship_key = grid[x][y]
            ship_coords = ships[ship_key]
            ship_coords.remove((x, y))
            if not ship_coords:
                result.append(f"ship {ship_key} sunk")
                del ships[ship_key]
            else:
                result.append(f"Attacked ship {ship_key}")
            attacked.add((x, y))

    return result

# Reading the grid and shots from the console
# print("Enter the grid:")

# print("Enter the shots:")
# input: 
grid = [
    [".", "A", "B", "B", "B"],
    [".", "A", ".", ".", "C"],
    ["D", "D", ".", ".", "."],
    [".", "E", "E", "E", "E"]
]
shots = [[0, 0], [0, 1], [0, 2], [1, 1], 
         [0, 1], [1, 4], [2, 2], [2, 4], [0, 3], [0, 0], [0, 4]
]

print(sea_battle(grid, shots))




