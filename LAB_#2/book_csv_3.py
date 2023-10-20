from csv import reader
import random
import webbrowser

output = open('result_random_list.txt', 'w')
k_str = 0
box_k_str = []
num = 0
count, index = 0, 1
c = 0

def RANDOM(FROM, TO):
        for  _ in range(20):
            n = random.randint(FROM, TO)
            box_k_str.append(n)
        return box_k_str

with open('books.csv',  'r', encoding= 'windows-1251') as csvFile:
    table = reader(csvFile, delimiter=';')
    table1 = list(table)

    for i in table1[1:]:
        k_str += 1

    RANDOM(1, k_str)

    for j in range(len(box_k_str)):
        for row in table1:
            count += 1
            if count == box_k_str[num]:
                output.write(str(index) + ') ' + f'Автор: {row[3]}. Название книги: {row[1]}. Год: {row[6][6:10]} \n')
        count = 0
        num += 1
        index += 1

#print(c, k_str)
output.close()
webbrowser.open("result_random_list.txt")   # Открывает файл result_random_list.txt на рабочем столе (приложение блокнот)