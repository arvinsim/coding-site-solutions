# https://www.hackerrank.com/challenges/ctci-balanced-brackets
# Python 3

def match_brace(a, b):
    match = {
        '{': '}',
        '}': '{',
        '[': ']',
        ']': '[',
        '(': ')',
        ')': '(',
    }

    if match[a] == b:
        return True
    return False

def is_matched(expression):
    stack = []
    for character in expression:
        if character in ['{', '[', '(']:
            stack.append(character)
        elif character in ['}', ']', ')']:
            if len(stack) > 0:
                pop = stack.pop()
                if not match_brace(pop, character):
                    return False
            else:
                return False
    if len(stack) > 0:
        return False
    return True

# bracket_list = [
#     '{}',
#     '}([[{)[]))]{){}[',
#     '{]]{()}{])',
#     '(){}',
#     '{}{()}{{}}',
# ]
# for expression in bracket_list:
#     if is_matched(expression) == True:
#         print("YES")
#     else:
#         print("NO")

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
