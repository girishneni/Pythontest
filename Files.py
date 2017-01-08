#basic file reading and writing
f=open('sample.txt','w+')
f.write('This is a new line')
#f.seek(0)
#print(f.read())

#appending to the same file and reading
#variable= open('fileanme','filemode)
#variable.read()
#varible.write('dskdhskd')
#f.close() //cumpolsory to close all files


f=open('sample.txt','a+')
f.write('\n This is the second line\n')
f.seek(0)
print(f.read())

#writing A new file
f1=open('firstfile.txt','w+')
f1.write('This is a new file')
f1.seek(0)
print(f1.read())


#Iterating through a file
for i in open('firstfile.txt'):
    print(i)

for line in open('sample.txt'):
  print(line, end=' ')

  f.close()
  f1.close()