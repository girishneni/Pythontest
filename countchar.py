my_str="hello world"
words=my_str.split()
print(len(words))
countChar=0
for i in range(len(words)):
    for k in range(int(len(my_str)/2)):
        print(words[i][k])
        countChar+=1

print(countChar)