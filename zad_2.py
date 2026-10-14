#A
def imiona(i):
    print(i)
    return

imi = ["Klaudia", "Kinga", "Karolina", "Szymon", "Kamil"]
imiona(imi)

#B I
def liczba(l):
    for l in licz:
        print(l * 2)
    return

licz = [22, 55, 45, 11, 69]
print(liczba(licz))

#B II
def liczba2(l):
    l=[x*2 for x in l]
    return l

licz = [22, 55, 45, 11, 69]
print(liczba2(licz))

#C
def parz(p):
    j=[]
    for i in range(len(p)):
        if p[i]%2 == 0:
            j.append(p[i])
    return j

p = list(range(10))
print(parz(p))

#D
def co_drugi_element(lista):
    for i in range(0, len(lista), 2):
        print(lista[i])

liczby = list(range(10))
co_drugi_element(liczby)