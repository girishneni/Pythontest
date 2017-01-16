from collections import defaultdict

#defaultdict used as a list
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d= defaultdict(list)

for key,value in s:
    d[key].append(value)

print(sorted(d.items()))

#defaultdict as an int then we can use it as a counter
s='abbbcdisiisaa'
f=defaultdict(int)

for k in s:
   f[k]=+1
print(sorted(f))

#defaultdict as a set
s=[('red',1),('green',2),('red',1),('red',1)]
a=defaultdict(set)
for k,v in s:
    a[k].add(v)
print(a)