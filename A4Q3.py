# Python program to square the elements of a list using map() function.

a = [4,5,2,9]

print(f'list : {a}')

result = map(lambda x : x ** 2 , a )

print(f'square list : {list(result)}')
