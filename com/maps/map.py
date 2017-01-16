def starmap(function, iterable):
    # starmap(pow, [(2,5), (3,2), (10,3)]) --> 32 9 1000
    for args in iterable:
        yield function(*args)


print(tuple(starmap(pow,[(2,5),(3,2),(10,3)])))


def takewhile(predicate, iterable):
    # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
    for x in iterable:
        if predicate(x):
            yield x
        else:
            break
print(list(takewhile(lambda x:x<5,[1,2,3,4,5])))


def numb(num):
    if(num%2==0):
        return num
    else:
        return "not even"


n=[0,1,2,3,4,5,6,7,8,9,10]
print(list(map(numb,n)))
list = [1, 2, 3, 4, 5, 6, 7]
