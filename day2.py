# Advent of Code Day 2 challenge

# Part 1: Calculate final horizontal location & depth, then multiply them

# import data, split into list of lists
text_file = open('day2.txt')
directions = text_file.readlines()
directions = [i.strip('\n') for i in directions]
directions = [i.split(' ') for i in directions]

# set counter for horizontal & depth
horizontal = 0
depth = 0

# run a for loop and count based on list[0] and list[1]
for i in directions:
    if i[0] == 'forward':
        horizontal += int(i[1])
    elif i[0] == 'up':
        depth -= int(i[1])
    elif i[0] == 'down':
        depth += int(i[1])

# multiply final counters together for the answer
print(f'The answer for Part 1 is {horizontal * depth}')

# reset our counters and add aim
horizontal = 0
depth = 0
aim = 0

# for loop a count based on instruction (list[0]) and value (list[1])
for i in directions:
    if i[0] == 'down':
        aim += int(i[1])
    elif i[0] == 'up':
        aim -= int(i[1])
    elif i[0] == 'forward':
        horizontal += int(i[1])
        depth += (aim * int(i[1]))

# multiple the new values together to get the answer
print(f'The answer for Part 2 is {horizontal * depth}')