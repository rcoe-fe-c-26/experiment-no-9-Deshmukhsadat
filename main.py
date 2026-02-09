# AIM: Design a Python program to compute 
# the factorial of a given integer N.
# Coder:Deshmukh Sadat Anwar Ahmad
# Date: 30-JAN-2026

print("--- Factorial Finder ---\n")


# Write your code here:
a = int(input("Enter Number: "))
if a<0:
    print(f"Factorial of {a} is Not Defined")
fact = 1
for x in range(1,a+1):
    fact = fact*x 
print(f"Factorial of {a} is",fact)


