#Define the Board Class and initialize members
class boardClass(object):

  #constructor and initializer for member variables
  def __init__(self):
    self.board_member = [0] * 5


#create the players' boards
playerOneBoard = boardClass()
playerTwoBoard = boardClass()

#print the 2 boards on console
print("Welcome to the game, this is a 2 players game, player 1 starts the game.") 
print ("Those are your boards: ")
print(playerOneBoard.board_member)
print(playerTwoBoard.board_member)
print("\n")


print("You will now both place your ships.\n")
#get player1 input, convert it to an int and make sure the number is in range of board size
#remove 1 to the input integer as the array index starts at 0 and not 1
playerOneInput = int(input("Player 1, enter a number between 1 and 5: ")) -1
while playerOneInput not in [0, 1, 2, 3, 4]:
  playerOneInput = int(
      input("Player 1, please try again, enter a number between 1 and 5: ")) -1



#insert player1's input in the board array at the index choosen by player
#remplace the 0 that was inside the array by 1
index = playerOneInput
playerOneBoard.board_member[index] = 1

#let player1 know his move have been recorded
print("Ship of player 1 is placed\n")




#get player2's input, convert it to an int and make sure the number is in range of board size
#remove 1 to the input integer as the array index starts at 0 and not 1
playerTwoInput = int(input("Player 2, enter a number between 1 and 5: ")) -1
while playerTwoInput not in [0, 1, 2, 3, 4]:
  playerTwoInput = int(
      input("Player 2, please try again, enter a number between 1 and 5: ")) -1

#insert player2's input in the board array at the index choosen by player
#remplace the 0 by 1 in the array
index = playerTwoInput
playerTwoBoard.board_member[index] = 1

#let player2 know his move have been recorded
print("Ship of player 2 is placed\n")



print("You will now attack your opponent's board.\n")
#get player1's input, convert it to an int and make sure the number is in range of board size
#remove 1 to the input integer as the array index starts at 0 and not 1
playerOneAttack = int(input("Player 1, enter a number between 1 and 5: ")) -1
while playerOneAttack not in [0, 1, 2, 3, 4]:
  playerOneAttack = int(input("Player 1, please try again, enter a number between 1 and 5: ")) -1

#check player1's input against his opponent's board 
#if number at index choosen by player1 in player2 board is equal to 1, player1 won
#if it is not the case, print you missed
if (playerTwoBoard.board_member[playerOneAttack] == 1):
  print("You won!")
  print("The game is now over, please restart to play another round")
#exit as player2 should not play his turn
  exit()
else:
  print("You missed, maybe more luck next time? \n")




#get player2's input, convert it to an int and make sure the number is in range of board size
#remove 1 to the input integer as the array index starts at 0 and not 1

playerTwoAttack = int(input("Player 2, enter a number between 1 and 5: ")) -1
while playerTwoAttack not in [0, 1, 2, 3, 4]:
  playerTwoAttack = int(input("Player 2, please try again, enter a number between 1 and 5: ")) -1

#check player2's input against his opponent's board 
#if number at index choosen by player2 in player1 board is equal to 1, player2 won
#if it is not the case, print you missed
if (playerOneBoard.board_member[playerTwoAttack] == 1):
  print("You won!")
  print("The game is now over, please restart to play another round")

else:
  print("You missed, maybe more luck next time?")
  
  print("The game is now over, please restart to play another round!")
