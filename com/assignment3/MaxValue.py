#finding the Maximun Value for given three no's

def MaxValue(val1,val2,val3):
    if(val1>val2 and val1>val3):
        return print("Max value is:",val1)
    elif(val2>val3):
        return print("Max Value is:",val2)
    else:
        return print("Max Value is:",val3)


MaxValue(100,588,200)