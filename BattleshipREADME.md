# Python Journal - Battleship Game

**Date:** 11/24/2023

## PART 1: Plan

Two friends are bored, so I will create a Battleship game to keep them busy. Each player will have 1 ship on a board of 10 squares divided into 2 boards (one per player). Each ship will take up the space of 1 square. Players will alternate turns, placing their ships and attacking the enemy's board. The game ends when a ship is hit.

### Game Flow

1. **Board Setup:**
   - Show the players their boards at the beginning of the game.
   - Ask players to place their ships.
   - Confirm ship placement to the players.

2. **Gameplay:**
   - Ask players to launch their attacks.
   - Inform players if they hit or missed.
   - Declare the winner when a ship is hit.

### Inputs

- Numbers from 1 to 5 from both players.

## PART 2: Specific Possible Outcomes/Cases

### Scenario 1: One Player Wins

1. Player 1 sets up their ship.
2. Player 2 sets up their ship.
3. Player 1 or Player 2 hits the enemy ship.
4. The game ends, and the winner is declared.

### Scenario 2: Invalid Input

1. Player 1 sets up their ship.
2. Player 2 sets up their ship.
3. Player 1 tries to hit Player 2's ship.
4. Player 1 misses.
5. Player 2 tries to hit Player 1's ship but enters an incorrect integer input.
6. Player 2 is prompted to enter a correct input.
7. The program will continue to request correct input until valid data is entered or the program is stopped.

## PART 3: Pseudocode

```python
# Creating classes and objects
class Board:
    # Initialize a board with 5 squares
    def __init__(self):
        self.squares = [0] * 5

# Main Program
def main():
    # Initialize boards
    player_one_board = Board()
    player_two_board = Board()
    
    # Show boards
    print("Player 1's board:")
    print(player_one_board.squares)
    print("Player 2's board:")
    print(player_two_board.squares)
    
    # Request ship placement
    for player in range(1, 3):
        place_ship(player)

    # Request attacks
    for player in range(1, 3):
        attack_opponent(player)

def place_ship(player):
    # Prompt player to place their ship
    print(f"Player {player}, pick a place on your board from 1 to 5:")
    ship_placement = int(input()) - 1  # Adjust for 0-based index
    if 0 <= ship_placement < 5:
        # Place ship
        print(f"Player {player}'s ship is placed at position {ship_placement + 1}.")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")

def attack_opponent(player):
    # Prompt player to attack
    print(f"Player {player}, choose a place on the board to hit between 1 and 5:")
    attack_position = int(input()) - 1  # Adjust for 0-based index
    if 0 <= attack_position < 5:
        # Check if the attack hits
        if player == 1:
            opponent_board = player_two_board
        else:
            opponent_board = player_one_board
        
        if opponent_board.squares[attack_position] == 1:
            print(f"Player {player} wins!")
            return
        else:
            print("You missed, maybe more luck next time?")
    else:
        print("Invalid input. Please enter a number between 1 and 5.")
```

## PART 4: Testing Log

### Errors and Fixes

1. **NameError: `name 'PlayerOneBoard' is not defined`**
   - **Issue:** `PlayerOneBoard` was not initialized.
   - **Fix:** Moved initialization inside the `main()` function and adjusted the indentation.

2. **Infinite Loop**
   - **Issue:** The input validation loop for the first player was incorrect.
   - **Fix:** Changed the `while` condition to:
     ```python
     while playerOneInput not in [0, 1, 2, 3, 4]:
     ```

3. **AttributeError: `'boardClass' object has no attribute 'insert'`**
   - **Issue:** Using `insert` on an array object.
   - **Fix:** Replaced `insert` with appropriate array access methods.

4. **TypeError: `'boardClass' object is not subscriptable`**
   - **Issue:** Incorrect access of array elements from a class object.
   - **Fix:** Adjusted array access to work with class objects.

5. **TypeError: `list indices must be integers or slices, not type`**
   - **Issue:** Comparing input values with strings instead of integers.
   - **Fix:** Ensured that comparisons use integer values.

6. **Unknown Error**
   - **Issue:** Incorrect behavior when placing and attacking ships.
   - **Fix:** Created separate board objects for each player and ensured correct board access.

### Testing Methods

- **Print Statements:** Used to check the board state and program flow.
  ```python
  print("test")
  print(playerOneBoard.board_member)

