class Contact:
    def __init__(self, name, phone, email=None, category=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.category = category




class ContactManager:
    def __init__(self):
        self.contact_book = {}


    def createContact(self, name, phone, email=None, category=None):
        key = name.strip().lower()
        if key in self.contact_book:
            print("Contact already saved")
            return False
        
        self.contact_book[key] = Contact(name, phone, email, category)
        print(f"Added {name} contact successfully")
        return True


    def deleteContact(self, name):
        key = name.strip().lower()
        if key not in self.contact_book:
            print("Contact does not exist")
            return False
        
        del self.contact_book[key]
        print(f"Deleted contact {name}")
        return True


    def updateContact(self, name, new_phone=None, new_email=None, new_category=None):
        key = name.strip().lower()
        if key not in self.contact_book:
            print("Contact does not exist")
            return False

        if new_phone != None:
            self.contact_book[key].phone = new_phone
        if new_email != None:
            self.contact_book[key].email = new_email
        if new_category != None:
            self.contact_book[key].category = new_category
        return True


    def searchContact(self, query):
        if not self.contact_book:
            print("No entry in contact book rn")
            return False 

        matches = []
        for contact in self.contact_book.values():
            if query.lower() in contact.name.lower() or query == contact.phone:
                matches.append(contact)

        if not matches:
            print("Contact does not exist")
        return matches
        

    def viewContacts(self):
        if not self.contact_book:
            return 

        print("======= ALL CONTACTS =======")
        for contact in self.contact_book.values():
            print("Name: ", contact.name)
            print("Phone: ", contact.phone)
            print("Email: ", contact.email if contact.email else "N/A")
            print("Category: ", contact.category if contact.category else "N/A")


    def viewSingleContact(self, contact):
        print(f"======= CONTACT FOR {contact.name} =======")
        print("Name: ", contact.name)
        print("Phone: ", contact.phone)
        print("Email: ", contact.email if contact.email else "N/A")
        print("Category: ", contact.category if contact.category else "N/A")
    




class CLIHandler:
    def __init__(self):
        self.book = ContactManager()


    def mainMenu(self):
        print("===WELCOME TO PHONE BOOK===")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Update contact")
        print("4. Search contact")
        print("5. Delete contact")
        print("6. Exit")

        user_input = input("Please choose an option(1-6): ")

        if user_input == '6':
            return False

        elif user_input == '1':
            name = input("Please enter the name for the contact: ")
            phone = input("Please enter the phone number for the contact: ")
            email = input("Optionally enter the email for the contact or press enter: ")
            category = input("Optionally enter the category for the contact or press enter: ")
            self.book.createContact(name, phone, email, category)
            return True
        
        elif user_input == '2':
            self.book.viewContacts()
            return True
        
        elif user_input == '3':
            name = input("Please enter the name for the contact that you want to update: ")
            phone = input("Please enter the updated phone number for the contact or press enter: ").strip() or None
            email = input("Optionally enter the updated email for the contact or press enter: ").strip() or None
            category = input("Optionally enter the updated category for the contact or press enter: ").strip() or None
            self.book.updateContact(name, phone, email, category)
            return True
        
        elif user_input == '4':
            search_query = input("Please enter the name or phone for the contact: ")
            results = self.book.searchContact(search_query)
            if results and results != False:
                for contact in results:
                    self.book.viewSingleContact(contact)
                    return True

        elif user_input == '5':
            name = input("Please enter the name of the contact you wish to delete: ")
            self.book.deleteContact(name)
            return True 
        
        else:
            print("Invalid option, please select option 1-6")
            return True


    def run(self):
        running = True
        while running:
            running = self.mainMenu()





if __name__ == "__main__":
    cli = CLIHandler()
    cli.run()