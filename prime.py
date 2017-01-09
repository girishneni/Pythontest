def genprime(num):
    i=1
    for i in range(num):
        if(i>1):
            for x in range(2,i):
                if(i%x==0):
                    break
            else:
                    print(i)

new=genprime(10)