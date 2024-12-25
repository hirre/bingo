import copy
import timeit
import bingo_functions as bf
import random

def generate_game_cards(nr_of_cards: int, prize_distribution: bf.PrizeDistribution) -> tuple[list[bf.BingoCard], dict[int,list[int]]]:
    loose_cards = []
    win_cards = []
    prize_dict: dict[int, list[int]] = {}
    row_index = 0
    round_robin = 0
    
    for prize in prize_distribution.get_prizes():
        if prize == 0:
            continue
        
        board = bf.generate_boards(1)[0]
        board_data = board.get_board_data()
        prize_row = [
                    board_data[0][row_index], 
                    board_data[1][row_index], 
                    board_data[2][row_index], 
                    board_data[3][row_index],
                    board_data[4][row_index]
                ]
        
        prize_dict[prize] = prize_row
                
        # Store the prize board for the lottery in a board card with other random boards
        # Create nr_of_cards * probability of winning rows copies of the board
        for x in range(int(nr_of_cards * prize_distribution.get_probability(prize))):
            copy_board = copy.deepcopy(board)
            card_boards = [bf.BingoBoard() for _ in range(5)]  # Create 5 instances of BingoBoard
            card_boards[round_robin] = copy_board # insert winning board at round_robin index
            
            if round_robin + 1 > 4:
                round_robin = 0
            else:
                round_robin += 1
                
            win_cards.append(bf.BingoCard(card_boards))
            
        row_index += 1
                
    for x in range(nr_of_cards - len(win_cards)):
        loose_cards.append(bf.BingoCard([bf.BingoBoard() for _ in range(5)]))
        
    loose_cards.extend(win_cards)
    
    # Shuffle the cards
    random.shuffle(loose_cards)
        
    return (loose_cards, prize_dict)
    
if __name__ == "__main__":
    print("Bingo Game\n")
    
    prize_distribution = bf.PrizeDistribution()
    
    prize_distribution.add_prize(500, 0.0002)
    prize_distribution.add_prize(1000, 0.0001)
    prize_distribution.add_prize(15000, 0.00002)
    prize_distribution.add_prize(150000, 0.00001)
    prize_distribution.add_prize(1000000, 0.000001)
    
    nr_of_cards = 10000
    
    #start_time = timeit.default_timer()
    #seed_boards = bf.generate_boards(nr_of_cards)
    #elapsed_time = timeit.default_timer() - start_time
    
    #print(f"Time taken to generate {nr_of_seed_boards} boards: {elapsed_time:.2f} seconds")
    #print(f"Unique boards generated: {len(seed_boards)}")
    
    tup = generate_game_cards(10000, prize_distribution)
    
    print(f"Cards {len(tup[0])}")