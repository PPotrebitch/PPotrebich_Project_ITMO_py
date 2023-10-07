print(" "* 20, "y = 1/x")
print('Y' +'  ^')
for j in range(13):
    if j == 1:
        print(" 4 " + "|" + ' ' + "*")
    elif j == 6:
        print(" 2 " + "|" + ' '*3 + "*")
    elif j == 10:
        print(" 1 " + "|" + ' '*18 + "*")
    elif j == 11:
        print("0.5" + "|" + ' '*36 + "*")
    else:
        print("   " + "|")
print(" 0 "+"-"*50+"> X")
print(' 0.25' + " 0.5" + " "* 13 + "1" + " " * 17 + "2")