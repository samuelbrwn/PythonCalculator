import calcfunctions
################USER INPUT################

z = input('Enter an operator(add, sub, mult, div): ').lower()
x, y = map(int, input("Enter two numbers: ").split())

if z == "add":
    calcfunctions.add(x,y)
elif z == "sub":
    calcfunctions.sub(x,y)
elif z == "mult":
    calcfunctions.mult(x,y)
elif z == "div":
    calcfunctions.div(x,y)
else:
    print("Operator undefined.")