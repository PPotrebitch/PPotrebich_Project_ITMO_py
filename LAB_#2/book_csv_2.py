from csv import reader
import webbrowser

flag = 0
output = open('result_find.txt', 'w')
search = input("Search for FIO: ")
with open('books.csv', 'r', encoding= 'windows-1251') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in list(table)[1:]:
        if float(row[7]) > 150.0:
            lower_case = row[4].lower()
            index = lower_case.find(search.lower())
            if index != -1:
                print(row[1])
                flag = 1
                output.write(f'ФИО автора: {row[4]}. Название книги: {row[1].lower()}. Цена за одну книгу: {row[7].lower()} рублей.\n')

    if flag == 0:
        print('Nothing found.')

output.close()
webbrowser.open("result_find.txt") # Открывает файл result_find.txt на рабочем столе (приложение блокнот)