name = 'Doug'
age = 40
product = 'Python eLearning course'

#format method index based string interpolation - not the best way -
#greeting = "Hi {0}, you are listed as {1} years old and you have purchased: {2}.".format(name, age, product)

#string literal -c leaner and you don't have to keep track of all the index numbers
greeting = f"Hi {name}, you are listed as {age} years old and you have purchased: {product}"

print(greeting)