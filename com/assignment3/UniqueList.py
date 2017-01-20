def unique_list(list):
    a=[]
    for i in list:
        if i not in a:
            a.append(i)
    return a



new=unique_list(['a','a','a','c','c','b','d','d'])
print(new)