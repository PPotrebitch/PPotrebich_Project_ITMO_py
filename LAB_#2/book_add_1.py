from csv import reader
import webbrowser

output = open('All_teg.txt', 'w')
ALLteg = ""
allteg = []
UniqueTegs = []


with open('books.csv',  'r', encoding= 'windows-1251') as csvFile:
    table = reader(csvFile, delimiter=';')
    table1 = list(table)

    for row in table1[1:]:
        ALLteg += f'{row[12]}'
    allteg += ALLteg.split('#')

    for i in range(len(allteg)):
        if allteg[i] not in UniqueTegs:
            UniqueTegs += [allteg[i]]

    output.write(f'Уникальные теги \n')

    for j in range(len(UniqueTegs)):
         print(11)
         output.write(f'{UniqueTegs[j]}\n')

output.close()
webbrowser.open("All_teg.txt")