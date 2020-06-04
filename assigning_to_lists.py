list1=[]
list2=[]
print("There are two lists")
a=True
while (a==True):
    inp1=input("Do you want to enter an element in any list?(yes/no): ")
    if inp1=='yes':
        b=True
        while (b==True):
            inp2=input("In which list do you want to enter an element? (1 / 2): ")
            if inp2=='1':
                inp3=input("please enter the element: ")
                list1.append(inp3)
                b=False
            elif inp2=='2':
                inp3=input("please enter the element: ")
                list2.append(inp3)
                b=False
            else:
                print("Invalid entry\n Try again!")
    elif inp1=='no':
        a=False
    else:
        print("Invalid entry\n Try again!")

print("list 1 :",list1)
print("list 2 :",list2)
        
        
                
        
