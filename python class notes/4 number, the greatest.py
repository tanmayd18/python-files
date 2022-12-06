a=eval(input("enter the first number:"))
b=eval(input("enter the 2nd number:"))
c=eval(input("enter the 3rd number:"))
d=eval(input("enter the 4rd number:"))
sum=a+b+c+d
for i in range(sum):
    if i==a or i==b or i==c or i==d:
        Large=i
print(Large)        
