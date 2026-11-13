def minmax(*pomiary):
    if pomiary:
        return (min(pomiary), max(pomiary))
    else:
        raise ValueError("brak pomiarów")

dane = [3, 9, 4]

print(minmax(8, 12, 10))
print(minmax(*dane))

def przetworz(*pomiary, minimum=None, maksimum=None, skala=1):
    output = []
    
    for p in pomiary:
        if minimum is not None and p < minimum:
            continue
        if maksimum is not None and p > maksimum:
            continue
        output.append(p*skala)
    return output

print(przetworz(3, 9, 4, skala=2))

