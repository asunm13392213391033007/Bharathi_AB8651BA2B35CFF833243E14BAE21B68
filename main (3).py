def factorial(n): 
  if n==0 or n==1:
    return 1
  else:
    return n* factorial(n-1)
namber=int(input("ENTER A VALUE:"))
fact =factorial (namber)
print("THE FACTORIAL OF",namber, "IS",fact)