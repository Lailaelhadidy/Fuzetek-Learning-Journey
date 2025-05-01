class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.__phone = phone
        self.__email =  email
        self.__address = address

    def get_details(self):
        return "Name: " + self.name + "\n Phone: " +  self.__phone + "\n Email: " + self.__email + "\n Address: " + self.__address

    def update_details(self, name=None, phone=None, email=None, address=None):
        if name is not None:
            self.name = name
        if phone: # if phone == if phone is not None
            self.__phone = phone
        if email:
            self.__email = email
        if address:
            self.__address = address

class ContactBook(Contact):
    def __init__(self):
        self.__contacts= []

    def add_contact(self, contact):
        self.__contacts.append(contact)

    def remove_contact(self, name):
        for i in range(len(self.__contacts)):
            if self.__contacts[i].name == name:
                self.__contacts.pop(i)
                break

    def find_contact(self, name):
        for i in range(len(self.__contacts)):
            if self.__contacts[i].name == name:
                return self.__contacts[i]
        return None

    def list_contacts(self):
        if len(self.__contacts) == 0:
            return "No contacts available."
        else:
            for i in range(len(self.__contacts)):
                print(self.__contacts[i].get_details())

book = ContactBook()
book.add_contact(Contact("Alice", "1234567890", "alice@example.com", "123 Street"))
book.add_contact(Contact("Bob", "0987654321", "bob@example.com", "456 Avenue"))

print("All Contacts:")
print(book.list_contacts())

# Output:
# All Contacts:
# Name: Alice
# Phone: 1234567890
# Email: alice@example.com
# Address: 123 Street
#
# Name: Bob
# Phone: 0987654321
# Email: bob@example.com
# Address: 456 Avenue

print("\nFinding Bob:")
contact = book.find_contact("Bob")
if contact is not None:
    print(contact.get_details())
else:
    print("Contact not found.")

# Output:
# Finding Bob:
# Name: Bob
# Phone: 0987654321
# Email: bob@example.com
# Address: 456 Avenue

book.remove_contact("Alice")
print("\nContacts after removing Alice:")
print(book.list_contacts())

# Output:
# Contacts after removing Alice:
# Name: Bob
# Phone: 0987654321
# Email: bob@example.com
# Address: 456 Avenue