from csv import reader

K = 0
with open("books.csv", 'r') as csvfile:
    table = reader(csvfile, delimiter=';')
    for row in table:
        #print(row[1])
        if len(row[1]) > 30:
            K += 1
print(K)