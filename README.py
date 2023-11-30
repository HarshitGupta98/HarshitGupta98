import random



def ConstBoard(board):
    print("Current State of the board \n\n")
    for i in range(3):
        for j in range(3):
            index = i * 3 + j
            if board[index] == -1:
                print(" X ", end="")
            elif board[index] == 1:
                print(" O ", end="")
            else:
                print(" _ ", end="")
            
            if j < 2:
                print("|", end="")
        print()
        if i < 2:
            print("-----------")
    print("\n\n")







def User1Turn(board):
  while True:
      pos = input("Enter X's value from [1,2,3,4,5,6,7,8,9]: ")
      pos = int(pos)
      if board[pos - 1] == 0:
          board[pos - 1] = -1
          break
      else:
          print("Wrong move. Try again.")


def User2Turn(board):
  while True:
      pos = input("Enter O's value from [1,2,3,4,5,6,7,8,9]: ")
      pos = int(pos)
      if board[pos - 1] == 0:
          board[pos - 1] = 1
          break
      else:
          print("Wrong move. Try again.")


'''world's best tic tac toe AI made by harshit gupta of class tenth
but you can still defeat this bot'''
def CompTurn(board):
  available_positions = [i for i in range(9) if board[i] == 0]

  if available_positions:
      pos = random.choice(available_positions)
      board[pos] = 1
  else:
      print("No available moves for the computer.")


def analyzeboard(board):
  cb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for i in range (0,8):
    if(board[cb[i][0]]!=0 and
      board[cb[i][0]]==board[cb[i][1]] and
      board[cb[i][0]]==board[cb[i][2]]):
     return board[cb[i][0]]
  return 0


def restart_game():
  print("Restarting the game...")
  main()


def main():
  choice = input("Enter 1 for single player, 2 for multiplayer, or 0 to exit:  ")
  choice = int(choice)
  board = [0,0,0,0,0,0,0,0,0]
  if choice == 0:
    print("Exiting the game. Goodbye!")
    exit()
  if (choice==1):
    print ("sample grid")
    print (" 1  2  3 ")

    print (" 4  5  6 ")

    print (" 7  8  9 ")
    print("Computer: O VS. you: X")
    player = input("Enter to play 1(st) or 2(nd): ")
    player = int(player)
    for i in range(0, 9):
      if(analyzeboard(board)!=0):
        break;
      if((i+player)%2==0):
        CompTurn(board)
      else:
        ConstBoard(board)
        User1Turn(board)
  elif choice != 1 and 2 and 0 :
    print ("kindly choose from 1, 2 and 0 ")
    main()
  elif choice ==2 :
    print ("sample grid")
    print (" 1  2  3 ")

    print (" 4  5  6 ")

    print (" 7  8  9 ")
    for i in range(0, 9):
      if(analyzeboard(board)!=0):
        break;
      if((i)%2==0):
        User1Turn(board)
      else:
        ConstBoard(board)
        User2Turn(board)
  x = analyzeboard(board)
  if(x==0):
    ConstBoard(board)
    print("draw!")
  if(x==-1):
    ConstBoard(board)
    print("\nPlayer X Wins !!!!! O Looses!")
  if(x==1):
    ConstBoard(board)
    print("Player O Wins !!!!! X Looses!")

  while True:
    restart_game()

       
if __name__ == "__main__":
  main()
  
