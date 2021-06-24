name = "Bob"

print(f"Hello, {name}")

name = "Ron"

print(f"Hello, {name}")

#---------------------

name ="Fred"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

#---------------------

longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Rolf", "Monday")

print(formatted)

#---------------------