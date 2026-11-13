def minmax(*pomiary):
    if pomiary:
        return (min(pomiary), max(pomiary))
    else:
        raise ValueError("brak pomiarów")

print(minmax(1, 23, 4, 5))
print(minmax())
