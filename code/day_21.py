# 2022-12-21, day 21

import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, '../input/day_21_input.txt')

monkeys = {}    # global for easy access by puzzles() and recursive function

def puzzles():
    # part 1
    # find what 'root' monkey yells

    input_file = open(filename, "r")
    input_data = input_file.read()

    # monkey info separated by newline
    monkey_data = input_data.split('\n')

    # store monkeys in dict as (name: Monkey)
    for monkey_info in monkey_data:
        m = monkey_info.split()
        name = m[0].replace(':', '')
        m.pop(0)
        monkey = Monkey(name, m)
        monkeys[name] = monkey

    root_number = find_output_for_monkey('root')
    print(f'\'root\' yells: {root_number}')

    # part 2
    # find what 'humn' has to yell in order for 'root's two numbers to be equal
    root = monkeys['root']
    humn_num = find_number_for_humn(root.name)
    print(f'\'humn\' needs to yell: {humn_num}')


# recursive helper to find the number a given monkey ends up yelling
def find_output_for_monkey(monkey_name, part=1):
    # either
    # the monkey just yells a number    
    monkey = monkeys[monkey_name]
    if monkey.has_number():
        return monkey.number
    
    # or they are waiting for two other monkeys to yell an operation result
    n1 = find_output_for_monkey(monkey.monkey_1)
    n2 = find_output_for_monkey(monkey.monkey_2)

    op = monkey.operation
    if op == '+':
        return (n1 + n2)
    if op == '-':
        return (n1 - n2)
    if op == '*':
        return (n1 * n2)
    if op == '/':
        return (n1 / n2)


# recursive helper to find the number 'humn' should yell such that
# the two monkeys 'root' is waiting for yell the same number
#   needed_output_for_current_monkey = None by default, 
#   indicating it's the first call of the function, 
#   otherwise this function will recursively call with that set to an integer
def find_number_for_humn(monkey_name, needed_output_for_current_monkey=None):
    if monkey_name == 'humn':
        return needed_output_for_current_monkey
    
    monkey = monkeys[monkey_name]
    monkey_1 = monkeys[monkey.monkey_1]
    monkey_2 = monkeys[monkey.monkey_2]

    if needed_output_for_current_monkey == None:    # monkey is 'root'
        # figure out which doesn't rely upon 'humn',
        # and pass that as needed_output with other's children
        if relies_on_humn(monkey_1.name):
            cv = find_output_for_monkey(monkey_2.name)
            return find_number_for_humn(monkey_1.name, cv)
        else:
            cv = find_output_for_monkey(monkey_1.name)
            return find_number_for_humn(monkey_2.name, cv)
    
    op = monkey.operation
    # monkey_out = m1_out [op] m2_out

    # if monkey isn't 'root', slightly more complicated
    if relies_on_humn(monkey_1.name):
        # monkey_1 relies on 'humn', therefore, needed value from monkey_1 is
        #   op=+    monkey_out - m2_out = m1_out
        #   op=-    monkey_out + m2_out = m1_out
        #   op=*    monkey_out / m2_out = m1_out
        #   op=/    monkey_out * m2_out = m1_out

        monkey_1_output = None
        monkey_2_output = find_output_for_monkey(monkey_2.name) # doesn't rely on humn

        if op == '+':
            monkey_1_output = needed_output_for_current_monkey - monkey_2_output
        if op == '-':
            monkey_1_output = needed_output_for_current_monkey + monkey_2_output
        if op == '*':
            monkey_1_output = needed_output_for_current_monkey / monkey_2_output
        if op == '/':
            monkey_1_output = needed_output_for_current_monkey * monkey_2_output
        
        return find_number_for_humn(monkey_1.name, monkey_1_output)
    
    if relies_on_humn(monkey_2.name):
        # monkey_2 relies on 'humn', therefore, needed value from monkey_2 is
        #   op=+    monkey_out - m1_out = m2_out
        #   op=-    -1*(monkey_out - m1_out) = m2_out
        #   op=*    monkey_out / m1_out = m2_out
        #   op=/    m1_out / monkey_out = m2_out

        monkey_1_output = find_output_for_monkey(monkey_1.name) # doesn't rely on humn
        monkey_2_output = None

        if op == '+':
            monkey_2_output = needed_output_for_current_monkey - monkey_1_output
        if op == '-':
            monkey_2_output = -1*(needed_output_for_current_monkey - monkey_1_output)
        if op == '*':
            monkey_2_output = needed_output_for_current_monkey / monkey_1_output
        if op == '/':
            monkey_2_output = monkey_1_output / needed_output_for_current_monkey
        
        return find_number_for_humn(monkey_2.name, monkey_2_output)


# returns True if 'humn' provides a number for 'monkey_name', else False
def relies_on_humn(monkey_name):
    if monkey_name == 'humn':
        return True
    if monkey_name == None:
        return False
    
    monkey = monkeys[monkey_name]
    return (relies_on_humn(monkey.monkey_1) or relies_on_humn(monkey.monkey_2))


# helper class to keep track of monkeys
class Monkey:
    def __init__(self, name, rest_of_raw_info):
        # rest_of_raw_info is a list of strings from a single line from the input file
        # except for the monkey's name (which is provided separately)
        self.name = name
        self.number = None
        self.monkey_1 = None
        self.monkey_2 = None
        self.operation = None

        if len(rest_of_raw_info) == 1:
            self.number = int(rest_of_raw_info[0])
        
        else:
            self.monkey_1 = rest_of_raw_info[0]
            self.operation = rest_of_raw_info[1]
            self.monkey_2 = rest_of_raw_info[2]
    
    def has_number(self):
        if self.number:
            return True
        return False


if __name__ == "__main__":
    puzzles()

