def reccur_fact(n):
    if n==1:
        return n
    else:
        return n*reccur_fact(n-1)
    
#driver code

number=int(input())
if number==0:
    print("the factorial is 0")
elif number<0:
    print("the factorial is not possible")

else:
    print("the factorial is",number,"is",reccur_fact(number))
