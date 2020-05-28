# Example of lists of type collection the difference between array and list is 
#List - can hold any data type
#Array will store numeric data type and must be the same type

names = ['Chris','Susan']   #list with strings
scores = []                 #empty list
scores.append(98)           #adding a new item to the list to index 0
scores.append(99)           #adding a new item to the list to index 1

print(names)
print()
print(scores)

print(scores[1])            #collection are zero-indexed will print 99

print(scores[0])            #collection are zero-indexed will print 98

print (len(names))          #Get the number of the items will give the length of the array

names.insert(3, 'Bill')     #insert data to an index

print(names)

names.sort()                #Will sort the list by alfabetical

print(names)

names.insert(4, 'Justin')

presenters = names[1:3]     #Start and end index- presenters list will hold index 1 to 3

print(names)

print(presenters)