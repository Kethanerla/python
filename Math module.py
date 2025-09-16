# ------------------- Basic Built-in Number Functions -------------------

# complex()
z1 = complex(2, 3)    
z2 = complex(5, -4)   
print("complex numbers:", z1, z2)

# divmod()
a, b = 17, 5
print("divmod(17,5):", divmod(a, b))  

# float()
num1 = 10
print("float(10):", float(num1))     
print("float('inf'):", float('inf'))
print("float('-inf'):", float('-inf'))

# round()
print("round(4.6):", round(4.6))         
print("round(4.4):", round(4.4))         
print("round(4.567, 2):", round(4.567, 2))
# Here, ndigits = 2, so we keep 2 digits after the decimal point.
# 4.567 - 4.57 (because the third digit 7 makes the second digit 6 round up to 7).
#Python’s round() uses Banker’s Rounding (also called round half to even) for .5 cases.
print(round(2.5))  # 2 (not 3!)
print(round(3.5))  # 4



# ------------------- Type Checking Methods -------------------

# isinstance()
a = 4.0
print("isinstance(a, int):", isinstance(a, int))    
print("isinstance(a, float):", isinstance(a, float)) 

nums = [10, 10.0, 11, 11.0, 12, 13]
for n in nums:
    print(n, "is int?", isinstance(n, int))

# type()
a = 10
b = 3.14
c = "Hello"
d = [1, 2, 3]
print("type(a):", type(a)) 
print("type(b):", type(b))  
print("type(c):", type(c))  
print("type(d):", type(d))  


# ------------------- Math Module Methods -------------------
import math

# trunc()
print("math.trunc(4.9):", math.trunc(4.9))   
print("math.trunc(-4.9):", math.trunc(-4.9)) 

# factorial()
print("math.factorial(5):", math.factorial(5))  

# fabs()
print("math.fabs(-10):", math.fabs(-10))  
print("abs(-10):", abs(-10))              
print("math.fabs(-10):", math.fabs(-10)) 

# floor()
print("math.floor(4.7):", math.floor(4.7))   
print("math.floor(-4.7):", math.floor(-4.7)) 

# pow()
print("pow(2,3):", pow(2,3))          
print("math.pow(2,3):", math.pow(2,3)) 

# ceil()
print("math.ceil(4.2):", math.ceil(4.2))    
print("math.ceil(-4.7):", math.ceil(-4.7))  

