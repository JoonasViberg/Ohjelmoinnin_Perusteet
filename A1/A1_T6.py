#1 Prompt user “Insert an integer: ” and assign the input value into Feed variable

Feed = input("Insert an integer: ")

#2 Convert the Feed into an integer and assign it to Value variable

Value = int(Feed)

#3 Calculate the remainder of the Value when divided by 2 and assign it to the Remainder variable.

Remainder = Value % 2

#4 Print the inserted value “Value is {Value}”

print (f"Value is {Value}")

#5 Print the remainder value “The remainder is {Remainder} when {Value} is divided by 2.”

print (f"The remainder is {Remainder} when {Value} is divided by 2.")