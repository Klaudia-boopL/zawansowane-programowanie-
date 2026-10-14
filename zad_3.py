def liczba(l) -> bool:
    if l % 2 == 0:
        return True
    else:
        return False

if liczba(3) == True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")