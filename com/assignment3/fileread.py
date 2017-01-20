
#finding a word from a text in file
def check(f_name, word):
    with open(f_name) as file:
        return any(word in line for line in file)

if check('Sample.txt', 'Python'):
    print("true")
else:
    print("false")



