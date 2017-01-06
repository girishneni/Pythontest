my_str="hello world"
word=my_str.split()
print(len(word))
countChar=0
for i in range(len(word)):
    for k in range(int(len(my_str)/2)):
        print(word[i][k])
        countChar+=1

print(countChar)