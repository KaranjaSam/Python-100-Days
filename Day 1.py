#Exercise 1

print("Day 1 -string manipulation")

print("string concatenation is done with the '+' sign.")

print('e.g. print("hello " + "world")')

print("new lines can be created with a backslash and .n sign")



#Input()will get user input in console
#Then print() will print the word "hello" and the user input

print("weeeee" + input("Mambo gani haya?"))




#Exercise 2
#code to print the number of characters in a user's name
#the len() function calculates the length of a string after the input() function is executed

x = input("what is your name?")
print(len(x))

print(len(input("what is your name?")))   #this can also be used to count hwo many characters are in a string


#Exercise 3
#code to switch the values stored in variables a and b

a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print(a)
print(b)




#Day 1 Project
#code to generate a band name
#the \n is used to create a new line
print(" WELCOME TO BAND NAME GENERATOR")
city_name = input("what is the name of the city you grew up in ?\n")
pet_name = input("what is the name of your pet ?\n")

#prints the band name 
#the " " is used to add a space between the two strings
print("your band name could be: \n"  + city_name + " " +  pet_name)

