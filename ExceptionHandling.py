'''while(True):
    try:
        x=int(input('Enter a valid no:'))
        break
    except ValueError:
         print('This is not a valid no ..try again')
'''

'''try:
    f = open('test.txt', 'r')
    f.write('this is to test try')
except IOError:
    print('Error: Could not find file or read data')

else:
    print('writen successfully')
    f.close()'''


#Finally statement execution
'''
try:
    f=open('test.txt','r')
    f.write('this is a test try')
    print('write is successful')
finally:
    print('Finally executes always')
    f.close()
'''

# how python handles the exceptions
try:
    f = open('test.txt', 'r')
    f.write('this is to test try')
except IOError:
    print('exception occured')
else:
    print('generic handlers')
finally:
    print('finally is executed')
    f.close()