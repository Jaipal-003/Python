myDict = {
    "fast" : "In a Quick Manner",
    "harry" :"A Coder",
    "marks" : [1,25,36,45,45],
    "anotherdict" : {"harry" : "Player"
    }

}
# Dictionary Methods

print(list(myDict.keys()))  # Prints the keys of he dictionary
print(myDict.values()) # Prints the values of he dictionary
print(myDict.items ()) # Prints the (keys,values) for all contents of he dictionary
 
print(myDict)
updateDict = {
    "lovish" : "Friend" ,
    "Jason" : "Friend",
    "harry" :"A Dancer"
}
myDict.update(updateDict)   # Updates the dictionary by adding key-value  pairs froem updateDict
print(myDict)  


print(myDict.get("harry")) # Prints value associated with key "harry"
print(myDict["harry"]) # Prints value associated with key "harry"

# The diffreance between .get and [] syntax in Dictinaries?

print(myDict.get("harry2"))  #Returns None as harry2 is not present in the dictionary
# print(myDict["harry2"])      # Throws an error as harry2 is not present in the dictionary 

