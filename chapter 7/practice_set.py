# Write a program to print multiplication table of a given number using for loop


# num = int(input("Enter the Number\n"))
# for i in range(1,11):
#     # print(str(num) + "X" + str(i) + "=" + str(num*i))
#      print(f"{num}x{i}={num*i}")


#  Write a program to greet all the person names strated in a list l1 and which starts with S


l1 = ["Harry","Sohan","Sachan","Rahul"]
for name in l1:
    if name.startswith("S"):
       print("Hello " + name)