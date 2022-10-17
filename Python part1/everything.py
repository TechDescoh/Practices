#Using every function that I learned in the third chapter of the book at least once
things = ["minecraft", "mariana", "sofía", "medellín", "tokyo", "armenia", "drawing", "reading", "programming"]
print(things)

#Using String methods in lists
print(things[3].title())

#Index position
print(things[4])
print(things[-1])

#Using individuals values
print(f"{things[2].title()} is very wise")

#Modifing element of the list
things[8] = "english"
print(things)

#Adding elements to a list: append()
things.append("NYC")
print(things)

#Inserting elements to a list: insert()
things.insert(0, "sleep")

#Removing elements: del
del things[-1]

#Removing elements: pop()
pop_things = things.pop()
print(things)
print(pop_things)

#Removing a Item by value: remove()
things.remove("tokyo")
print(things)

#Finding the lenght of the list
print(len(things))

#Print a list in reverse order: reverse()
things.reverse()
print(things)
things.reverse()

#Sorting the list temporarily: sorted()
print(sorted(things))
print(sorted(things, reverse=True))
print(things)

#Sorting permanently the list: sort()
things.sort()
print(things)
things.sort(reverse=True)
print(things)
