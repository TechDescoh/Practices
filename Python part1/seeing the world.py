places = ["Japan", "New Zeland", "Germany", "Canada", "Mexico"]

#Organizing temporarily a list 
print(places)
print(sorted(places))
print(places)

#organizing temporarily a list with sorted() to print the list in reverse alphabetical order
print(sorted(places, reverse=True))
print(places)

#Reversing the list
places.reverse()
print(places)
#Reversing the list again to have to original order
places.reverse()
print(places)

#Organizing the list in an alphabetical order permanently
places.sort()
print(places)

#Reversing the list permanently with .sort() method
places.sort(reverse=True)
print(places)