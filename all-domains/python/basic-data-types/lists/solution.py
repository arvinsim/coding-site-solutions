#!/user/bin/env python
#https://www.hackerrank.com/challenges/python-lists

def get_commands():
    # return [
    #     'insert 0 5',
    #     'insert 1 10',
    #     'insert 0 6',
    #     'print',
    #     'remove 6',
    #     'append 9',
    #     'append 1',
    #     'sort',
    #     'print',
    #     'pop',
    #     'reverse',
    #     'print'
    # ]
    number_of_commands = int(raw_input())
    commands = []
    for foo in xrange(number_of_commands):
        commands.append(raw_input())
    return commands

def parse_command(command):
    return command.split(' ')

def execute_command(command, worked_on_list):
    if command[0] == 'insert':
        i = int(command[1])
        e = int(command[2])
        worked_on_list.insert(i, e)
    elif command[0] == 'print':
        print(worked_on_list)
    elif command[0] == 'remove':
        e = int(command[1])
        worked_on_list.remove(e)
    elif command[0] == 'append':
        e = int(command[1])
        worked_on_list.append(e)
    elif command[0] == 'sort':
        worked_on_list.sort()
    elif command[0] == 'pop':
        worked_on_list.pop()
    elif command[0] == 'reverse':
        worked_on_list.reverse()
    return worked_on_list

worked_on_list = []
for command in get_commands():
    parsed_command = parse_command(command)
    worked_on_list = execute_command(parsed_command, worked_on_list)
