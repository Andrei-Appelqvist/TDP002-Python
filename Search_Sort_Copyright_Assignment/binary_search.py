seq = [3,4,5,9,15,78,81,99,101]
imbd= [{'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},
 {'title': 'sdf', 'actress': 'Raise your voice', 'score': 13},
 {'title': 'fgjh', 'actress': 'Hilary Duff', 'score': 15},
 {'title': 'yuew', 'actress': 'Hilary Duff', 'score': 18}]

def binary_search(x, seq, func=lambda e: e):
    low = 0
    high = len(seq) - 1
    while low <= high:
        mid = (low + high) // 2
        if func(seq[mid]) < x:
            low = mid + 1
        elif func(seq[mid]) > x:
            high = mid - 1
        else:
            return mid;
    return -1


print(binary_search(15, seq))
