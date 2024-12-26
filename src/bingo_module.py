from hashlib import sha256
import random
import uuid          

# Bingo board with 3*5x5 grid
class BingoBoard:
    __board_data: list[list[int]]
    __checksum = ""
    
    def __init__(self):
        self.__board_data = self.__generate_board_data()
        self.__checksum = sha256(str(self.__board_data).encode()).hexdigest()
            
    # Generate a 3*5 x 5 board, with a unique number per cell and board
    def __generate_board_data(self) -> list[list[int]]:
        bColumn = self.__generate_random_numbers(1, 16)
        iColumn = self.__generate_random_numbers(17, 32)
        nColumn = self.__generate_random_numbers(32, 47)
        gColumn = self.__generate_random_numbers(48, 70)
        oColumn = self.__generate_random_numbers(71, 99)      
        
        return [bColumn, iColumn, nColumn, gColumn, oColumn]
    
    def __generate_random_numbers(self, min_number: int, max_number: int) -> list[int]:
        if (max_number - min_number) < 15:
            raise ValueError("The difference between max and min number should be at least 15")
        
        arr: list[int] = [0] * 15
        used_numbers: dict[int, bool] = {}
        
        for x in range(len(arr)):      
            not_used = True
            
            while not_used:
                rand_nr = random.randint(min_number, max_number)
                
                if rand_nr not in used_numbers:
                    arr[x] = (rand_nr)
                    used_numbers[rand_nr] = True
                    not_used = False
        return arr
        
    def get_checksum(self) -> str:
        return self.__checksum
    
    def get_board_data(self) -> list[list[int]]:
        return self.__board_data
    
# Bingo card with 5 boards
class BingoCard:
    __boards: list[BingoBoard] = []
    __id: uuid.UUID       
        
    def __init__(self, boards: list[BingoBoard]):
        self.__boards = boards
        self.__id = uuid.uuid4()
    
    def get_boards(self) -> list[BingoBoard]:
        return self.__boards
    
    def get_id(self) -> uuid.UUID:
        return self.__id
  
# Prize distribution for the lottery           
class PrizeDistribution: 
    __prize_distribution: dict[int, float] = { }
    
    # Calculate expected value of the game 
    def expected_value(self) -> float:
        expected_value = 0.0
        
        for prize in self.__prize_distribution.keys():
            expected_value += prize * self.__prize_distribution[prize]
        
        return expected_value
      
    def add_prize(self, prize: int, probability: float) -> None:
        
        if prize == 0:
            raise ValueError("Prize can't be 0")
        
        self.__prize_distribution[prize] = probability
        
        win_probability_sum = 0.0
        
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
    
# Generates bingo cards for the lottery
class BingoCardGenerator:
    
    # Generate a unique board    
    def __get_unique_board(self, checksum_dict: dict[str, bool]) -> BingoBoard:
        not_found = True
        while not_found:
            board = BingoBoard()
            checksum = board.get_checksum()
            
            if checksum not in checksum_dict:
                checksum_dict[checksum] = True
                not_found = False
                return board
            
        return BingoBoard() # Should never reach this point

    # Generate game cards
    def generate_game_cards(self, nr_of_cards: int, prize_distribution: PrizeDistribution) -> tuple[list[BingoCard], dict[int,list[int]]]:
        checksum_dict: dict[str, bool] = {}
        all_cards = []
        win_cards = []
        prize_combo_dict: dict[int, list[int]] = {}
        winning_row_index = 0
        round_robin = 0

        # Generate winning cards
        for prize in prize_distribution.get_prizes():
            if prize == 0:
                continue
            
            winning_board = self.__get_unique_board(checksum_dict)
            
            winning_board_data = winning_board.get_board_data()
            
            # Select the winning combination from lowest to highest prize (ascending order)
            winning_combo = [
                        winning_board_data[0][winning_row_index], 
                        winning_board_data[1][winning_row_index], 
                        winning_board_data[2][winning_row_index], 
                        winning_board_data[3][winning_row_index],
                        winning_board_data[4][winning_row_index]
                    ]
            
            nr_of_winning_cards = int(nr_of_cards * prize_distribution.get_probability(prize))
            
            # Store the winning combination for the prize
            prize_combo_dict[prize] = winning_combo if nr_of_winning_cards != 0 else []
                    
            # Store the prize board for the lottery in a board card with other random boards
            # Create nr_of_cards * probability of winning cards
            for x in range(nr_of_winning_cards):
                card_boards = [self.__get_unique_board(checksum_dict) for _ in range(5)]  # Create 5 instances of BingoBoard
                card_boards[round_robin] = winning_board # insert winning board at round_robin index
                
                if round_robin + 1 > 4:
                    round_robin = 0
                else:
                    round_robin += 1

                win_cards.append(BingoCard(card_boards))
                
            winning_row_index += 1
                    
        # Create loose cards
        for x in range(nr_of_cards - len(win_cards)):
            all_cards.append(BingoCard([self.__get_unique_board(checksum_dict) for _ in range(5)]))
            
        # Add winning cards to all cards
        all_cards.extend(win_cards)

        # Shuffle the cards
        random.shuffle(all_cards)
            
        return (all_cards, prize_combo_dict)