'''2.6. Print the following pattern of numbers:

5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
'''
i=int(input('Enter number for Pyramid Pattern:'))
while i>=1:
    j=i
    while j>= 1:
        print(j,end=' ')
        j=j-1
    print()
    i=i-1
