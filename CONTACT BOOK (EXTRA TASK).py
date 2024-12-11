class Contact:
  def __init__(self, name, phone_number, email, address):
    self.name = name
    self.phone_number = phone_number
    self.email = email
    self.address = address

class ContactBook:
  def __init__(self):
    self.contacts = []

  def add_contact(self):
    name = input("Enter name: ")
    phone_number = input("Enter phone number: ")
    email = input("Enter email (optional): ")
    address = input("Enter address (optional): ")
    self.contacts.append(Contact(name, phone_number, email, address))
    print("Contact added successfully!")

  def view_contacts(self):
    if not self.contacts:
      print("Contact book is empty.")
      return

    print("Contact List:")
    for i, contact in enumerate(self.contacts, 1):
      print(f"{i}. {contact.name} - {contact.phone_number}")

  def search_contact(self):
    find = input("Enter name or phone number to search: ")
    found_contacts = [contact for contact in self.contacts if find in contact.name or find in contact.phone_number]
    if found_contacts:
      print("Search Results:")
      for contact in found_contacts:
        print(f"Name: {contact.name}")
        print(f"Phone Number: {contact.phone_number}")
        if contact.email:
          print(f"Email: {contact.email}")
        if contact.address:
          print(f"Address: {contact.address}")
        print()
    else:
      print("Contact not found.")

  def update_contact(self):
    name = input("Enter the name of the contact to update: ")
    found = False
    for i, contact in enumerate(self.contacts):
      if contact.name == name:
        found = True
        print("Enter new details:")
        new_phone_number = input("New phone number (leave blank to keep old): ")
        if new_phone_number:
          contact.phone_number = new_phone_number
        new_email = input("New email (leave blank to keep old): ")
        if new_email:
          contact.email = new_email
        new_address = input("New address (leave blank to keep old): ")
        if new_address:
          contact.address = new_address
        print("Contact updated successfully!")
        break
    if not found:
      print("Contact not found.")

  def delete_contact(self):
    name = input("Enter the name of the contact to delete: ")
    found = False
    for i, contact in enumerate(self.contacts):
      if contact.name == name:
        found = True
        self.contacts.pop(i)
        print("Contact deleted successfully!")
        break
    if not found:
      print("Contact not found.")

def main():
  contact_book = ContactBook()
  while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
      contact_book.add_contact()
    elif choice == '2':
      contact_book.view_contacts()
    elif choice == '3':
      contact_book.search_contact()
    elif choice == '4':
      contact_book.update_contact()
    elif choice == '5':
      contact_book.delete_contact()
    elif choice == '6':
      print("Exiting Contact Book...")
      break
    else:
      print("Invalid choice. Please try again.")

if __name__ == "__main__":
  main()