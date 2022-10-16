# With the value that we got from "var name" the program print: "name" (message) 
name = input("What is your name? ")
name = name.strip()
name = name.title()
print(f"Hi {name}, would you like to learn python?")

# The name is printed in uppercase, lowercase and .title()
eric= "eric"
eric = eric.upper()
print(eric)
eric = eric.lower()
print(eric)
eric = eric.title()
print(eric)

# Here we printed a quote from a famous person
print('Albert Einstein once said, “A person who never made a mistake never tried anything new.”')

# Here we put the name of the famous person in a variable and then we print the 
# quote calling the name of the famous person in the variable
famous_person = "Albert Einstein"
print(f'{famous_person} once said "A person who never made a mistake never tried anything new."')