import calcfunctions
################USER INPUT################

z = input('Enter an operator(add, sub, mult, div): ').lower()
x, y = map(int, input("Enter two numbers: ").split())

if z == "add":
    add(x,y)
elif z == "sub":
    sub(x,y)
elif z == "mult":
    mult(x,y)
elif z == "div":
    div(x,y)
else:
    print("Operator undefined.")