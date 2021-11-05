x = int(input("Enter a positive integer number: "))

if x == 0 or x == 1 or (x != 2 and x % 2 == 0) or (x != 3 and x % 3 == 0) or (x != 5 and x % 5 == 0) or (x != 7 and x % 7 == 0):
    print("Is not prime")
else:
    print("Is prime")    
