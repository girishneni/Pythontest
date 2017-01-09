my_str="hello world Welcome to python"
words=my_str.split()
no_words=len(words)
print("No of words in a string:",no_words)

for i in range(no_words):
    print("no of char in word",[i],"is :",len(words[i]))


