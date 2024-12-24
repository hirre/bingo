import timeit
import bingo_functions as bf

    
if __name__ == "__main__":
    print("Bingo Game\n")
    
    nr_of_boards = 10000
    boards = []
    start_time = timeit.default_timer()
    boards = bf.generate_boards(nr_of_boards)
    elapsed_time = timeit.default_timer() - start_time
    
    print(f"Time taken to generate {nr_of_boards} boards: {elapsed_time:.2f} seconds")
    print(f"Unique boards generated: {len(boards)}")