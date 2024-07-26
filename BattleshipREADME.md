Python Journal - Battleship game
Date: 11/24/2023

PART 1: Plan

Two friends are bored. I will create a game of battleship to keep them busy. 
Each player will have 1 ship on a board of 10 squares that will be divided into 2 boards (one per player). Each ship will take the space of 1 square. Each player will play one after the other.

The ships will be placed by the player on their respective boards using their input. 
They will then input each of their attacks to the enemy's board.  After 1 hit, the ship is down and the game automatically ends.
Each player has one turn to sink the enemy ship and the game can be restarted by running the program again.

The outputs throughout the program will : 
Show the players their boards at the beginning of the game
Tell the players to place their ship
Inform the player their ship is placed
Tell the players to launch their attack
Inform the player if they won or lost

The inputs needed : 
Numbers from 1 to 5 from both players


PART 2: Specific possible outcomes/cases


Scenario 1 : one of the player wins

1. player 1 sets up his ship
2. player 2 sets up his ship
3. Player 1 or 2  hits enemy ship
4. player 1 or 2 wins the game

Scenario 2 : one of the player enters an integer input out of range

1. player 1 sets up his ship
2. player 2 sets up his ship
3. player 1 tries to hit player 2 ship
4. Player 1 misses
5. player 2 tries to hits player 1 ship but enter incorrect integer input
6. Player 2 is asked again to enter correct input
7. Program will ask for correct integer input until correct input is entered or users close or stop the program

PART 3: Pseudocode

#creating classes and objects

class board
create a board object from the class
board value =  array of 5 index or “squares” (1,2,3,4,5) 


#Main Program

Initializing the boards (1 per player) from the board class object
output visual representation of board on screen

#request input from players to place their ship on their board:

output “Pick a place on your board from 1 to 5”
get input from player 1 and remove 1 from input number, to match numbers of the board index (0 to 4)
Make sure the input is the expected input (an integer within range) 
assign ship to square from input
ship 1 is placed on board
confirm to player that the ship is placed down 

output “Pick a place on your board from 1 to 5”
get input from player 2 and remove 1 from input number, to match numbers of the board index (0 to 4) 
Make sure the input is the expected input (an integer within range) 
assign ship to square from input
ship 2 is placed on board
confirm to player that the ship is placed down 


#request input from player to attack the opponent's board:

output “Choose a place on the board to hit between 1 and 5”
get input from player 1 and remove 1 from input number, to match numbers of the board index (0 to 4) 
Make sure the input is the expected input (an integer within range) 
Check the player2’s board at the index given by player1’s input
if index = 1, player 1 wins
outputs “You won!”
game ends

else if square = 0
Outputs “You missed, maybe more luck next time?”

output “Choose a place on the board to hit between 1 and 5”
get player 2 input and remove 1 from input number, to match numbers of the board index (0 to 4) 
Make sure the input is the expected input (an integer within range) 
Check the player1’s board at the index given by player2’s input
if square = 1, player 1 wins
outputs “You won!”
game ends

else if square = 0
Outputs “You missed, maybe more luck next time?”


The game is now over, restart to play a new round!”




PART 4: Testing log

NameError : name 'PlayerOneBoard' is not defined

When I came across this error, I knew the issue was the fact that the board for player 1 was not initialized.
I had a line that was doing this, but that line was under def main() at the time. I suspected that because it was under def main() it was isolated from the rest of the program that was not indented under def main. 
I looked into the python documentation and saw that def main was not a requirement so I removed def main, fixed the indentation and the error was fixed.

Infinite loop

When I was asking for the first input from the first player, no matter what number I was entering it was  always asking again and was not moving to the next step. This was not listed on the error log but was an issue. 
I supposed the issue was in my while statement which at the time was  this :
while playerOneInput != 0 or 1 or 2 or 3 or 4
I changed it to this and the issue was fixed :
while playerOneInput not in [0, 1, 2, 3, 4]:

AttributeError : 'boardClass' object has no attribute 'insert'

I was using insert as it is a pre-build function to work with arrays in python. From that error message, I thought that the program was not able to know it was an array and/or access it. As I was not sure how to address this, I looked up how to access an array from a class and added the missing part to my line, the part that was access the object and not just the class. This fixed the issue.

TypeError : ‘boardClass’ object is not subscriptable

This was the main issue and the most difficult error I had. When making my program I knew the steps I wanted to take but I was not sure how to write it in code. 
I wanted to take the input from a player and check the opponent’s board at the index corresponding to the input (minus 1). 

My first idea was to write it like this : 
playerTwoBoard[playerOneAttack] 

At this point I was not sure how to address this. I googled the error to find more explanations. While this gave me a little bit of understanding of what was happening, nothing helped me. 
I then remembered the previous and similar issue I had that also included ‘boardClass’
I added the same part to access the object and this fixed the issue. 

TypeError: list indices must be integers or slices, not type

This error came right after my previous one. I was not sure what it could be as it was only throwing this error when I was comparing an input to an array and not when I was inserting the input to the array. I was also thinking I was doing what was supposed to be done but after looking more closely to that line, I saw I was using “1” and not 1. Even if it looked like the same thing, their type were different and that was the issue. I removed the “ “ and the error was resolved.

Unknown error

At this point the program was fully running with no error. While testing it, I came across an issue. When placing ships in position 1 (index 0) and then attacking ship in position 2 (index 1) the game would say you won which is supposed to be a miss. I tried with position 3, 4 and 5 and the game was running as intended.

I was not sure why or how this was happening, as I had done print test along the program to make sure the ship would be placed at the correct index in the array. 

I decided to print the boards to make sure and the console output showed me the issue.
For the first player, the ship would be inserted at the right position in that array but the array will get an extra index instead of the 0 being replace by a 1.
For the second player, the ship would be inserted at the right position but it was inserted in the same array that for player one, when they are both to be 2 separate arrays.

To fix the first part of the issue, I created two board_member objects as they were clearly both using the same one. I was not sure why they were doing that. When creating two objects, there was no issues so I knew the issue was in those first line. I read documentation on how to make a class and its object in python and was able to figure out the part of the statement I missed. The issue is now fixed.

For the insert issue. I looked up how to access and replaced the content of an array at a give index as the insert function was not working. I was able to find a way that looked like it would work and added it, the issue was fixed. 


The code now works well and the outcome looks like what I had expected. The program works and I think the next step would be to make a bigger board with a X and Y, have multiple ships, include a number of turns and loop through those.


2.Test done throughout : 

To test my program, to either find where the error was or to see why something would not work as intended, I would use print statement. To either print the board and see what was going on internally behind the scene or a random print statement to see how far in my lines the program would go before stopping. 

print(“test)
print(playerOneBoard.board_member)

I also tested it by entering all possible options that the players could enter to make sure all were working as intended.

3.Edge cases/user error (scenario 2)

The main issue that I saw could happen was for users to enter a wrong number or something that is not the expected number.
I applied a condition that if the number entered by a user is not one of the expected ones, the user will be asked to try again, using the right number. 


This condition should also be applied to anything entered that would not be an integer and that is currently throwing an error when inputted. 
Since any input in python is a string, the approach I took to get the input will not allow for an exception as it is on the same line.
To test this (possible)scenario 3, user entering a letter, I would have to divide what I did in multiples steps.
 I would have to get the input, check that input to make sure it is an integer and then convert it to an integer to then make sure it is in range. For now, I will have to rely on the users to properly read the instructions requesting them to enter a number.
