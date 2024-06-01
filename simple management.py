class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print("Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            print("Your Contacts:")
            for contact in self.contacts:
                print(contact)
        else:
            print("Your contact list is empty.")

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if contact.name.lower() == name.lower()]
        if found_contacts:
            print("Found contacts:")
            for contact in found_contacts:
                print(contact)
        else:
            print("No contacts found with that name.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name.lower() != name.lower()]
        print("Contact deleted successfully.")


def main():
    contact_manager = ContactManager()
    while True:
        print("\nMenu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            contact = Contact(name, phone)
            contact_manager.add_contact(contact)
        elif choice == "2":
            contact_manager.view_contacts()
        elif choice == "3":
            name = input("Enter contact name to search: ")
            contact_manager.search_contact(name)
        elif choice == "4":
            name = input("Enter contact name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
