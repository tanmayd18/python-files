f=open('pythonhtml.txt','w')
f.write("this is tanmay")
f.close()
f=open('pythonhtml.txt','r')
for each in f:
    print(each)
