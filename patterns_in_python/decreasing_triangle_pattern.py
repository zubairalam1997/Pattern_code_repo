def decreasing_triangle():
    n= int(input("Enter a positive number: "))
    if (n<=0):
        print("enter a valid positive number")
        return
    for i in range (n):
        for j in range(n-i):
            print("*", end='')
        print()


decreasing_triangle()

# output:
# Enter a positive number: 5
# *****
# ****
# ***
# **
# *