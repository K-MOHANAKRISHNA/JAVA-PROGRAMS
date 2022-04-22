##pythpon program to check number is prime ir not

n=int(input("Enter a number"))

if(n>1):
    for i in range(2,int(n/2)+1):
        if(n%i==0):
            print(n," is not a prime number")
            break
        else:
            print(n," is a prime number")
else:
    print(n," is not a prime number")


##Fibbonacci search using recursion

def fibo(n):
   if n <= 1:
       return n
   else:
       return(fibo(n-1) + fibo(n-2))

n=int(input("Plese enter a positive integer:"))
print("Fibonacci sequence:")
for i in range(n):
    print(fibo(i))


##Factorial program

num = int(input("Enter a number: "))
factorial = 1
if num < 0:
   print("factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)

##Palindrome or not

number=int(input("Enter any number :"))
temp=number
rev_num=0
while(number>0):
    digit=number%10
    rev_num=rev_num*10+digit
    number=number//10
if(temp==rev_num):
    print(temp," The number is palindrome!")
else:
    print("Not a palindrome!")

##program to find sum of digits in a number

def getSum(n):
    sum = 0
    while (n != 0):   
        sum = sum + (n % 10)
        n = n//10   
    return sum
   
n = int(input("Enter a number:"))
print("sum of a digits in a number ",getSum(n))


##program to find given year is leap year or not

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print(year," year is a leap year!")
else:
    print(year," year isn't a leap year!")
    
    
##armstrong number or not

num=int(input("Enter a number:"))
order = len(str(num))
sum = 0
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** order
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")

##number is strong or not

#Strong number : A Strong number is a special number whose sum of the all digit factorial should be equal to the number itself.
  
#For example - The given number is 145, we have to pick each digit and find the factorial 1! = 1, 4! = 24, and 5! = 120.
#Now, we will do the sum of the factorials, we get 1+24+120 = 145, which is exactly the same as the given number. So we can say that 145 is a strong number.

sum=0
num=int(input("Enter a number:"))    
temp=num  
while(num):    
    i=1  
    fact=1  
    rem=num%10  
    while(i<=rem):  
        fact=fact*i   # Find factorial of each number  
        i=i+1  
    sum=sum+fact  
    num=num//10  
if(sum==temp):  
    print(temp," number is a strong number")  
else:  
    print(temp," number is not a strong number")  

##swapping of 2c numbers without using thirs variable

x=int(input("Enter a number:"))
y=int(input("Enter a number:")) 
print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)
# code to swap 'x' and 'y'
x, y = y, x
print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)


##number is automorphic or not
##automorphic:A number is said to be an automorphic number if the last digits of the square of this number give the same numb
  
def isAutomorphic(N) :
	sq = N * N
	while (N > 0) :
		if (N % 10 != sq % 10) :
			return False
		N //= 10
		sq //= 10

	return True
N =int(input("Enter a number:"))
if isAutomorphic(N) :
	print (N," is Automorphic")
else :
	print ("Not Automorphic")

  
##number is perfect or not

#perfect number : Any number can be perfect number in Python, if the sum of its positive divisors excluding the number itself is equal to that number.

n = int(input("Enter any number: "))
sum1 = 0
for i in range(1, n):
    if(n % i == 0):
        sum1 = sum1 + i
if (sum1 == n):
    print(n," number is a Perfect number!")
else:
    print("The number is not a Perfect number!")

    
##Harshad number

#harshad number:If a number is divisible by the sum of its digits, then it will be known as a Harshad Number.

num =int(input("enter a number:"))
rem = sum = 0   
n = num    
while(num > 0):    
    rem = num%10  
    sum = sum + rem   
    num = num//10    
if(n%sum == 0):    
    print(n, " is a harshad number");    
else:    
    print(n, " is not a harshad number");   

##Abundant number
#abundant number:A Number that is smaller than the sum of all it's factors except the number itself is known as an Abundant number.

n = int(input("enter a number"))
sum=0
for i in range(1,n):
  if(n%i==0):
   sum=sum+i

if(sum>n):
  print(n,'is Abundant Number')

else:
  print(n,'is not Abundant Number')


