import timeit
import bingo_functions as bf
import random

def generate_game_cards(nr_of_cards: int, seed_boards: list[bf.BingoBoard], 
                        prize_distribution: bf.PrizeDistribution) -> list[bf.BingoCard]:
    cards = []
    
    row_index = 0
    for prize in prize_distribution.get_prizes():
        if prize == 0:
            continue
        
        board = random.choice(seed_boards)
        prize_row = [
                    board.get_board_data()[0][row_index], 
                    board.get_board_data()[1][row_index], 
                    board.get_board_data()[2][row_index], 
                    board.get_board_data()[3][row_index],
                    board.get_board_data()[4][row_index]
                ]
        
        # Store the prize row for lottery
        # Create nr_of_cards * probability of winning rows copies of the board
        
    
        
        row_index += 1
        
        
    return cards
    
if __name__ == "__main__":
    print("Bingo Game\n")
    
    prize_distribution = bf.PrizeDistribution()
    
    prize_distribution.add_prize(500, 0.0002)
    prize_distribution.add_prize(1000, 0.0001)
    prize_distribution.add_prize(15000, 0.00002)
    prize_distribution.add_prize(150000, 0.00001)
    prize_distribution.add_prize(1000000, 0.000001)
    
    nr_of_seed_boards = 10000
    seed_boards = []
    
    #start_time = timeit.default_timer()
    seed_boards = bf.generate_boards(nr_of_seed_boards)
    #elapsed_time = timeit.default_timer() - start_time
    
    #print(f"Time taken to generate {nr_of_seed_boards} boards: {elapsed_time:.2f} seconds")
    #print(f"Unique boards generated: {len(seed_boards)}")
    
    generate_game_cards(1000000, seed_boards, prize_distribution)