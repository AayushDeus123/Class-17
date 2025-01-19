a =int(input('Enter a number : '))

while a>0:
    a = a - 1
    if a == 5 or a % 5 == 0:
        continue
    print('\n Current vaule of n is :',a)
print('\n Good Bye')