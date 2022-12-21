# 2022-12-02, day 2

def puzzles():
    # part 1
    # calculate rock-paper-scissors total score
    # A/X = rock, B/Y = paper, C/Z = scissors
    # score => rock=1, paper=2, scissors=3, 

    input_file = open("advent-of-code-2022/inputs/day_2_input.txt", "r")
    input_data = input_file.read()

    # rounds separated by '\n'
    round_list = input_data.split("\n")

    total_score = 0

    for round in round_list:
        if len(round) != 3:
            continue

        opponent_shape = round[0]
        my_shape = round[2]
        
        total_score = total_score + calculate_round_score_part_1(opponent_shape, my_shape)

    print("part 1 total score: ", total_score)

    # part 2
    # X,Y,Z = you need to lose,draw,win
    # calculate new total score (have to figure out which shape to pick)


# helper to calculate score each round (for clealiness)
def calculate_round_score_part_1(opponent_shape, my_shape):
    score = 0

    if my_shape == 'X':
        # rock
        score = score + 1

        if opponent_shape == 'A':
            # rock, draw
            score = score + 3
        elif opponent_shape == 'B':
            # paper, opp wins
            score = score + 0
        elif opponent_shape == 'C':
            # scissors, I win
            score = score + 6
        else:
            print("unrecognized opponent shape")

    elif my_shape == 'Y':
        # paper
        score = score + 2

        if opponent_shape == 'A':
            # rock, I win
            score = score + 6
        elif opponent_shape == 'B':
            # paper, draw
            score = score + 3
        elif opponent_shape == 'C':
            # scissors, opp wins
            score = score + 0
        else:
            print("unrecognized opponent shape")

    elif my_shape == 'Z':
        # scissors
        score = score + 3

        if opponent_shape == 'A':
            # rock, opp wins
            score = score + 0
        elif opponent_shape == 'B':
            # paper, I win
            score = score + 6
        elif opponent_shape == 'C':
            # scissors, draw
            score = score + 3
        else:
            print("unrecognized opponent shape")
    
    else:
        print("unrecognized player shape")

    return score

# helper to calculate score each round (for part 2)
def calculate_round_score_part_2(opponent_shape, round_outcome):
    score = 0

if __name__ == "__main__":
    puzzles()

