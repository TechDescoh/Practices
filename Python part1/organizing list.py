names = ["Carlos", "María", "Ramiro", "Fernando", "Juan Carlos"]
print(names)

#With the .sort() method we can order the list alfabetically permanently 
names.sort()
print(names)

#With the .sorted function we can order the list alfabetically but not permanently
# so we can use the original value as well
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\n{cars}")

print(sorted(cars))
print(f"\n{cars}")