# Example of array of type collection the difference between array and list is 
#List - can hold any data type
#Array will store numeric data type and must be the same type

from array import array


scores = array('d')         #array named scores
scores.append(98)           #adding a new item to the array to index 0
scores.append(99)           #adding a new item to the array to index 1

print(scores)               #will print all the array

print(scores[1])            #collection are zero-indexed will print 99

print(scores[0])            #collection are zero-indexed will print 98
