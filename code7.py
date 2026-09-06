a=int(input("enter a number:"))
b=int(input("enter another number:"))
#arithmetic operation
print("the sum of two numbers:",a+b)
print("the difference of two numbers:",a-b)
print("the prouct of two numbers:",a*b)
print("the division of two numbers:",a/b)
print("the floor division of two numbers:",a//b)
print("the modulu of two numbers:",a%b)
print("the exponent of two numbers:",a**b)
#relational operation
print("a>b:",a>b)
print("a<b:",a<b)
print("a==b:",a==b)
print("a!=b:",a!=b)
#logical operation
print("a>0 and b>0:",a>0 and b>0)
print("a>0 or b>0:",a>0 or b>0)
print("not(a>b):",not(a>b))
#assignment operation
c=a
c=c+b
print("the value of c after assignment operation:",c)
#membership operation
s=input("enter a word:")
ch=input("enter a letter to search:")
print("the letter is in the word:",ch in s)