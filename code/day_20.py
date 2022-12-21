# 2022-12-20, day 20

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../input/day_20_input.txt')


def puzzles(part=1):
    # part 1
    # "mix" input file:
    #   in the original order that they appear in the input,
    #   move each number a number of spaces in the list according to its value
    
    input_file = open(filename, "r")
    input_data = input_file.read()

    # numbers are separated by newline
    input_list = input_data.split("\n")
    mix_list = []
    mix_copy = []   # not touched after initial vals, just used to get numbers in right order

    for input in input_list:
        # for each element of the input, turn the value into an integer
        # and associate with it whether it's been "mixed" yet (all start False)
        n = number(int(input))
        if part == 2:
            # for part 2, each number is multiplied by this key
            n.value = 811589153 * n.value
        mix_list.append(n)
        mix_copy.append(n)


    rounds = 1
    if part == 2:
        # for part 2, the mixing is applied 10 times
        rounds = 10
    
    for _ in range(rounds):
        for n in mix_copy:
            # for each number in the copy (stays in order)
            # get its index, remove it, set isMixed = True,
            # and re-insert it at its current index plus its value
            index = mix_list.index(n)
            new_index = (index + n.value) % (len(mix_list)-1)
            mix_list.pop(index)

            mix_list.insert(new_index, n)

    # this is definitely not a good way of doing this,
    # but given I decided to use objects I think it's easiest right now
    zero_index = 0
    for n in mix_list:
        if n.value == 0:
            zero_index = mix_list.index(n)
    
    sum = 0
    for i in [1000, 2000, 3000]:
        sum += mix_list[ (zero_index + i) % (len(mix_list)-1) ].value
    
    print(f'sum of the 1000th, 2000th, and 3000th numbers after 0 is  {sum}')

# helper class to keep track of mixing of numbers
#   (probably not the best/most clever way of doing this)
class number:
    def __init__(self, v):
        self.value = v


if __name__ == "__main__":
    puzzles(2)

