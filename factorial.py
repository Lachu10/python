#factorial of a number
def factorial(n):
 return 1 if (n==1 or n==0)else factorial(n-1);
#driver code
num=5;
print("factorial of ",num ,"is",
      factorial(num))
