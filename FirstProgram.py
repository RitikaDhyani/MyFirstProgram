print("Program: Even or Odd")
while 1:
    x=int(input("Enter the number : "))
    if x%2==0:
        print("The given no is even")
    else:
        print("The given no is odd")
    print("Do you want to repeat ?: yes/no")
    ch=input()
    if ch=="yes":
        continue
    else:
        break


