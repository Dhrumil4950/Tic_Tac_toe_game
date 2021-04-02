from enum import Enum

class TicTacToe:
    class STATES(Enum):
        CROSS_TURN = 0
        NIGHT_TURN = 1
        DRAW = 2
        CROSS_WON = 3
        NAUGHT_WON = 4
    def __init__(self):
        self.board = []
        for i in range(3):
            self.board.append(["","",""])

    def print_board(self):
        response = ""
        for i in range(len(self.board)):
            for item in self.board[i]:
                if item == "":
                    response += " _ "
                else:
                    response += " " + str(item) + " "
            response+="\n"

        return response

    def is_board_filled(self):
        filled_totally = True
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=="":
                    filled_totally = False
                    break

        return filled_totally



    def __repr__(self):
        return self.print_board()

    def is_place_taken(self,row,col):
        if self.board[row-1][col-1]!="":
            return True
        return False

    def place_marker(self,symbol,row,column):
        self.board[row-1][column-1] = symbol

        print(self.print_board())


        if self.board[row-1][0] == symbol and self.board[row-1][1] == symbol and self.board[row-1][2] == symbol:
                return ('game_won',True)
        elif self.board[0][column-1] == symbol and self.board[1][column-1] == symbol and self.board[2][column-1] == symbol:
                return ('game_won',True)
        else :
            if self.is_board_filled()==True:
                return ('game_drawn',True)
            else:
                return ('game_won',False)

tic = TicTacToe()

valid_input_for_start = False
while valid_input_for_start==False:
    player_one_symbol = input("First Player Input ( SELECT FROM 'X' OR '0') : ")
    if player_one_symbol == 'X' or player_one_symbol =='0':
        valid_input = True
        if player_one_symbol == 'X':
            player_two_symbol = "0"
        else:
            player_two_symbol = 'X'

        print("Player One Symbol is {}".format(player_one_symbol))
        print("Player Two Symbol is {}".format(player_two_symbol))

        print(tic)

        while tic.is_board_filled() is not True:
            print("Player One Input now ")
            valid_input_for_player_one = False
            while valid_input_for_player_one == False:
                try:
                    player_one_row_val = int(input("Enter row : "))
                    player_one_col_val = int(input("Enter column : "))

                    if (player_one_row_val > 3 or player_one_row_val < 0) and (
                            player_one_col_val > 3 or player_one_col_val < 0):
                        print("Enter a number between 1 to 3")
                        valid_input_for_player_one = False
                    else:
                        if tic.is_place_taken(player_one_row_val,player_one_col_val)==True:
                            print("This position is already filled . Choose some other row and column value")
                            valid_input_for_player_one = False
                        else:
                            valid_input_for_player_one = True
                            # if tic.is_place_taken(player_one_row_val,player_one_col_val)==False:
                            #     valid_input=True


                except:
                    print("Enter a number between 1 to 3")
                    valid_input_for_player_one = False

            val = tic.place_marker(player_one_symbol, player_one_row_val, player_one_col_val)
            if val[1] == True and val[0]=="game_won":
                print("Player One wins")
                valid_input_for_start = True
                break
            elif val[1] == True and val[0]=='game_drawn':
                print("The game is drawn")
                valid_input_for_start = True
                break
            print("Player Two Input now ")
            valid_input_for_player_two = False
            while valid_input_for_player_two == False:
                try:
                    player_two_row_val = int(input("Enter row : "))
                    player_two_col_val = int(input("Enter column : "))

                    if (player_two_row_val > 3 or player_two_row_val < 0) and (
                            player_two_col_val > 3 or player_two_col_val < 0):
                        print("Enter a number between 1 to 3")
                        valid_input_for_player_two = False
                    else:
                        if tic.is_place_taken(player_two_row_val, player_two_col_val) == True:
                            print("This position is already filled . Choose some other row and column value")
                            valid_input_for_player_two = False
                        else:
                            valid_input_for_player_two = True
                            # if tic.is_place_taken(player_one_row_val,player_one_col_val)==False:
                            #     valid_input=True


                except:
                    print("Enter a number between 1 to 3")
                    valid_input_for_player_two = False

            val = tic.place_marker(player_two_symbol, player_two_row_val, player_two_col_val)
            if val[1] == True and val[0]=='game_won':
                print("Player Two wins")
                valid_input_for_start = True
                break
            elif val[1] == True and val[0]=='game_drawn':
                print("The game is drawn")
                valid_input_for_start = True
                break


    else:
        valid_input_for_start = False
        print("Enter a valid input")

