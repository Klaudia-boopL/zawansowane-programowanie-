def listy(lista1, lista2):
    polaczona = lista1 + lista2
    bez_duplikatow = set(polaczona)
    wynik = [x ** 3 for x in bez_duplikatow]
    return wynik

lista1 = [1,6,2,4]
lista2 = [9,3,1,5,7]
print(listy(lista1, lista2))