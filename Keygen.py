import random

def key_gen():

    Symbol = "0123456789QWERTYUIOPASDFGHJKLZXCVBNM"
    number = "0123456789"
    A = ''
    B = ''
    C = ''
    a, b, c = 0, 0, 0
    text = ''

    for i in range(5):
        a1 = random.randint(0, len(Symbol)-1)
        vec_k_a = random.randint(1, 10)
        if (Symbol[a1] in number) == False:
            a += vec_k_a
        elif (Symbol[a1] in number) == True:
            a += int(Symbol[a1])
        A += Symbol[a1]

    for j in range(4):
        b1 = random.randint(0, len(Symbol)-1)
        vec_k_b = random.randint(1, 10)
        if (Symbol[b1] in number) == False:
            b += vec_k_b
        elif (Symbol[b1] in number) == True:
            b += int(Symbol[b1])
        B += Symbol[b1]

    for k in range(4):
        c1 = random.randint(0, len(Symbol)-1)
        vec_k_c = random.randint(1, 10)
        if (Symbol[c1] in number) == False:
            c += vec_k_c
        elif (Symbol[c1] in number) == True:
            c += int(Symbol[c1])
        C += Symbol[c1]

    if (15<= a <= 34) or (15<= b <= 34) or (15<= c <= 34):
        return f'{A}-{B}-{C}'
    else:
        key_gen()