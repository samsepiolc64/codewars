def program_input(prog_line=''):
    for inp in iter(input, prog_line):
        yield inp.split()

def program_do(prog):
    A,B,C = 0, 0, 0
    for i in range(0,len(prog)):
        if prog[i][0] == 'MOV':
            if prog[i][2].isdigit():
                if prog[i][1] == 'A':
                    A = int(prog[i][2])
                else:
                    B = int(prog[i][2])
            elif prog[i][1] == 'A':
                A = B
            else:
                B = A
        if prog[i][0] == 'ADD':
            C = A + B
        if prog[i][0] == 'MUL':
            C = A * B
        if prog[i][0] == 'JMP':
            i = 3
        if prog[i][0] == 'JNP' and C != 0:
            i = 3

    print(C)

program = list(program_input())
program_do(program)

