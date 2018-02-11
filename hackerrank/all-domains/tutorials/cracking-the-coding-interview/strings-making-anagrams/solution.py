# https://www.hackerrank.com/challenges/ctci-making-anagrams
# Python 3

def delete_char_at(s, i):
    return s[:i] + s[i+1:]

def number_needed(a, b):
    counter = 0
    loop_over, reference = (a, b) if len(a) > len(b) else (b, a)

    for character in loop_over:
        index = reference.find(character)
        if index == -1:
            counter += 1
        else:
            # Remove the character from the reference string
            reference = delete_char_at(reference, index)

    # If there are remaining characters in reference string, add those to count
    counter += len(reference)

    return counter

a = input().strip()
b = input().strip()

# TEST answer should be 3
# betas and beast are anagrams...so the trailing bz and a should be removed
# a = 'betasbz'
# b = 'beasta'

print(number_needed(a, b))
