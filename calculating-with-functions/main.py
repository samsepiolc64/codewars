# Press Shift+F10 to execute it or replace it with your code.

def zero(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 0)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 0)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 0)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 0)
    else:
        return 0
def one(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 1)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 1)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 1)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 1)
    else:
        return 1
def two(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 2)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 2)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 2)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 2)
    else:
        return 2
def three(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 3)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 3)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 3)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 3)
    else:
        return 3
def four(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 4)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 4)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 4)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 4)
    else:
        return 4
def five(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 5)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 5)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 5)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 5)
    else:
        return 5
def six(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 6)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 6)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 6)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 6)
    else:
        return 6
def seven(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 7)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 7)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 7)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 7)
    else:
        return 7
def eight(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 8)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 8)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 8)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 8)
    else:
        return 8
def nine(*arg): #your code here
    if arg:
        if arg[0][0] == 'times': return times(arg[0][1][0], 9)
        if arg[0][0] == 'plus': return plus(arg[0][1][0], 9)
        if arg[0][0] == 'minus': return minus(arg[0][1][0], 9)
        if arg[0][0] == 'divided_by': return divided_by(arg[0][1][0], 9)
    else:
        return 9

def plus(*args): #your code here
    if len(args) == 1:
        return 'plus', args
    else:
        return args[0] + args[1]
def minus(*args): #your code here
    if len(args) == 1:
        return 'minus', args
    else:
        return args[1] - args[0]
def times(*args): #your code here
    if len(args) == 1:
        return 'times', args
    else:
        return args[0]*args[1]
def divided_by(*args): #your code here
    if len(args) == 1:
        return 'divided_by', args
    else:
        return int(args[1]/args[0])

if __name__ == '__main__':
    x = six(divided_by(two()))  # must return 35
    # four(plus(nine()))  # must return 13
    # eight(minus(three()))  # must return 5
    # six(divided_by(two()))  # must return 3
    # print(f'odp:{opr}')
    print(x)