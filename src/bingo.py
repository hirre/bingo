import timeit
from bingo_module import PrizeDistribution, BingoCardGenerator

if __name__ == "__main__":
    print("\nBingo Game Card Generator\n")
    
    prize_distribution = PrizeDistribution()
    bcg = BingoCardGenerator()
    nr_of_cards = 10000

    # Add prizes and their probabilities
    prize_distribution.add_prize(500, 0.0002)
    prize_distribution.add_prize(1000, 0.0001)
    prize_distribution.add_prize(15000, 0.00002)
    prize_distribution.add_prize(150000, 0.00001)
    prize_distribution.add_prize(1000000, 0.000001)
    
    start_time = timeit.default_timer()
    
    # Tuple of list of BingoCard objects and dictionary of prize combos
    # The data can be used for different purposes, such as storing in a database etc...
    tup = bcg.generate_game_cards(nr_of_cards, prize_distribution)

    elapsed_time = timeit.default_timer() - start_time
    
    print(f"Time taken to generate {len(tup[0])} boards: {elapsed_time:.2f} seconds")
    
    print("\nPrize --> winning combo:\n")

    for prize in tup[1].keys():
        print(f"{prize} --> {tup[1][prize]}")
        
    print()