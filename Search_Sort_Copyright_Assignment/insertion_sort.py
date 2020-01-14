


def insertion_sort(db, func=lambda e:e):
    for i in range(0, len(db)):
        key = db[i]
        j = i - 1
        while j >= 0 and func(key) < func(db[j]):
            db[j+1] = db[j]
            j -= 1
        db[j+1] = key

db = [(2,3),(1,5),(4,2),(0,1)]
print(db)
insertion_sort(db, lambda e: e[1])
print(db)
