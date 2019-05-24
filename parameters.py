#List is a collection which is ordered and changeable. Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#Set is a collection which is unordered and unindexed. No duplicate members.
#Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.


#list
thislist = ["apple", "banana", "cherry"]
#constructor
#thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
#print(thislist[1])



#tuple
thistuple = ("apple", "banana", "cherry")
#constructor
#thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
#print(thistuple[1])



#set
thisset = {"apple", "banana", "cherry"}

#constructor
#thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
# for x in thisset:
#   print(x)

#dict
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
#constructor
#thisdict =	dict(brand="Ford", model="Mustang", year=1964)
# x = thisdict["model"]



print(type(test));
