# 2048 Game

# To-do:
# - Score board - add whatever was merged
# - New game?
# - Show game over/out of moves
# - Condense logic of up/down by using left/right



import numpy as np

# Create starting board
def start_game():
    # Set all initial spaces to 0
    game_board = np.array([
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ])

    # Choose two random spaces to start as numbers
    new_number(game_board)
    new_number(game_board)

    # Print rules to the game
    print(game_board)
    print("Welcome to 2048! How to play: Type [up, down, left, right] to move the tiles. Tiles with the same number merge into one when they touch. Add them up to reach 2048!")

    while True:
        move = input("Select a move (left, right) or type 'quit' to end the game: ")

        if move == "quit":
            break # Exit the loop

        print("") # Get a blank line in between moves

        match move:
            case "left":
                swipe_left(game_board)
            case "right":
                swipe_right(game_board)
            case "up":
                swipe_up(game_board)
            case "down":
                swipe_down(game_board)
            case _:
                print("Invalid move, please select [left or right]")

        new_number(game_board)
        print(game_board)

def new_number(game_board):
    #There's a 10% chance of getting a 4 in a new tile instead of a 2. We'll decide that here
    new_tile_number = np.random.randint(100)

    # Choose the coordinates for our new tile
    new_tile_row = np.random.randint(4)
    new_tile_column = np.random.randint(4)

    # Variable to determine whether our new coordinates are an open space
    open_space = False

    # Run until new tile complies with rules
    while not open_space:
        
        # If the space is free, add a 2 or 4
        if game_board[new_tile_row, new_tile_column] == 0:
            if new_tile_number < 10:
                game_board[new_tile_row, new_tile_column] = 4
            else:
                game_board[new_tile_row, new_tile_column] = 2
            open_space = True
        
        # Otherwise, 
        else:
            # Reroll
            new_tile_row = np.random.randint(4)
            new_tile_column = np.random.randint(4)

    return game_board

# Swipe Left
def swipe_left(game_board):
    for row in range(len(game_board)):
        # Get rid of zeroes
        new_row = [value for value in game_board[row] if value != 0]
        
        # Combine like numbers in new array
        merged_row = []
        i = 0
        while i < len(new_row):
            if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
                merged_row.append(new_row[i] * 2)
                i += 2  # Skip the next element since it has been merged
            else:
                merged_row.append(new_row[i])
                i += 1

        # Add zeroes to the merged row
        while len(merged_row) < len(game_board):
            merged_row.append(0)

        game_board[row] = merged_row

    print("swiped left. Here's the new board: ")

# Swipe Right
def swipe_right(game_board):
    for row in range(len(game_board)):
        # Get rid of zeroes
        new_row = [value for value in game_board[row] if value !=0]

        # Combine like numbers in new array
        merged_row = []
        i = len(new_row) -1
        while i >= 0:
            if i - 1 >= 0 and new_row[i] == new_row[i - 1]:
                merged_row.insert(0, new_row[i] * 2) # Using insert at position 0 rather than append
                i -= 2 # Skip the next element since it has already been merged
            else:
                merged_row.insert(0, new_row[i])
                i -= 1

        # Add zeroes to the merged row
        while len(merged_row) < len(game_board):
            merged_row.insert(0, 0)

        game_board[row] = merged_row

    print("swiped right. Here's the new board: ")

# Swipe Up
def swipe_up(game_board):
    # Transpose game_board
    transposed_game_board = game_board.transpose()

    # Apply logic of swipe_left
    for row in range(len(transposed_game_board)):
        # Get rid of zeroes
        new_row = [value for value in transposed_game_board[row] if value != 0]
        
        # Combine like numbers in new array
        merged_row = []
        i = 0
        while i < len(new_row):
            if i + 1 < len(new_row) and new_row[i] == new_row[i + 1]:
                merged_row.append(new_row[i] * 2)
                i += 2  # Skip the next element since it has been merged
            else:
                merged_row.append(new_row[i])
                i += 1

        # Add zeroes to the merged row
        while len(merged_row) < len(transposed_game_board):
            merged_row.append(0)

        transposed_game_board[row] = merged_row

    # Re-transpose
    game_board = transposed_game_board.transpose()

    print("swiped up. Here's the new board: ")

# Swipe Down
def swipe_down(game_board):
    # Transpose game_board
    transposed_game_board = game_board.transpose()

    # Apply logic of swipe_right
    for row in range(len(transposed_game_board)):
        # Get rid of zeroes
        new_row = [value for value in transposed_game_board[row] if value !=0]

        # Combine like numbers in new array
        merged_row = []
        i = len(new_row) -1
        while i >= 0:
            if i - 1 >= 0 and new_row[i] == new_row[i - 1]:
                merged_row.insert(0, new_row[i] * 2)
                i -= 2 # Skip the next element since it has already been merged
            else:
                merged_row.insert(0, new_row[i])
                i -= 1

        # Add zeroes to the merged row
        while len(merged_row) < len(transposed_game_board):
            merged_row.insert(0, 0)

        transposed_game_board[row] = merged_row

    # Re-transpose
    game_board = transposed_game_board.transpose()

    print("swiped down. Here's the new board: ")

# Start the game!
start_game()