#1.if numbers is zero print like "Entered number is zero"
n=int(input())
if n==0:
      print("Entered number is zero")
print("program done")

#2. check if number is zero or not
num=int(input("Enter a number:"))
if num==0:
        print("number is zero")
else:        
        print("number is not zero")

#Approach 2
num = int(input("Enter a number:"))
if num!=0:
       print("number is a not zero")
else:
       print("number is a zero")


#3. check if number is even or odd
num=int(input("Enter a number:"))
if num%2==0:
        print(num,"number is even")
else:
    print(num,"number is odd")
print("program is successfuly executed")

#4. checking number is -ve even,-ve odd,+ve even,+ve odd
num=int(input("Enter a number:"))
n=10
if num>=0 and num%2==0:
        print("number is a positive even")
elif num>=0 and num%2!=0:
        print("number is a positive odd")
elif num<0 and num%2==0:
        print("number is a negetive even")
elif num<0 and num%2!=0:
        print("number is a negetive odd")
else:
        print("number is negetive odd")
    
   
        
