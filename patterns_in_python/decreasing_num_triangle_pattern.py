def decreasing_triangle():
    n= int(input("Enter a positive number: "))
    if (n<=0):
        print("enter a valid positive number")
        return
    for i in range (n):
        for j in range(1,n-i+1):
            print(j, end='')
        print()


decreasing_triangle()


# Output:
# Enter a positive number: 5
# 12345
# 1234
# 123
# 12
# 1