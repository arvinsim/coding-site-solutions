# https://www.hackerrank.com/challenges/py-introduction-to-sets
# Python 2

# N = int('10')
# heights_of_plants = '161 182 161 154 176 170 167 171 170 174'
N  = int(raw_input())
heights_of_plants = raw_input()

height_set = set([int(x) for x in heights_of_plants.split(' ')])
average = reduce(lambda x, y: x + y, height_set) / float(len(height_set))
print(average)
