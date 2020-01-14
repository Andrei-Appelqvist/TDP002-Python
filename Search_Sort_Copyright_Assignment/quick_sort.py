def quick_sort(db, func=lambda e: e):
    db_length = len(db)
    if(db_length <= 1):
        return db
    else:
        pivot = db[0]
        greater = [element for element in db[1:] if func(element) > func(pivot)]
        lesser = [ element for element in db[1:] if func(element) <= func(pivot)]
        return quick_sort(lesser, func) + [pivot] + quick_sort(greater, func)


db = [5, 3, 8, 10, 1, 11]
#db = [(0, 1) ,(5, 3), (8, 2)]
print(db)
var = quick_sort(db)
print(var)
