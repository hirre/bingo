import timeit
from bingo_module import PrizeDistribution, BingoCardGenerator

if __name__ == "__main__":
    print("\nBingo Game Card Generator\n")
    
    prize_distribution = PrizeDistribution()
    bcg = BingoCardGenerator()
    nr_of_cards = 10000
    win_probability = 0.0

    # Add prizes and their probabilities
    prize_distribution.add_prize(10, 0.001)
    prize_distribution.add_prize(200, 0.0002)
    prize_distribution.add_prize(500, 0.0002)
    prize_distribution.add_prize(1000, 0.0001)
    prize_distribution.add_prize(15000, 0.00002)
    prize_distribution.add_prize(100000, 0.00001)
    prize_distribution.add_prize(150000, 0.000002)
    prize_distribution.add_prize(250000, 0.000001)
    prize_distribution.add_prize(350000, 0.0000001)
    prize_distribution.add_prize(500000, 0.00000001)
    prize_distribution.add_prize(700000, 0.00000001)
    prize_distribution.add_prize(850000, 0.000000001)
    prize_distribution.add_prize(1000000, 0.000000001)
    prize_distribution.add_prize(2000000, 0.0000000001)
    prize_distribution.add_prize(5000000, 0.00000000001)
  
    start_time = timeit.default_timer()
    
    # Tuple of a list of BingoCard objects and a dictionary of prize combos
    # The data can be used for different purposes, such as storing it in a database for different usages...
    tup = bcg.generate_game_cards(nr_of_cards, prize_distribution)

    elapsed_time = timeit.default_timer() - start_time
    
    print(f"Time taken to generate {len(tup[0])} boards: {elapsed_time:.2f} seconds")
    # If lottery tickets cost more than expected prize value, the game is profitable
    print(f"Expected prize value of the game: {prize_distribution.expected_value()}")
    # Probability of not winning anything should be close to 1
    print(f"Probability of not winning anything: {prize_distribution.get_probability(0):.6f}")
    
    print("\nPrize | # Winning cards | Winning combo\n")

    for prize in tup[1].keys():
        print(f"{prize}\t| {int(nr_of_cards*prize_distribution.get_probability(prize))}\t| {tup[1][prize]}")
        
    print()