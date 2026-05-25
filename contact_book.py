# =========================
# CONTACT BOOK PROJECT
# =========================

contacts = []


# -------------------------
# Add Contact
# -------------------------
def add_contact():

    name = input("Enter Name: ")

    # Phone validation
    while True:
        phone = input("Enter Phone Number: ")

        if phone.isdigit() and len(phone) == 10:
            break
        else:
            print("Phone number should be 10 digits")

    # Email validation
    while True:
        email = input("Enter Email: ")

        if "@" in email and ".com" in email:
            break
        else:
            print("Email should have @ and .com")

    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!\n")


# -------------------------
# View Contacts
# -------------------------
def view_contacts():

    if len(contacts) == 0:
        print("No contacts found.\n")

    else:
        print("\n===== CONTACT LIST =====")

        for i, contact in enumerate(contacts, start=1):

            print(f"{i}. {contact['name']}")
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            print()


# -------------------------
# Search Contact
# -------------------------
def search_contact():

    search = input("Enter Name or Phone Number: ")

    for contact in contacts:

        if contact["name"] == search or contact["phone"] == search:

            print("\nContact Found")
            print("Name:", contact["name"])
            print("Phone:", contact["phone"])
            print("Email:", contact["email"])
            print("Address:", contact["address"])
            print()
            return

    print("Contact not found.\n")


# -------------------------
# Update Contact
# -------------------------
def update_contact():

    name = input("Enter Name to Update: ")

    for contact in contacts:

        if contact["name"] == name:

            # Phone validation
            while True:
                phone = input("New Phone Number: ")

                if phone.isdigit() and len(phone) == 10:
                    break
                else:
                    print("Phone number should be 10 digits")

            # Email validation
            while True:
                email = input("New Email: ")

                if "@" in email and ".com" in email:
                    break
                else:
                    print("Email should have @ and .com")

            address = input("New Address: ")

            contact["phone"] = phone
            contact["email"] = email
            contact["address"] = address

            print("Contact updated successfully!\n")
            return

    print("Contact not found.\n")


# -------------------------
# Delete Contact
# -------------------------
def delete_contact():

    name = input("Enter Name to Delete: ")

    for contact in contacts:

        if contact["name"] == name:
            contacts.remove(contact)

            print("Contact deleted successfully!\n")
            return

    print("Contact not found.\n")


# -------------------------
# Main Menu
# -------------------------
while True:

    print("===== CONTACT BOOK =====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book")
        break

    else:
        print("Invalid choice")