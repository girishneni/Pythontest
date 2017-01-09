st = 'Create a list of the first letters of every word in this string'
st_word=st.split()
len_st_word=len(st_word)
print("The first letter of each word is :")
for i in range(len_st_word):
        print(st_word[i][0])

