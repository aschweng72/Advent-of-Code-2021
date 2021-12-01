# Advent of Code Day 1 challenge

# part 1: find how many measurements are larger than the previous measurement

text_file = open('day1.txt')
depth_list = text_file.readlines()
depth_list = [int(i.strip('\n')) for i in depth_list]

# comparing each set of two items in the list, increasing the counter by 1 if greater
increases = 0
for a,b in zip(depth_list, depth_list[1:]):
    #print(f'a: {a}, b: {b}, {b>a}')
    if a < b:
        increases +=1

print(f'Part one answer is: {increases}')

# part 2: compare the sum of each set of three numbers with the sum of the next set of three numbers

increases = 0
# below works because the only difference between the two sets of three is a and b
for a,b in zip(depth_list, depth_list[3:]):
    if b>a:
        increases += 1

print(f'Part two answer is: {increases}')
