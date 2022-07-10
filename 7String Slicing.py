#String :- Combination of character is known as String

# Three types of strings in Python :
# 1) Single Quote String – (‘Single Quote String’)
# 2) Double Quote String – (“Double Quote String”)
# 3) Triple Quote String – (‘’’ Triple Quote String ‘’’)

# Print the string

har1 = "Harshit is a good boy"
print(har1)

# String Slicing
# In python index start with zero (0)
# If you need a single character so use this method []

an1 = "Ankit"
print(an1[2])

# If you need multiple character so use this method [ Incliding: Excluding ]

rse = "Renu Singh"
print(rse[0:4])

# Length Function :- len()

p = "Anjani"
print(len(p))

# Advanced String Slicing

j = "Lucknow is a city of nawab"
print(j[0:7:3])

# Negative Index

l = "Integral University"
print(l[-1:-11:-1])

# String Function's
#1) type ()

n= "Anjani Kumar Singh"
print(type(n))

#2) .isalnum():- Gives true and false value
#) If sentence has a space so it gives False

n2= "Anjani Kumar Singh"
print(n2.isalnum())

#) If sentence has no space so it gives True

n3= "AnjaniKumarSingh"
print(n3.isalnum())

#3) .isalpha
#) isalpha() returns True if all characters are letters.

n4= "AnjaniKumarSingh"
print(n4.isalpha())

#4) .endswith()
#)It's checks weather the last sentence is similar or not

n5= "Anjani Kumar Singh"
print(n5.endswith("Singh"))

#5) .count()

n6= "Anjani Kumar Singh"
print(n6.count("a"))

#6) .capitalize()

n7= "Anjani Kumar Singh"
print(n7.capitalize())

#7) .find()
# It helps to find the sentence and give the index value

n8= "Anjani Kumar Singh"
print(n8.find("Kumar"))

#8) .casefold
#Converts string into lower case
n9 = "Harshit Singh"
print(n9.casefold())

#9) .center()
#Returns a centered string . Its add the space ()

n10 = "Anjani Kumar Singh"
print(n10.center(50))

#10) .encode()
#Returns an encoded version of the string

n11  = "My name is Stale"
print(n11.encode())

#11) .index
# Searches the string for a specified value and returns the position of where it was found

n12 = "Harshit Singh"
print(n12.index("Singh"))

#12) .isdigit()
# Returns True if all characters in the string are digits

n13 = "87897"
print(n13.isdigit())

#13) .islower()
#) Returns True if all characters in the string are lower case

n14 = "harshit singh"
print(n14.islower())

# 14) .istitle()
# The title() function in python is the Python String Method which is used to convert the first character
# in each word to Uppercase and remaining characters to Lowercase in the string and returns a new string.
# Returns True and False

print( 'The Hilton'.istitle() )


# Important Question

# 1) Check if a string contains a specific substring :- String inside the String
# The in operator will return True if a string contains a substring.

# print( 'plane' in 'The worlds fastest plane' ) #=> True
# print( 'car' in 'The worlds fastest plane' ) #=> False


# 2) Search a specific part of a string for a substring

# 'the happiest person in the whole wide world.'.index('the',10,44)
#=> 23


# 3) Interpolate a variable into a string using format()
# format() is similar to using an f-string.

# difficulty = 'easy'
# thing = 'exam'
# 'That {} was {}!'.format(thing, difficulty)
# #=> 'That exam was easy!'


# 4) Split a string on a specific character

# 'This is great'.split(' ')
# #=> ['This', 'is', 'great']


# 5 Can an integer be added to a string in Python?

# Type Error


# 6) Join a list of strings into a single string, delimited by hyphens

# '-'.join(['a','b','c'])
# #=> 'a-b-c'


# 7) When would you use splitlines()?

# sentence = "It was a stormy night\nThe house creeked\nThe wind blew."
# sentence.splitlines()
# #=> ['It was a stormy night', 'The house creeked', 'The wind blew.']


# 8)  Replace all instances of a substring in a string

# sentence = 'Sally sells sea shells by the sea shore'
# sentence.replace('sea', 'mountain')
# #=> 'Sally sells mountain shells by the mountain shore'


# 10)  Remove whitespace from the left, right or both sides of a string
# lstrip(), rstrip() and strip()

# string = '  string of whitespace    '
# string.lstrip() #=> 'string of whitespace    '  #Starting
# string.rstrip() #=> '  string of whitespace'  #Ending
# string.strip() #=> 'string of whitespace'


# 11) startswith()

# city = 'New York'
# city.startswith('New') #=> True
# city.endswith('N') #=> False


# 12) Capitalize the first character of each word in a string
# title() will capitalize each word in a string.

# 'once upon a time'.title()


# 13) Give an example of using the partition() function

# sentence = "If you want to be a ninja"
# print(sentence.partition(' want '))
# #=> ('If you', ' want ', 'to be a ninja')


#  14) When would you use rfind()?

# The rfind() method finds the last occurrence of the specified value.
# The rfind() method returns -1 if the value is not found

# story = 'The price is right said Bob. The price is right.'
# story.rfind('is')
# #=> 39


# 15)  Remove vowels from a string?

# class Solution(object):
#    def removeVowels(self, s):
#       s = s.replace("a","")
#       s = s.replace("e","")
#       s = s.replace("i","")
#       s = s.replace("o","")
#       s = s.replace("u","")
#       return s
# ob1 = Solution()
# print(ob1.removeVowels("iloveprogramming"))