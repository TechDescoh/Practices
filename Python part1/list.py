#I created a list with a set of names and after that I call the elements of the list with a print()
flist = ["maría josé", "manuela", "simón", "pity"]
print(flist[0].title())
print(flist[1].title())
print(flist[2].title())
print(flist[3].title())

#With the .append() method we can add elements to a list 
flist.append('carlos')
print(flist)

#With the .insert() method we can set a value in a specific within the list 
flist.insert(0, "carlos")
print(flist)

#with the del statement we can delete an element of the list but we can use no longer that value that we remote
del flist[4]
print(flist)

#The pop() method removes the last item in a list, but it lets you work with that item after removing it
pop_flist = flist.pop()
print(flist)
print(pop_flist)

#You can use pop() to remove an item from any position in a list by including the index of the item you want to remove in parentheses.
best_friend = flist.pop(2)
print(f"My best friend is {best_friend}")

#If you only know the value of the item you want to remove, you can use the remove() method.
flist.remove("simón")
print(flist)
