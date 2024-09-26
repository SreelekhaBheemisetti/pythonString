# string : "My position is 1st and my friend come on 4th"
# output : 5

string = "My position is 1st and my friend come on 4th"
sum=0
for i in string:
    if i.isdigit()==True:
        z=int(i)
        sum=sum+z
print(sum)


# s = "My blog"
# a=s.upper()
# b=s.lower()
# c=s.islower()
# d=s.isupper()
# e=s.isalpha()
# f=s.isdigit()
# print(a,b,c,d,e,f)


# str1 = "Welcome to my Blog"
# print(str1.rstrip('og'))
# print(str1.lstrip('We'))
# print(str1.strip('Welog'))



