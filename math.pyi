def MathOperations(a, b, operator):
    if operator == "+":
        return (a + b)
        
    if operator == "*" : 
        return (a*b)
        
    if operator == "-" : 
        return a-b
        
    if operator == "/" : 
        return a/b
        
    if operator == "^" : 
        return a^b
        
    print("Invalid operation")


a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))
operatios = ["*", "/", "^", "-", "+"]
for o in operatios: 
    print(f'{a} {o}  {b} = {MathOperations(a, b,o)}')
    if a == 12 :
     print(f"A =12")
