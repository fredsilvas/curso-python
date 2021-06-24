user_age = int(input("Enter your age: "))
months = user_age * 12
days = months * 30.4375
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

print(f"Your age {user_age} is equal to {months} months.")
print(f"Your age {user_age} is equal to {days} days.")
print(f"Your age {user_age} is equal to {hours} hours.")
print(f"Your age {user_age} is equal to {minutes} minutes.")
print(f"Your age {user_age} is equal to {seconds} seconds.")