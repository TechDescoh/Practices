
#set a list of names in a variable
list = ["Warrent Buffet", "King Jung Gi", "Hola Mundo"]

#use the len function to see how many values are in the list 
print(len(list))

print(list)
print(f"\n{list[1]} can't go to the dinner")

#delete a name and add other name to the list
del list[1]
list.insert(1, "Daniel Defoe")
print(f"\n{list} you're cordiately invitated to my dinner")

#Adding people to specifics place within the list
print(f"{list} I found a bigger table")
list.insert(0, "Mohammed Ali")
list.insert(2, "Bruce Lee")
list.append("Freddy Vega")
print(f"{list[0]} you're cordiately invitated to my dinner")
print(f"{list[1]} you're cordiately invitated to my dinner")
print(f"{list[2]} you're cordiately invitated to my dinner")
print(f"{list[3]} you're cordiately invitated to my dinner")
print(f"{list[4]} you're cordiately invitated to my dinner")
print(f"{list[5]} you're cordiately invitated to my dinner")

#removing people of the list
print(f"\nI apologize, the table can affort just two of you, guys")
freddy_list = list.pop()
print(f"\n{freddy_list} sorry, you're not currently invited to the dinner")
bruce_list = list.pop()
print(f"\n{bruce_list} sorry, you're not currently innvited to the dinner")
ali_list = list.pop()
print(f"\n{ali_list} sorry, you're not currently innvited to the dinner")
hola_list = list.pop()
print(f"\n{hola_list} sorry, you're not currently innvited to the dinner")

print(f"{list} you're currently invited")

#deleting two last names and getting an empty list
del list[0]
del list[0]
print(list)