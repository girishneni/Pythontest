high=100
low=1

def presence(num):
    if(num>=low & num<=high ):
        print('number is within the range')
    else:
        print('number is out of range')


presence(25)
presence(100)
presence(0)
presence(-1)