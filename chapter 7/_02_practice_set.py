# Write a program to find whether a given number is prime or not


num = int(input("Enter the number :"))
prime = True

for i in range (2,num):
    if(num%i == 0):
        prime = False
        break
if prime:
    print("This is prime")
else:
    print("This number is not prime")        


