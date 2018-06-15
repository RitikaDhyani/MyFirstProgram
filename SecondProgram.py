#WAP to print largest number from a group of five number

while 1:
    temp=0
    large=0
    x=0
    while x < 5:
        try:
            num=int(input("Enter the number"))
            x+=1
        except ValueError as e:
            print("Oops you entered a character. We need numbers !")
            continue
        if num>large:
            large=num
        else:
            pass
    print("The largest number is ",large)
    print("Do you want to repeat ?: yes/no")
    ch=input()
    if ch=="yes":
        continue
    else:
        break
