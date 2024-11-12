
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)





#ADD FUNCTION

def add(n1, n2):
  return n1 + n2
# SUBTRACT
def subtract(n1, n2):
  return n1 - n2
#MULTIPLY
def multiply(n1, n2):
  return n1 * n2
#DIVIDE
def divide(n1, n2):
  return n1 / n2

operations = {}
operations["+"] = add
operations["-"] = subtract
operations["*"] = multiply
operations["/"] = divide  


num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
  print(symbol)
operation_symbol = input("pick an operation from the lines above: ")

calculation_function =       operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}")
