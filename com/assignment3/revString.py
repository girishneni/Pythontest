#print a given string in a reverse way
'''def revStr(str1):
    str1_new=""
    i=len(str1)
    while i:
        i -= 1
        str1_new +=str[i]
    return str1_new'''

def revStr(str1):
    str1_res=''
    str1_word=str1.split()
    i =len(str1_word)
    while i:
        i-=1
        str1_res+=" " + str1_word[i]
    print(str1_res)


revStr('My Name is girish')