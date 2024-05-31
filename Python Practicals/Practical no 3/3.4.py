'''3.4 Write a Python program to calculate the factorial of a given
user-accepted number using a recursive function.'''
def fact(num):
    if num==0:
        return 1
    else:
        return num* fact(num-1)

num=int(input("Enter Any Number: "))
print("Factorial of Given Number: ", num , "= ",fact(num))

'''
fact(3)             1 call with 4
4*fact(3)           2 call with 3
4*3*fact(2)         3 call with 2
4*3*2*fact(1)       4 call with 1
4*3*2*1
'''
