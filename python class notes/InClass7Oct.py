def max(num1,num2):#parameters
    if num1>num2:
        print("Num1 is greater")
    elif num2>num1:
        print("num2 is greater")
    else:
        print("both")
max(20,10)


'''def emp(name,Age):#positional Arguments
    print("NAme=", Name, "AGe=",Age)
emp("harry")'''

#parameter with default values:
def emp(name, msg="welcome"):
    print("Hello", name, msg)
emp("harry")

            
