def farh(cel):
    return (cel *(9/5)) + 32

c = int(input("Enter a Number: "))
f = farh(c)
print("Fahreheit Temperature is " + str(f))