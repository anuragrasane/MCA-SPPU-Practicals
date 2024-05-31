'''
str1 = 'PythonForPython'
# lambda returns a function object
rev_upper = lambda string: string.upper()[::-1]
print(rev_upper(str1))
#Output: NOHTYPROFNOHTYP
#Condition Checking Using Python lambda function
format_numeric = lambda num: f"{num:e}" if isinstance(num, int)else f"{num:,.2f}"
print("Int formatting:", format_numeric(1000000))
print("float formatting:", format_numeric(999999.789541235))
#Output: Int formatting: 1.000000e+06
#float formatting: 999,999.79
#using the lambda function
#print("Using lambda function, cube:", lambda_cube(5))
div = lambda x: x/2
print(div(10))
'''
is_even_list = [lambda arg=x: arg * 10 for x in range(1, 5)]
# iterate on each lambda function and invoke the function to get the calculated value
for item in is_even_list:
    print(item())
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(filter(lambda x: (x % 2 != 0), li))
print(final_list)
# Python code to illustrate map() with lambda() to get double of a list
#li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2, li))
print(final_list)
