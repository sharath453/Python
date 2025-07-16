# declare
name2="Sharath"
print(name2[-1])  #it will print the last letter so that python have negative indexing also

# String is imutable -- it cannot be changed once assigned


''' 
-- starting value is always less than the ending
-- default increment value is 1
-- this is how the indexing is happen

 +---+---+---+---+---+---+
 | P | y | t | h | o | n |
 +---+---+---+---+---+---+
 0   1   2   3   4   5   6
-6  -5  -4  -3  -2  -1

 '''

#String slicing or indexing 
name1="Sharath"
print(name1[3:7])  #starts printing 3 to all the way till 7 (Exclusing 3)
print(name1[:4])  #same as 0 : 4
print(name1[0:])  #same as 0 : 4 

'''Note how the start is always included, and the end always excluded.
This makes sure that s[:i] + s[i:] is always equal to s:'''
print(name1[:3]+name1[3:])  #output : Sharath
print(name1[-7:]) #Sharath

print(name1[::-2])
print(name1[4::1]+name1[0:4:1])  #output : athShar


#String Functions
name="SHARATH"
print(len(name)) #this function helps to find the length of the String
print(name.endswith('a'))  #it will cheeck whether String ends with given char if yes it will print (True) else (False)
print(name.startswith('s')) #it is opposite to endswith function both are case sensitive
print(name.capitalize())  # it will convert first letter into capitial(only first alphabet)
print(name.lower())  #convert entair String into lower
print(name.upper()) #convert the entair String into a upper 
print(name.strip()) #This method will remove all the white spaces wxceepy in b/w the letters living 

print(name.replace('sHARATH', 'Dinesh'))  #it will replace the present String in the sentance or char from the given String or a char
print(name.split()) #this will split the string to separe Strings
print(name.casefold()) #converts all the charters to lower case but it is different from lower()

print('_'*50)
alpha="Manoj"
print(alpha.isalpha()) #Returns True if all characters in the string are in the alphabet


#escape sequence
print('hi it\'s me') 
mysore="mysore is a big city \ni love mysore very much"  #/n is the new line indication
print(r"hi i am sharath\ni am a good boy")  #If you don’t want characters prefaced by \ to be interpreted as special characters, use 'r' n the statement so that every thing is gone a prrint

name3=("sharath A L is going to mymbai for some reason" r"\nhe is gone a meet his friend")
print(name3)  #output : sharath A L is going to mymbai for some reason\nhe is gone a meet his friend

myname="sharath" *3 + 'A L'
print(myname)   #output : sharathsharathsharathDeepashree

p="SHarath" "A L"  #Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
print(p) #output : SHarathA L

print('-'*30)

# Loop through the letters in the word "banana":
for i in "Banana":
    print(i)

print("_"*50)

#check the particular string is their or not 
data="Sharath is a good boy"
print("Good" in data)  #false

if "Sharath" in data:
    print(f"yes u are finding term is their")

#how to delete the String in python 
s="sony"
del s  #s variable is deeted, if we try to pprint it it will through the error


#convert the intergeree into a string
a=65
b=str(a)  #better to use this their are may types to do
b="{}".format(a) 
print(type(b))  #converted into string

#accessing a elements of String
a="manoj"

# method 1 
for i in a:
    print(i)

for i, j in enumerate(a):
    print(f"Index {i} : {j}")
