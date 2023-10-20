from csv import reader
import webbrowser

output = open('top_20_popular_bookks.txt', 'w')
Count_taken_book = [[0,0]]*10000
TOP_20 = [[0,0]]*20
COUNT = [0]
k_str = 1
count = 0
num = 1

with open('books.csv',  'r', encoding= 'windows-1251') as csvFile:
    table = reader(csvFile, delimiter=';')
    table1 = list(table)

    for row in table1[1:]:
        Count_taken_book[k_str] = [k_str, int(f'{row[8]}')]
        k_str += 1

    Count_taken_book.sort(key=lambda x: x[1], reverse=True)

    for i in range(20):
        TOP_20[i] = [[Count_taken_book[i][0]],[Count_taken_book[i][1]]]

    print(TOP_20)

    output.write(f'TOP-20 popular books \n')
    for j in range(20):
        for ROW in table1[1:]:
            count += 1
            if count in TOP_20[j][0]:
                print(TOP_20[j][0], count)
                output.write(str(num) + ') ' + f'Название книги: {ROW[1]}. Автор: {ROW[3]}. Кол-во выдач: {ROW[8]} \n')
        count = 0
        num += 1


output.close()
webbrowser.open("top_20_popular_bookks.txt")   # Открывает файл top_20_popular_bookks.txt на рабочем столе (приложение блокнот)