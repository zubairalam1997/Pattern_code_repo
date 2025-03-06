def square_pattern():
    n= int(input("Enter a number: "))
    if (n<=0):
        print("enter a valid positive number")
        return

    for i in range(n):
        for j in range(n):
            print(" * ", end="")
        print()

square_pattern()
