lst = ['listItem1','listItem2','listItem3','listItem4','listItem5','listItem6']
print('Your List : ',lst)

lst.append('AppendedItem')
print('\nYour List After Apped Item: ',lst)

lst.extend('listItem1')
print('\nYour List After Extended Item: ',lst)

lst.remove('listItem1')
print('\nYour List After Remove Item: ',lst)

lst.sort()
print('\nYour List After Assending Order : ',lst)

lst.sort(reverse=True)
print('\nYour List After Assending Order : ',lst)