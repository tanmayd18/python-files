num1=eval(input("enter number:"))
num2=eval(input("enter number2:"))
print("1)Add")
print("2)Sub")
print("3)Mul")
print("4)Div")
choice=int(input("please enter choice:"))
if choice==1:
    print("Add", num1,"and", num2,"is", num1+num2)
elif choice==2:
    print("Sub", num1,"and", num2,"is", num1-num2)
elif choice==3:
    print("Mul", num1,"and", num2,"is", num1*num2)
elif choice==4:
    print("Div", num1,"and", num2,"is", num1//num2)
else:
    print("sorry")
