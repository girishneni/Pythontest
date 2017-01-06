my_str=input("enter the string value:")
#making the string for a caseless comparision

my_str=my_str.casefold()
rev_str=reversed(my_str)
#converting a string to list for comparsion

if(list(my_str)==list(rev_str)):
    print("it is a palindrome")
else:
    print("it is not a palindrome")