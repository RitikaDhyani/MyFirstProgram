x=int(input("Enter the number of words : "))
lw=[]
ll=[]
for i in range(0,x):
    x=input("Enter a word : ")
    lw.append(x)
    ll.append(len(x))
j=0
print("---------------------------")
print("Word\t=\tNo. of Characters")
print("---------------------------")
for i in lw:
    print(i,"\t=\t",ll[j])
    j=j+1
