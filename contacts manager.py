import csv

def menue():
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")
    
    
print("====Contact Manager====")
menue()

choice = None
while choice != 4:
    
    choice = int(input("\nEnter your choice:\n"))
    fieldnames = ['Name' ,'Phone' ,'Email']
            
    if choice == 1:
        name = input("Enter name: ").strip().title()
        phone = input("Enter your phone number: ").strip()
        email = input("Enter your email adress: ").strip()            
        try:
            with open("contacts.csv", "a+", newline = "") as csv_file:
                
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                
                if csv_file.tell() == 0:
                    csv_writer.writeheader()
                
                data = {
                    "Name": name,
                    "Phone": phone,
                    "Email": email
                }
                csv_writer.writerow(data)
                
        except Exception as e:
            print("An error occurred while adding the contact:", e)
    
    elif choice == 2:
        try:
            
            contact_found = False
            phone = input("Enter your phone number to search: ").strip()
            
            with open("contacts.csv", "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                
                for line in csv_reader:
                    
                    if line["Phone"] == phone:
                        
                        print("Your contact found.")     
                        print(line)   
                        contact_found = True    
                        
                if not contact_found:
                    print("\nContact not found.")
                
        except Exception as e:
            print("An error occurred while searching the contact:", e)
            
    elif choice == 3:
        
        try:
            phone = input("Enter your phone number to delete: ").strip()
            rows = []
            found = False
            
            with open("contacts.csv", "r") as csv_file:
                
                csv_reader = csv.DictReader(csv_file,fieldnames = fieldnames)
                
                for line in csv_reader:
                    if line["Phone"] == phone:
                        found = True
                    else:
                        rows.append(line)

                if found:
                    print("Contact removed successfully.")
                else:
                    print("Contact not found.")
                    
            with open("contacts.csv", "w", newline = "") as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames = fieldnames)
                csv_writer.writerows(rows)
                
        except Exception as e:
            print("An error occurred while removing the contact:", e)
    else:
        print("Enter a valid choice...")    
        
    print()    
    menue() 
            
            
        