imbd= [{'title': 'Raise your voice', 'actress': 'Hilary Duff', 'score': 10},
 {'title': 'sdf', 'actress': 'Raise your voice', 'score': 13},
 {'title': 'fgjh', 'actress': 'Hilary Duff', 'score': 18},
 {'title': 'yuew', 'actress': 'Hilary Duff', 'score': 13}]


seq = [1, 4, 6 ,7]
def linear_search(seq, val, func = lambda e: e):
    result = []
    for dict in seq:
        if func(dict) == val:
            return dict
    if result == []:
        return -1
    else:
        return dict




print(linear_search(seq, 4))
print(linear_search(imbd, "Raise your voice", lambda e: e["actress"]))



"""
    if func == None:
        for i in dict:
            if dict[i] == val:
                result.append(dict)
    else:

"""
