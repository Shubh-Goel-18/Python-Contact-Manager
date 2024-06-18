import os

def display_menu():
    print("\nContact Book")
    print("1. Add contact")
    print("2. View contacts")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Save contacts to a file")
    print("6. Search contact by name")
    print("7. Exit")

def add_contact(contacts):
    name = input("Enter the name: ")
    phone = input("Enter the phone number: ")
    email = input("Enter the email: ")
    contacts[name] = {"phone": phone, "email": email}
    print("Contact added!")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for name, info in contacts.items():
            print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email: ")
        contacts[name] = {"phone": phone, "email": email}
        print("Contact updated!")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted!")
    else:
        print("Contact not found.")

def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, "w") as file:
        for name, info in contacts.items():
            file.write(f"{name},{info['phone']},{info['email']}\n")
    print("Contacts saved to file!")

def search_contact(contacts):
    name = input("Enter the name of the contact to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")
    else:
        print("Contact not found.")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            save_contacts(contacts)
        elif choice == "6":
            search_contact(contacts)
        elif choice == "7":
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
