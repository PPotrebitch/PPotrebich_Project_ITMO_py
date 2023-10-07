END = '\u001b[0m'
WHITE = '\u001b[47m'
BLACK  = '\u001b[40m'
BAZA = [[22, 2, 0, 2, 22]] * 9
print(len(BAZA))
for j in range(8):
    baza = [BAZA[j][0]-3, BAZA[j][1]+2, BAZA[j][2]+2, BAZA[j][3]+2, BAZA[j][4]-3]
    BAZA[j+1] = baza
print(BAZA)

for i in range(len(BAZA)):
    print(f'{WHITE}{" " *BAZA[i][0]}{BLACK}{" " * BAZA[i][1]}{WHITE}{" " *BAZA[i][2]}{BLACK}{" " * BAZA[i][3]}{WHITE}{" " *BAZA[i][4]}{END}')
