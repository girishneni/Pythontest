from collections import namedtuple
D=namedtuple('Dog','age breed name')

Gan=D(age=10,breed='pugg',name='fif')
jeff=D(11,'puppy','jeff')

print(Gan)
print(jeff)
print(Gan.name)
print(jeff.age)

from collections import defaultdict

