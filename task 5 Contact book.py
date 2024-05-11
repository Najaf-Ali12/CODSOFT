contact_book={"najaf":{"number":"03121348757", "email":"zoroaster876@gmail.com","address":"Dadu"},
              "aftab":{"number":"03121345767", "email":"aftab@gmail.com", "address":"jamshoro"}}
def Add():
    name=input("Enter the name of new contact:").lower()
    number=input(f"Enter the number of {name}:")
    email=input(f"Enter the email of {name}:").lower()
    address=input(f"Enter the address of {name}:").lower()
    contact_book[name]={"number":number,"email":email,"address":address}
def View():
    for name,detail in contact_book.items():
        print(name,":",detail["number"])
def Search():
    way=input("Enter\n1 if want to search contact using name\n2 if want to search contact using number:")
    if way=="1":
        name=input("Enter the name of the contact you want to search:").lower()
        if name in contact_book.keys():
            print(contact_book[name])
        else:
            print("Sorry that contact is not included in contact book")
    elif way=="2":
        number=input("Enter the number of the contact whom you want to search:")
        for name,info in contact_book.items():
            if info["number"]==number:
                print(name,":",contact_book[name])
                break
        else:
            print("Sorry that numebr is not included in the contact book")
    else:
        print("Enter nothing except 1 or 2")
        Search()
def Update():
    list_of_data=["number","email","address"]
    name=input("Enter the name whose data you want to update:").lower()
    if name in contact_book.keys():
        ask=input(f"Enter which thing from (email,number,address) you want to update of {name}:").lower()
        if ask in list_of_data:
            update=input(f"Enter the updated {ask} of {name}:").lower()
            contact_book[name][ask]=update
            print(f"{ask} is updated")
        elif ask=="name":
            print("you cannot change name")
            Update()
        else:
            print(f"you can only update email,number or address of {name}")
            Update()
    else:
        print("that name is not in the contact_book")
        Update()
def Delete():
    name=input("Enter the name of the contact whom you want to delete:")
    if name in contact_book.keys():
        del contact_book[name]
        print(f"{name} has been deleted from the contact_book")
    else:
        print("that name is not in the contact book")
        Delete()
while True:
    choice=input("what you want to do\n1:Add a contact\n2:view list of contact names and numbers\n3:Search a contact\n4:Update contact\n5:delete contact\n6:Exit\nEnter 1,2,3,4,5 or 6:")
    if choice=="1":
        Add()
    elif choice=="2":
        View()
    elif choice=="3":
        Search()
    elif choice=="4":
        Update()
    elif choice=="5":
        Delete()
    elif choice=="6":
        break
    else:
        print("INVALID CHOICE")
    
