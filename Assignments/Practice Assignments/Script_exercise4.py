class Script:
  
  def __init__(self):
    self.n1=0
    self.n2=1
    self.n3=0
  
  def factorial_recursion(self,num):
    if(num==0):
      return 1
    else:
      fact=num*self.factorial_recursion(num-1)
    return fact
  
  def fibonacci_recursion(self,num):
    if(num>0):
      self.n3=self.n2+self.n1
      self.n1=self.n2
      self.n2=self.n3
      print self.n3
      self.fibonacci_recursion(num-1)	
  
  def main(self):
    print("Menu:\n")
    print("1: Factorial of a number")
    print("2: Fibonacci Series")
    n=input("Enter your choice")
    if n==1:
      print(self.factorial_recursion(input("Enter the number for factorial:")))
    elif n==2:
      self.fibonacci_recursion(input("Enter the number of elements in fibonacci series:"))
    else:
      print("Enter valid number")