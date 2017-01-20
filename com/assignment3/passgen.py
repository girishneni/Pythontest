#password generator

import random
alpha='abcdefghijklnmopqrstuvwxyz'
upperalpha=alpha.upper()
psd_len=8
psd_list=[]

for i in range(psd_len//3):
    psd_list.append(alpha[random.randrange(len(alpha))])
    psd_list.append(upperalpha[random.randrange(len(upperalpha))])
    psd_list.append(str(random.randrange(10)))

for i in range(psd_len-len(psd_list)):
    psd_list.append(alpha[random.randrange(len(alpha))])

random.shuffle(psd_list)
p_string = "".join(psd_list)
print(p_string)
