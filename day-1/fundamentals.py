###variables
age = 45 #integer
salary = 1459.5 #float
name = "johndoe" #string

print(f"age:{age} is a"+ ' ' +str(type(age)))
print(f"salary:{salary} is a"+ ' ' +str(type(salary)))
print(f"name:{name} is a"+ ' ' +str(type(name)))

###Operators:
# Operators are the main building block of any programming language. Operators allow the programmer to perform different kinds of operations on operands. These operators can be categorized based upon their different functionality

###Arithmetic Operators:
# Examples of Arithmetic Operator 
a = 9
b = 4
   
# Addition of numbers 
add_two_number = a + b 
# Subtraction of numbers  
sub_two_number = a - b 
# Multiplication of number  
mul_two_number = a * b 
# Division(float) of number  
div1 = a / b 
# Division(floor) of number  
div2 = a // b 
# Modulo of both number 
mod_of_two_number = a % b 
   
# print results 
print("add_two_number: "+str(add_two_number)) 
print("sub_two_number: "+str(sub_two_number)) 
print("mul_two_number: "+str(mul_two_number)) 
print("div1: "+str(div1)) 
print("div2: "+str(div2)) 
print("mod_of_two_number: "+str(mod_of_two_number))

# Relational Operators: Relational operators compares the values. It either returns True or False according to the condition.

# Examples of Relational Operators 
a = 13
b = 33
   
# a > b is False 
print(a > b) 
   
# a < b is True 
print(a < b) 
   
# a == b is False 
print(a == b) 
   
# a != b is True 
print(a != b) 
   
# a >= b is False 
print(a >= b) 
   
# a <= b is True 
print(a <= b)

# Logical Operators: Logical operators perform Logical AND, Logical OR and Logical NOT operations.

# Examples of Logical Operator 
a = True
b = False
   
# # Print a and b is False 
print(a and b) 
   
# # Print a or b is True 
print(a or b) 
   
# # Print not a is False 
print(not a) 

# Bitwise operators: Bitwise operator acts on bits and performs bit by bit operation.

# Examples of Bitwise operators 
a = 10
b = 4
   
# Print bitwise AND operation   
print(a & b) 
   
# Print bitwise OR operation 
print(a | b) 
   
# # Print bitwise NOT operation  
print(~a) 
print(~b) 
   
# # print bitwise XOR operation  
print(a ^ b) 
   
# # # print bitwise right shift operation  
print(a >> 2) 
   
# # # print bitwise left shift operation  
print(a << 2)

