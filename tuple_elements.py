tuple = ("C","C++","Java","Python","R")
a=True
print("the tuple has five elements")
while (a==True):
    
    inp=int(input("To view the ith element of the tuple enter the value of i: "))
    print(tuple[inp-1])
    x=input("Do you want to run the process again?(yes/no): ")
    if x=='yes':
        a=True
    elif x=='no':
        a=False
    else:
        print("inalid entry!")
        a=False
