##1.
my_dict = {
  "Name":"Ziyang Wang",
  "Age": 21
}

'''2.
.items() returns an array of tuples with each tuple consisting of a key/value pair from the dictionary

The .keys() method returns a list of the dictionary's keys

The .values() method returns a list of the dictionary's values.
'''
print my_dict.keys()
print my_dict.values()

## 3.
for key in my_dict:
  print key,my_dict[key]
  
##4
doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

even_squares = [x**2 for x in range(1,11) if x%2 == 0]

print even_squares

'''
5
Where start describes where the slice starts (inclusive), end is where it ends (exclusive), 
and stride describes the space between items in the sliced list. For example, 
a stride of 2 would select every other item from the original list to place in the sliced list.
'''

cubes_by_four = [x ** 3 for x in range(1, 11) if ((x ** 3) % 4) == 0]
print cubes_by_four


'''
6
the default of start point is the beginning, the default of end point is the end point. The default stride is 1
'''
my_list = range(1, 11) # List of numbers 1 - 10 

print my_list[::2] ##print out all the odd numbers between 1 and 10

## 7 
backwards = my_list[::-1] #reverse the my_list

##12 : Lambda function,一种可以快速定义，但是无法重复使用的函数
languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()
print filter(lambda x : x == "Python", languages)

##16 : create a list, threes_and_fives, that consists only of the numbers between 1 and 15 (inclusive) 
## that are evenly divisible by 3 or 5.
threes_and_fives = [ x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives
squares = [x ** 2 for x in range(1, 11)]
print filter(lambda x: x >= 30 and x <= 70, squares)

##18
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter (lambda x : x != "X", garbled)
print message
 



  



