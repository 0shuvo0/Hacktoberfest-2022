# takes a list of lists and flattens it

def flatten(l):
    flat_list = []
    for sublist in l:
        for item in sublist:
            flat_list.append(item)
    return flat_list

print(flatten([[1, 2, 3], [4, 5, 6]]))
