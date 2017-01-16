#filter: function,iterable
#it is similar to map but returns a iterable only for the true condition of a function
print('Odd check:\n')
def numodd(n):
    if(n%2!=0):
        return n

i=range(10)
d=filter(numodd,i)

for k in d:
    print(k)

print('\n even check:\n')
def even_check(num):
    if(num %2 == 0 ):
        return True

numbersList = range(10) # 0 to 20

d = filter(even_check, numbersList)

for item in d:
    print(item)