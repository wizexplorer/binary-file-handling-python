import pickle
def create():
    f=open('stock.dat','wb')
    num=int(input("\t   Enter the number of items to add : "))
    for i in range(num):
        icode = input("\t       Enter the item code  : ")
        itemName = input("\t       Enter the item name  : ")
        unitPrice = float(input("\t       Enter the item price : "))
        print("-"*65)
        l=[icode, itemName, unitPrice]
        pickle.dump(l,f)
    print("\t\t     Items successfully added")
    f.close()

def display():
    f=open('stock.dat','rb')
    try:
        while True:
            x=pickle.load(f)
            print('\t\t     Item Code  :', x[0])
            print('\t\t     Item Name  :', x[1])
            print('\t\t     Unit Price :', x[2])
            print()
    except:
        f.close()

def search(detail):
    f=open('stock.dat','rb')
    try:
        while True:
            x=pickle.load(f)
            if x[1]==detail:
                print("")
                print('\t\t     Item Code  :', x[0])
                print('\t\t     Item Name  :', x[1])
                print('\t\t     Unit Price :', x[2])
    except:
        f.close()

def delete(detail):
    f=open('stock.dat','rb')
    f1=open('temp.dat','wb')
    try:
        while True:
            x=pickle.load(f)
            if x[1]!=detail:
                pickle.dump(x,f1)
            else:
                continue
    except:
        f.close()
        f1.close()
        import os
        os.remove('stock.dat')
        os.rename('temp.dat','stock.dat')
    print("-"*65)    
    print("\t\t        Record Deleted Successfully")

def update(detail):
    f=open('stock.dat','rb')
    f1=open('temp.dat','wb')
    try:
        while True:
            x=pickle.load(f)
            if x[1]!=detail:
                pickle.dump(x,f1)
            else:
                x[2] = float(input("\t        Enter the new price : "))
                pickle.dump(x,f1)
    except:
        f.close()
        f1.close()
        import os
        os.remove('stock.dat')
        os.rename('temp.dat','stock.dat')
    print("-"*65)
    print("\t\t        Record Updated Successfully")

choice='0'
print("|----------------------EXPERIMENT NO.06-------------------------|")
print("|                    BINARY FILE HANDLING                       |")
while(choice!='6'):
    print("*"*65)
    print("\t\t 1: Create a record")
    print("\t\t 2: Display records")
    print("\t\t 3: Search a record")
    print("\t\t 4: Delete a record")
    print("\t\t 5: Update a record")
    print("\t\t 6: EXIT")
    choice=input("\t\t  Enter your choice : ")
    print("*"*65)
    if choice == '1':
        create()
    elif choice == '2':
        display()
    elif choice == '3':
        detail=input("   Enter the name of item to serach : ")
        search(detail)
    elif choice == '4':
        detail=input("   Enter the name of item to delete : ")
        delete(detail)
    elif choice == '5':
        detail=input("   Enter the name of item to update : ")
        update(detail)
    elif choice not in ['1','2','3','4','5','6']:
        print("\t    Wrong input; input numbers from 1 to 6")
else :
    print("\t\t-->Exiting loop")
