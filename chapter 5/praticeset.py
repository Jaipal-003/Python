# Program to Create a Dictionary of hindu words

myDict = {
    "Pankha" :  "Fan",
    "Dabba" : "Box" ,
    "Vastu" : "Item"
}
# print("Options are ", myDict.keys())
# a = input("Enter the hindi Word\n")
# print("The meaning of your word is:" , myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
# print("The meaning of your word is:" , myDict.get(a))


# Program to inputright numbers from the user and display all the Unique numbers(once)


# num1 = int(input("Enter a Number 1\n"))
# num2 = int(input("Enter a Number 2\n"))
# num3 = int(input("Enter a Number 3\n"))
# num4 = int(input("Enter a Number 4\n"))
# num5 = int(input("Enter a Number 5\n"))
# num6 = int(input("Enter a Number 6\n"))
# num7 = int(input("Enter a Number 7\n"))
# num8 = int(input("Enter a Number 8\n"))

# s = {num1,num2,num3,num4,num5,num6,num7,num8}
# print(s)


# Can we have a set with 18(int)  and "18"(string) as a values in it?

# s = {18, "18" ,18.1}
# print(s)



# What will be the length of following set s:

# s = set()
# s.add(20)
# s.add("20")
# s.add(20.0)
# print(len(s))

# What is the type of s ={}


# s ={}
# print(type(s))


# Create an empty dictionary .Allow 4 Friends to enter their favourite langueage as values and use keys as their names .Assume that the names are unique

Favlang = {}
a = input("Enter your Favorite language Shubham\n")
b = input("Enter your Favorite language Jason\n")
c = input("Enter your Favorite language Madhav\n")
d = input("Enter your Favorite language Ishan\n")
Favlang["shubham"] = a      
Favlang["Jason"] = b
Favlang["Madhav"] = c
Favlang["Ishan"] = d
 
print(Favlang)


