#Using PASS keyword in loop
a = int(input('Enter a number : '))

for i in range(a):
    if i % 20 == 0:
        print('Twist')
    elif i % 15 == 0:
        print('Tam')
    elif i % 5 == 0:
        pass
    elif i % 3 == 0:
        print('Buzz')
    else:
        print(i)