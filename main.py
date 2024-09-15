def cube(x):
    return x**3
def divi3(x):
    if x%3==0:
        return cube(x)
    else: 
     return "Not Divisible"
n=int(input("Enter any number:"))
print("Value:",divi3(n))