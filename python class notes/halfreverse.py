x=input()
a=len(x)//2
b=x[:a]
c=x[-a:]
print(b[::-1]+c[::-1])
