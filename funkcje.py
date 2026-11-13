def minmax(*pomiary):
    if pomiary:
        return (min(pomiary), max(pomiary))
    else:
        raise ValueError("brak pomiarów")

dane = [3, 9, 4]

print(minmax(8, 12, 10))
print(minmax(*dane))
