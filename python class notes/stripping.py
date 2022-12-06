#stripping characters from a string
S1=" \t\*hello python "
S2=S1.lstrip()
print(S2)


S2=S1.rstrip()
print(S2)


S1.strip('\t')
print(S1)


#formatting a string:
S1="hello python"
print(S1.center(15))
print(S1.rjust(15))
print(S1.ljust(5))
