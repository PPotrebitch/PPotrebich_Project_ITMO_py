RED = '\u001b[41m'
WHITE = '\u001b[47m'
BLUE = '\u001b[44m'
END = '\u001b[0m'
COLOR_BAZA = [RED, WHITE, BLUE]
FLAG_THA = [0, 1, 2, 2, 1, 0]
for i in range(len(FLAG_THA)):
    print(f'{COLOR_BAZA[FLAG_THA[i]]}{" " *24}{END}')
