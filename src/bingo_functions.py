from hashlib import sha256
import random


def generate_boards(nr_of_boards: int) -> list['BingoBoard']:
    checksum_dict: dict[str, bool] = {}
    boards = [BingoBoard]
    
    for x in range(nr_of_boards):
        not_found = True
        
        while not_found:
            board = BingoBoard()
            checksum = board.get_checksum()
            
            if checksum not in checksum_dict:
                checksum_dict[checksum] = True
                not_found = False
                boards.append(board)
                
    return boards
            

class BingoBoard:
    __board_data = [list[int]]
    __checksum = ""
    
    def __init__(self):
        self.__board_data = self.__generate_board_data()
        self.__checksum = sha256(str(self.__board_data).encode()).hexdigest()
            
    # Generate board a 15 x 5, three separate  5x5 board grids with unique number per cell and column
    def __generate_board_data(self) -> list[list[int]]:
        bColumn = self.__generate_random_numbers(1, 15)
        iColumn = self.__generate_random_numbers(16, 30)
        nColumn = self.__generate_random_numbers(31, 45)
        gColumn = self.__generate_random_numbers(46, 60)
        oColumn = self.__generate_random_numbers(61, 99)      
        
        return [bColumn, iColumn, nColumn, gColumn, oColumn]
    
    # TODO: this might have a infinite loop if it can't find a unique number, 
    # don't set a low max number in combination with a high array size
    def __generate_random_numbers(self, min_number: int, max_number: int) -> list[int]:
        
        arr = [int] * 15
        used_numbers: dict[int, bool] = {}
        
        for x in range(len(arr)):      
            not_used = True
            
            while not_used:
                rand_nr = random.randint(min_number, max_number)
                
                if rand_nr not in used_numbers:
                    arr[x] = rand_nr
                    used_numbers[rand_nr] = True
                    not_used = False
        return arr
        
    def get_checksum(self) -> str:
        return self.__checksum
    
    def get_board_data(self) -> list[list[int]]:
        return self.__board_data
    
    
class BingoCard:
    __boards = [BingoBoard]       
        
    def __init__(self, boards: list[BingoBoard]):
        self.__boards = boards
    
    def get_boards(self) -> list[BingoBoard]:
        return self.__boards
        
        
class PrizeDistribution: 
    __prize_distribution: dict[int, float] = { }
    
    def add_prize(self, prize: int, probability: list[int]) -> None:
        
        if prize == 0:
            raise ValueError("Prize can't be 0")
        
        self.__prize_distribution[prize] = probability
        
        win_probability_sum = 0
        
        # Calculate the probability of winning something
        for key in self.__prize_distribution:
            if key != 0:
                win_probability_sum += self.__prize_distribution[key]
                
        # 0 is the probability of not winning anything
        self.__prize_distribution[0] = 1 - win_probability_sum 
    
    def get_probability(self, prize: int) -> float:
        return self.__prize_distribution[prize]
    
    def get_prizes(self) -> list[int]:
        return sorted(self.__prize_distribution.keys())