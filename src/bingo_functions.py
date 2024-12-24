from hashlib import sha256
import random

# Generate board a 15 x 5, three separate  5x5 board grids with unique number per cell and column
def generate_board():
    bColumn = generate_random_numbers(1, 15)
    iColumn = generate_random_numbers(16, 30)
    nColumn = generate_random_numbers(31, 45)
    gColumn = generate_random_numbers(46, 60)
    oColumn = generate_random_numbers(61, 99)      
    
    return [bColumn, iColumn, nColumn, gColumn, oColumn]


def print_board(board):
    
    print("B\tI\tN\tG\tO\n")
    
    for x in range(15):
        print(board[0][x] , "\t", board[1][x] , "\t", board[2][x] , 
              "\t", board[3][x] , "\t", board[4][x])
        if (x+1) % 5 == 0:
            print("\n")
            
# TODO:  this might have a infinite loop if it can't find a unique number, 
# don't set a low max number in combination with a high array size
def generate_random_numbers(min_number, max_number):
    
    arr = [int] * 15
    used_numbers = {}
    
    for x in range(len(arr)):      
        not_used = True
        
        while not_used:
            rand_nr = random.randint(min_number, max_number)
            
            if rand_nr not in used_numbers:
                arr[x] = rand_nr
                used_numbers[rand_nr] = True
                not_used = False
    return arr


def generate_boards(nr_of_boards):
    checksum_dict = {}
    boards = []
    
    for x in range(nr_of_boards):
        not_found = True
        
        while not_found:
            board = generate_board()
            checksum = sha256(str(board).encode()).hexdigest()
            
            if checksum not in checksum_dict:
                checksum_dict[checksum] = True
                not_found = False
                boards.append(BingoBoard(board, checksum))
                
    return boards
            

class BingoBoard:
    board = []
    checksum = ""
    
    def __init__(self, board, checksum):
        self.board = board
        self.checksum = checksum
    
    def get_checksum(self):
        return self.checksum
    
    def get_board(self):
        return self.board
    
class BingoCard:
    boards = []       
        
    def __init__(self, boards):
        self.boards = boards
    
    def get_boards(self):
        return self.boards
        
    