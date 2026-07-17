import csv

FILE_NAME = "contacts.csv"
FIELDNAMES = ["Name", "Phone", "Email"]


def menu():
    print("\n===== Contact Manager =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Exit")


print("==== Contact Manager ====")

while True:
    menu()

    # Validate menu choice
    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a number between 1 and 4.")
        continue

    # -------------------- ADD CONTACT -------------------- #
    if choice == 1:
        name = input("Enter name: ").strip().title()
        phone = input("Enter phone number: ").strip()
        email = input("Enter email address: ").strip()

        try:
            with open(FILE_NAME, "a+", newline="") as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)

                # Write header only if file is empty
                if csv_file.tell() == 0:
                    csv_writer.writeheader()

                data = {
                    "Name": name,
                    "Phone": phone,
                    "Email": email
                }

                csv_writer.writerow(data)

            print("\nContact added successfully.")

        except Exception as e:
            print("An error occurred while adding the contact:", e)

    # -------------------- SEARCH CONTACT -------------------- #
    elif choice == 2:
        phone = input("Enter phone number to search: ").strip()
        contact_found = False

        try:
            with open(FILE_NAME, "r", newline="") as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    if line["Phone"] == phone:
                        contact_found = True

                        print("\nContact Found")
                        print("-" * 30)
                        print(f"Name : {line['Name']}")
                        print(f"Phone: {line['Phone']}")
                        print(f"Email: {line['Email']}")
                        print("-" * 30)

                        break

                if not contact_found:
                    print("\nContact not found.")

        except FileNotFoundError:
            print("No contacts found. Please add a contact first.")

        except Exception as e:
            print("An error occurred while searching:", e)

    # -------------------- DELETE CONTACT -------------------- #
    elif choice == 3:
        phone = input("Enter phone number to delete: ").strip()

        rows = []
        found = False

        try:
            with open(FILE_NAME, "r", newline="") as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for line in csv_reader:
                    if line["Phone"] == phone:
                        found = True
                    else:
                        rows.append(line)

            with open(FILE_NAME, "w", newline="") as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=FIELDNAMES)

                csv_writer.writeheader()
                csv_writer.writerows(rows)

            if found:
                print("\nContact removed successfully.")
            else:
                print("\nContact not found.")

        except FileNotFoundError:
            print("No contacts found.")

        except Exception as e:
            print("An error occurred while removing the contact:", e)

    # -------------------- EXIT -------------------- #
    elif choice == 4:
        print("\nThank you for using Contact Manager.")
        break

    # -------------------- INVALID CHOICE -------------------- #
    else:
        print("Please enter a valid choice (1-4).")