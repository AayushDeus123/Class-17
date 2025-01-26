bill = float(input('Enter the bill : '))
paid = float(input('Enter the amount paid : '))
rem = paid - bill

for i in range(1):
    if paid == bill:
        print('You have no remainder to pay')
        break
    else:
        print('The shopkeeper owes you ',rem)
print('Have good day!')        