import timeit
import bingo_functions as bf
from bingo_functions import BingoCard, BingoBoard, PrizeDistribution

    
if __name__ == "__main__":
    print("Bingo Game\n")
    
    prize_distribution = PrizeDistribution()
    
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
    
    tup = bf.generate_game_cards(10000, prize_distribution)
    
    print(f"Cards {len(tup[0])}")