# 2 player Tic Tac Toe

import os

class TicTacToe:

    def __init__(self):       

        #initialize the board to all empty squares
        self.Board = [" " for i in range(9)]

        #Representation of each index in self.Board
        #          |       |
        #     [0]  |  [1]  |  [2]
        #    ______|_______|_______   
        #          |       |
        #     [3]  |  [4]  |  [5]
        #    ______|_______|_______
        #          |       |
        #     [6]  |  [7]  |  [8]
        #          |       |
        
        #Whose turn is it; X is true; O is false
        self.Turn = True

        #To check for a tie       
        self.NumMoves = 0        

    #returns true if the latest move is a win
    def CheckForWin(self):
        if  ( 
            ((self.Board[0] + self.Board[1] + self.Board[2]) == "XXX") or #top row
            ((self.Board[3] + self.Board[4] + self.Board[5]) == "XXX") or #middle row
            ((self.Board[6] + self.Board[7] + self.Board[8]) == "XXX") or #bottom row
            ((self.Board[0] + self.Board[3] + self.Board[6]) == "XXX") or #left column
            ((self.Board[1] + self.Board[4] + self.Board[7]) == "XXX") or #center column
            ((self.Board[2] + self.Board[5] + self.Board[8]) == "XXX") or #right column
            ((self.Board[0] + self.Board[4] + self.Board[8]) == "XXX") or #Diagonal \
            ((self.Board[6] + self.Board[4] + self.Board[2]) == "XXX")    #Diagonal /
            ):                       
        
            print("X Wins!!!\n")
            return True

        elif(             
            ((self.Board[0] + self.Board[1] + self.Board[2]) == "OOO") or #top row
            ((self.Board[3] + self.Board[4] + self.Board[5]) == "OOO") or #middle row
            ((self.Board[6] + self.Board[7] + self.Board[8]) == "OOO") or #bottom row
            ((self.Board[0] + self.Board[3] + self.Board[6]) == "OOO") or #left column
            ((self.Board[1] + self.Board[4] + self.Board[7]) == "OOO") or #center column
            ((self.Board[2] + self.Board[5] + self.Board[8]) == "OOO") or #right column
            ((self.Board[0] + self.Board[4] + self.Board[8]) == "OOO") or #Diagonal \
            ((self.Board[6] + self.Board[4] + self.Board[2]) == "OOO")    #Diagonal /        
        ):
            print("O Wins!!!\n") 
            return True

        elif self.NumMoves >= 9:
            print("Its a tie!!!\n")
            return True

        else:
            return False          

    def DrawBoard(self):
        os.system('cls')
        print("\n")
        print("    1    |    2    |    3    ")
        print("         |         |         ")        
        print("    %s    |    %s    |    %s    " % ((self.Board[0]), self.Board[1], self.Board[2]))
        print("         |         |         ")        
        print("_________|_________|_________")
        print("    4    |    5    |    6    ")
        print("         |         |         ")
        print("    %s    |    %s    |    %s    " % ((self.Board[3]), self.Board[4], self.Board[5])) 
        print("         |         |         ")
        print("_________|_________|_________")
        print("    7    |    8    |    9    ")
        print("         |         |         ")
        print("    %s    |    %s    |    %s    " % ((self.Board[6]), self.Board[7], self.Board[8]))
        print("         |         |         ")
        print("         |         |         ")
        print("\n") 
        


    #adds valid moves to the board
    def AddMove(self, move):
        if (self.Board[move] == " "):
            if self.Turn:
                self.Board[move] = "X"
                self.Turn = False
            else:
                self.Board[move] = "O"
                self.Turn = True
            self.NumMoves += 1
        else:
            print("Invalid Move\n")        
        


    #the main iterative loop of the game
    def Play(self):
        self.DrawBoard()        
        while not self.CheckForWin():
            print("press 0 to quit")           
            if self.Turn == True:
                try:
                    move = int(input("make a move X:")) - 1
                    self.AddMove(move)
                except:
                    print("invalid move")            
                    
            else:
                try:
                    move = int(input("make a move O:")) - 1
                    self.AddMove(move)
                except:
                    print("invalid move")
            if move == -1: break
            self.DrawBoard()           
            


#main
Game = TicTacToe()
Game.Play()

input("press enter to close\n")