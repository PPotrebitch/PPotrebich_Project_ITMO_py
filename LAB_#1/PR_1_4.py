f = open('lab_1.txt', 'r')
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
list = []
l = [line.rstrip() for line in f]

for n in l:
    if float(n) != 5 and float(n) >= 0:
        list.append(float(n))
k = len(l)
b5, l5 = 0, 0
for i in l:
    if float(i) > 5.0:
        b5 += 1
    elif float(i) < 5.0:
        l5 += 1
f.close()
print(list)
print('b5 = ', b5, 'l5 = ', l5, 'k = ', k)
pr_b5 = (b5*100)/k
pr_l5 = (l5*100)/k

#print(10 - int(b5 / 10))
#print('pr_b5 = ', pr_b5, '%', 'pr_l5 = ', pr_l5, '%')
print('pr_b5 = ', pr_b5, '%', f'{BLUE}{" " * int(b5 / 10)}{WHITE}{" " *abs(10 - int(l5 / 10))}{END}')
print('pr_l5 = ', pr_l5,'%' , f'{RED}{" " * int(l5 / 10)}{WHITE}{" " *abs(10 - int(b5 / 10))}{END}')