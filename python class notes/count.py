# write down the program to find the sum of the digits num=of given number
num=int(input("enter the number"))
x=num
sum=0
rem=0
while num>0:
    rem=num%10
    num=num//10
    sum=sum+rem
print("sum of digits", sum)