# https://www.hackerrank.com/challenges/symmetric-difference
# Python 2

# M = '4'
# M_integers = '2 4 5 9'
# N = '4'
# N_integers = '2 4 11 12'
M = raw_input()
M_integers = raw_input()
N = raw_input()
N_integers = raw_input()

def input_to_set(input):
    return set(map(lambda x: int(x), input.split(' ')))

M_set = input_to_set(M_integers)
N_set = input_to_set(N_integers)

intersection = M_set.intersection(N_set)
union = M_set.union(N_set)

output = set()
for item in union:
    if item not in intersection:
        output.add(item)

sorted_output = sorted(output)
for x in sorted_output:
    print(x)
