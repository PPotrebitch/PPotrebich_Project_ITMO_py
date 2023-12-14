# Лаба №4 "задача о рюзаке". Программист: студент 1 курса ИТМО  Потребич Пввел

baza = {'r': (3, 25), # Винтовка (riflle)
       'p': (2, 15), # Пистолет (Pistol)
       'a': (2, 15), # Боекомплект (ammo)
       'm':(2, 20), # Аптечка (Medkit)
       'i': (1, 5), # Ингалятор (inhaler)
       'k':(1, 15), # Нож (kmife)
       'x':(3, 20), # Топор (axe)
       't':(1, 25), # Оберег (Talisman)
       'f':(1, 15), # Фляжка (flask)
       'd':(1, 10), # Антидот (antidot)
       's':(2, 20), # Еда (Supplies)
       'c':(2, 20)} # Арбалет (crossbow)

def Get_area_and_value(baza):
    area = [baza[item][0] for item in baza]
    value = [baza[item][1] for item in baza]
    return area, value

def Get_memtable(baza, W):
    area, value = Get_area_and_value(baza)
    n = len(value)

    T = [[0 for x in range(W + 1)] for y in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                T[i][j] == 0
            elif area[i - 1] <= j:
                T[i][j] = max(value[i - 1] + T[i - 1][j - area[i - 1]], T[i - 1][j])
            else:
                T[i][j] = T[i - 1][j]
    return T, area, value


def Get_selected_itens_list(baza, W):
    T, area, value = Get_memtable(baza, W)
    N = len(value)
    res = T[N][W]
    w = W
    items_list = []

    for i in range(N, 0, -1):
        if res <= 0:
            break
        if res == T[i -1][w]:
            continue
        else:
            items_list.append((area[i -1], value[i -1]))
            res -= value[i - 1]
            w -= area[i - 1]

    baza_keys = []

    for search in  items_list:
        for key, value in baza.items():
            if value == search and key not in baza_keys:
                for i in range(value[0]):
                    baza_keys.append(key)
                break
    baza_keys = set(baza_keys)
    return  list(baza_keys)

def Flag(totvalue, damage):
    if totvalue - damage > 0:
        return True
    else:
        return False

def Get_pull(Res, baze):
    Table = [baze[item][0] for item in Res]
    Res = list(Res)
    table_n = []
    for i in range(len(Table)):
        table_n += [[Res[i]]] * Table[i]
    return table_n

def Get_all_comb(i, Dl, L, count):
    global  baza, A, key, summa
    if baza[key[i]][0] + Dl <= W:
        Dl += baza[key[i]][0]
        count += baza[key[i]][1]
        L.append(key[i])
        for k in range(i+1, len(key)):
            Get_all_comb(k, Dl, L.copy(), count)
        if summa - count < count:
            A.append(L.copy())
            A[0].append(count)

def Get_final_all_comb():
    Get_all_comb(0, 0, [], 0)

    for ind, sp in enumerate(A[1::]):
        table = [[0 for _ in range(3)] for _ in range(3)]
        table[2][2] = "d"
        el_old = 'd'
        for el in sp:
            if baza[el][0] == 3:
                table[0] = [el for _ in range(3)]
                el_old += el
            if baza[el][0] == 2:
                if table[1][0] == 0:
                    table[1][0] = el
                    table[2][0] = el
                    el_old += el
                else:
                    table[1][1] = el
                    table[2][1] = el
                    el_old += el
            elif el not in el_old:
                if table[1][1] == 0:
                    table[1][1] = el
                elif table[1][2] == 0:
                    table[1][2] = el
                else:
                    table[2][1] = el
        for line in table:
            print(*line)
        print(f"Итоговые очки выживания: {A[0][ind] - summa + A[0][ind]}")
        print("-------")


print('Решение основного задания')
W = 9
baza_new = baza.copy()
del baza_new['d']
#print(baza_new, len(baza_new))
W -= baza['d'][0]
Res = Get_selected_itens_list(baza_new, W)
Res += ['d']
#print(Res)
print(Get_pull(Res, baza))
totarea = sum(baza[item][0] for item in Res)
totvalue = sum(baza[item][1] for item in Res)
print('занимаает место = ', totarea, 'Сумм ценность = ', totvalue)
Hit_point = 15 + totvalue
baza_damage = baza.copy()
for l in range(len(Res)):
    del  baza_damage[Res[l]]
#print('baza_damage = ', baza_damage)
damage = sum(baza[item][1] for item in baza_damage.keys())
#print('damage = ', damage)
#print(sum(baza[key][1] for key in baza.keys()) - damage)
print(f'Если флаг поднять, значить итоговые очки выживания положительные, то есть герой выживает. Положение флвгв: {Flag(totvalue, damage)}')
print("Итоговые очки выживания: ", totvalue)

print('', 'Решение для доп. задание №1', sep='\n')
W = 7
Res = Get_selected_itens_list(baza, W)
print(Res)
totarea = sum(baza[item][0] for item in Res)
totvalue = sum(baza[item][1] for item in Res)
print('занимаает место = ', totarea, 'Суммарная ценность = ', totvalue)

print('', 'Решение для доп. задание №2', sep='\n')
A = [[]]
W = 9
key = list(baza.keys())
summa = sum(baza[item][1] for item in baza.keys())
Get_final_all_comb()
#print(Get_memtable(baza, W))