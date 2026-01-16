#simple calculator operations
#variable and operators
a=10
b=20
addition=a+b

#Arthimetic operators
print("sum of two numbers is:", addition)
print("subtraction of two numbers is:",a-b)
print("multiplication of two numbers is:",a*b)
print("division of two numbers is:",b/a)
print("floor division of two numbers is:",b//a)
print("modulo division of two numbers is:",b%a)
print("power of two numbers is :",b**a)

#Realtional operators
a=20
b=30
print("Relational Operators")
print("20 less than 30 is :",20<30)
print("20 lessthan 30 is:",20<30)
print("20 greeaterthan 30 is:",20>30)
print("20 lessthan or equal to 30 is:",20<=30)
print("20 greatertan or equal to 30 is:",20>=30)
print("20 equal to equal to 30 is:",20==30)
print("20 not equal to 30 is:",20!=30)

#Logical operators
a=10
b=20
print("logical Operators")
print("a>5 and b<10:",a>5 and b<10)
print("a>5 or b>10:",a>5 or b>10)
print("not(a>b):",not(a>b))

#Assignment operators
a=10
print("Initial value of a:",a)
a+=5
print("After a+=5:",a)
a-=3
print("After a-=3:",a)
a*=2
print("After a*=2:",a)
a/=4
print("After a/=4:",a)
a%=3
print("After  a%=3:",a)
a**=2
print("After a**=2:",a)

#Bitwise operators
print("Bitwise operators")
a=10
b=20
print("a&b:",a & b)       #AND
print("a | b :", a | b)   # OR
print("a ^ b :", a ^ b)   # XOR
print("~a    :", ~a)      # NOT
print("a << 1:", a << 1)  # Left shift
print("a >> 1:", a >> 1)  # Right shift

# Membership Operators:

s=[20,30,67,"world",5.90,"Tanuja","BIET",652.90]

print("IN operators:",40 in s)
print("IN operator:", "hI" in s)
print("IN operators:", "Tanuja" in s)
print("NOT In operators:", 30 in s)
print(" NoT In operators:", 20 in s)

#Identity operators:

print(" IS operators:", a is b)
print(" NOT Is operators:", a is not b)


