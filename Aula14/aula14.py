"""
Documentação - Built-in types
"""

num1 =  (input ("Digite um número: "))
num2 =  (input ("Digite outro número "))

# isnumeric, isdigit, isdecimal
#numeros e positivos (123456.22)

try:
    num1 = float(num1)
    num2 = float(num2)
    
    print(int (num1 + num2))
    
except: 
    print("Error!")
    
        