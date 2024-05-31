#2.5. Write a Python program to check whether a given number is an Armstrong number or not using a while loop. Accept the number from the user.
num= int(input("Enter a Number"))
order=len(str(num))
sum=0
temp = num
while temp>0:
    digit = temp % 10
    #sum=sum+digit**3
    sum=sum +digit**order
    temp//=10
if num== sum :
        print(num,"is a Armstrong Number")
else:
        print(num,"is not Armstrong Number")
