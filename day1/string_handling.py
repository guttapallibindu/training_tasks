text = "hello , My name Is bindu"

print(text.upper()) #converts all words to uppercase
print(text.lower()) #converts all words to lowercase
print(text.split()) #converts to a lits and removes spaces
print(type(text.split())) #type after splitting it 
print(text.replace("bindu" , "Guttapalli Bindu"))
print(text.replace("Guttapalli" , "Guttapalli Bindu"))
print(text.title())
print(text.capitalize())
print(text.find("Hi"))
print(text.find("My")) #will take first letter index of the particular word
print(text.count("l"))
print(len(text))
print("Hello".count("l"))
print(text.isalpha())
print(text)