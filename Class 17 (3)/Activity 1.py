#Using BREAK keyword in loops
a = input('Enter a word : ')
for i in a:
    if i == 'a':
        print('a is found in this word')
        break
    else:
        print(i)