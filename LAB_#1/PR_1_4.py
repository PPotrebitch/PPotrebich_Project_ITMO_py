f = open('lab_1.txt', 'r')
RED = '\u001b[41m'
BLUE = '\u001b[44m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
list = []
l = [line.rstrip() for line in f]

for n in l:
    if float(n) != 5.0 and float(n) >= 0.0:
        list.append(float(n))
k = len(list)
more_5, less_5 = 0, 0
for i in list:
    if float(i) > 5.0:
        more_5 += 1
    elif float(i) < 5.0:
        less_5 += 1
f.close()
print(list)
print('more_5 = ', more_5, 'less_5 = ', less_5, 'k = ', k)
pr_more_5 = (more_5*100)/k
pr_less_5 = (less_5*100)/k
print('pr_more_5 = ', pr_more_5, '%', f'{BLUE}{" " * int(pr_more_5 / 10)}{WHITE}{" " *abs(10 - int(pr_more_5 / 10))}{END}')
print('pr_less_5 = ', pr_less_5,'%' , f'{RED}{" " * int(pr_less_5 / 10)}{WHITE}{" " *abs(10 - int(pr_less_5 / 10))}{END}')
