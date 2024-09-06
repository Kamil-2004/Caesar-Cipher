import random

logo = """


                              ,     /)         
 _  _    _  _   _   __    _    __  (/    _  __ 
(__(_(__(/_/_)_(_(_/ (_  (___(_/_)_/ )__(/_/ (_
                            .-/                

"""
print(logo)
# make caesar cipher game

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x' ,'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g' ,'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def ceaser(start_text, shift_amount, cipher_direction):
  end_text = ""
if cipher_direction == "decode": 
  shift_amount *= -1
for letter in start_text:
  if char in alphabet:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    end_text += alphabet[new_position]
  else:
    end_text += letter
print(f"Here's the {cipher_direction}d result: {end_text}")

should_continue = True
while should_continue:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  shift = shift % 26
  ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
  result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
  if result == "no":
    should_continue = False
print("Goodbye")


def format_name(f_name, l_name):
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

print(format_name(input("What is your first name? "), input("What is your last name? ")))

calcuator

add  
def add(n1, n2):
  return n1 + n2

#subtract
def subtract(n1, n2):
  return n1 - n2

#multiply
def multiply(n1, n2):
  return n1 * n2

#divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))
for symbol in operations:
  print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
calculation_function = operations[operation_symbol]
answer = calculation_function(num1, num2)
print(f"{num1} {operation_symbol} {num2} = {answer}" )


                         


                         