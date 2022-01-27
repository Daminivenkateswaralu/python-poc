from ast import operator


class calculator:
    def add(self,a,b):
        print("The sum is " + str(a+b))
        return (a+b)
    def sub(self,a,b):
        print("The difference is " + str(a-b))
    def mult(self,a,b):
        print("The product is " + str(a*b))
    def div(self,a,b):
        print("The divident is " + str(a/b))

print("Select operation to perform")
print("1.add")
print("2.Subract")
print("3.Multiply")
print("4.Divide")

operation = input("Enter the operand")
calci = calculator()
if operation == "1":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 1: "))
    calci.add(num1,num2)
elif operation == "2":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 1: "))
    calci.sub(num1,num2)
elif operation == "3":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 1: "))
    calci.mult(num1,num2)
elif operation == "3":
    num1 = int(input("Enter number 1: "))
    num2 = int(input("Enter number 1: "))
    calci.div(num1,num2)
else:
    print("enter valid input")

