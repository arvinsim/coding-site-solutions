# https://www.hackerrank.com/challenges/ctci-ransom-note
# Python 3

def create_word_dictionary(word_list):
    word_dictionary = {}
    for word in word_list:
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1
    return word_dictionary

def ransom_note(magazine, ransom):
    word_dictionary = create_word_dictionary(magazine)
    for word in ransom:
        if word not in word_dictionary:
            return False
        word_dictionary[word] -= 1
        if word_dictionary[word] < 0:
            return False
    return True
    
m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')

# Expected Output "No"
# m = 15
# n = 17
# magazine = 'o l x imjaw bee khmla v o v o imjaw l khmla imjaw x'.split(' ')
# ransom = 'imjaw l khmla x imjaw o l l o khmla v bee o o imjaw imjaw o'.split(' ')

answer = ransom_note(magazine, ransom)

if(answer):
    print("Yes")
else:
    print("No")     