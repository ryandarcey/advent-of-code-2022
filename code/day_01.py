# 2022-12-01, day 1

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../input/day_01_input.txt')


def puzzles():
    # part 1
    # find the largest sum of values from the groups of values in
    #   'day_1_puzzle_1_input.txt' -> groups of values separated by blank line
    
    input_file = open(filename, "r")
    input_data = input_file.read()

    # groups of values are separated by blank line, aka two newlines
    # this gets a list of strings as ['XXXX\nXXXX\nXXXX..', ...]
    input_list = input_data.split("\n\n")

    sums_list = []

    # for each group of values, split into values, convert to ints, get their sum
    for group_of_vals in input_list:
        vals_list = [eval(i) for i in group_of_vals.split('\n')]
        sums_list.append(sum(vals_list))
    
    # get max sum of groups
    print("highest num calories: ", max(sums_list))

    # part 2
    # find total of top 3 elves
    
    sums_list.sort()
    print("total of top 3: ", sum(sums_list[-3:]))


if __name__ == "__main__":
    puzzles()

