i=1
a=True
dict={}
while(a==True):
    x=input("Enter the element for key{} in the dictionary: ".format(i))
    dict[i]=x
    i+=1
    inp=input("Do you want to enter another element?(yes/no): ")
    if inp=='yes':
        a=True
    else:
        a=False

b=True
while (b==True):
    m=int(input("Enter the value of i to delete the ith entry: "))
    dict.pop(m)
    inp=input("Do you want to repeat the process?: ")
    if inp=='yes':
        b=True
    else:
        b=False

print("The modified dictionary elements are :")
for i in dict:
    print(dict[i])
