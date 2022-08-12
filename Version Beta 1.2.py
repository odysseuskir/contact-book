'''
Authors: Odysseus-Abraham Kirikopoulos
License: GNU General Public License v3.0
Version: 1.2 beta
'''

contact_1_name = ""
contact_1 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_2_name = ""
contact_2 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_3_name = ""
contact_3 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_4_name = ""
contact_4 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_5_name = ""
contact_5 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_6_name = ""
contact_6 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_7_name = ""
contact_7 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_8_name = ""
contact_8 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_9_name = ""
contact_9 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
contact_10_name = ""
contact_10 = {"Name": "", "Surname": "", "Phone number": "", "Home adress": ""}
operation = 0
contact_choosen = 0
option = 0

def select_contact():
    contact_choosen = input(f"Select a contact:\n{contact_1_name}\n{contact_2_name}\n{contact_3_name}\n{contact_4_name}\n{contact_5_name}\n{contact_6_name}\n{contact_7_name}\n{contact_8_name}\n{contact_9_name}\n{contact_10_name}\n")


print("Author: Odysseus-Abraham Kirikopoulos")
print("License: GNU General Public License v3.0")
print("Build Version: 1.2 Beta")

print("\nContact List\nSelect an operation")

while operation != 0:

    print("1) View your contacts\n2) View a contact's details\n3) Create a new contact\n4) Edit a contact\n5) Delete a contact\nTo exit press 0")

    operation = input()

    while True:

        if operation == 0:
            break

        elif operation == 1:
            print(f"1) {contact_1_name}\n2) {contact_2_name}\n3) {contact_3_name}\n4) {contact_4_name}\n5) {contact_5_name}\n6) {contact_6_name}\n7) {contact_7_name}\n8) {contact_8_name}\n9) {contact_9_name}\n10) {contact_10_name}\n")
            break

        elif operation == 2:

            select_contact()

            if contact_choosen == "":
                print("Err:ContactNotUsable")

            elif contact_choosen == contact_1_name:
                print(contact_1)

            elif contact_choosen == contact_2_name:
                print(contact_2)

            elif contact_choosen == contact_3_name:
                print(contact_3)

            elif contact_choosen == contact_4_name:
                print(contact_4)

            elif contact_choosen == contact_5_name:
                print(contact_5)

            elif contact_choosen == contact_6_name:
                print(contact_6)

            elif contact_choosen == contact_7_name:
                print(contact_7)

            elif contact_choosen == contact_8_name:
                print(contact_8)

            elif contact_choosen == contact_9_name:
                print(contact_9)

            elif contact_choosen == contact_10_name:
                print(contact_10)

            else:
                print("Err:ListNotFound")

        elif operation == "3":

            if contact_1_name == "":

                contact_1["Name"] = input("Enter the name of the contact: ")

                contact_1["Surname"] = input("Enter the surname of the contact: ")

                contact_1["Phone number"] = input("Enter the phone number of the contact: ")

                contact_1["Home adress"] = input("Enter the home adress of the contact: ")

                contact_1_name = f"{contact_1['Name']} {contact_1['Surname']}"

            if contact_2_name == "":

                contact_2["Name"] = input("Enter the name of the contact: ")

                contact_2["Surname"] = input("Enter the surname of the contact: ")

                contact_2["Phone number"] = input("Enter the phone number of the contact: ")

                contact_2["Home adress"] = input("Enter the home adress of the contact: ")

                contact_2_name = f"{contact_2['Name']} {contact_2['Surname']}"

            if contact_3_name == "":

                contact_3["Name"] = input("Enter the name of the contact: ")

                contact_3["Surname"] = input("Enter the surname of the contact: ")

                contact_3["Phone number"] = input("Enter the phone number of the contact: ")

                contact_3["Home adress"] = input("Enter the home adress of the contact: ")

                contact_3_name = f"{contact_3['Name']} {contact_3['Surname']}"

            if contact_4_name == "":

                contact_4["Name"] = input("Enter the name of the contact: ")

                contact_4["Surname"] = input("Enter the surname of the contact: ")

                contact_4["Phone number"] = input("Enter the phone number of the contact: ")

                contact_4["Home adress"] = input("Enter the home adress of the contact: ")

                contact_4_name = f"{contact_4['Name']} {contact_4['Surname']}"

            if contact_5_name == "":

                contact_5["Name"] = input("Enter the name of the contact: ")

                contact_5["Surname"] = input("Enter the surname of the contact: ")

                contact_5["Phone number"] = input("Enter the phone number of the contact: ")

                contact_5["Home adress"] = input("Enter the home adress of the contact: ")

                contact_5_name = f"{contact_5['Name']} {contact_5['Surname']}"

            if contact_6_name == "":

                contact_6["Name"] = input("Enter the name of the contact: ")

                contact_6["Surname"] = input("Enter the surname of the contact: ")

                contact_6["Phone number"] = input("Enter the phone number of the contact: ")

                contact_6["Home adress"] = input("Enter the home adress of the contact: ")

                contact_6_name = f"{contact_6['Name']} {contact_6['Surname']}"

            if contact_7_name == "":

                contact_7["Name"] = input("Enter the name of the contact: ")

                contact_7["Surname"] = input("Enter the surname of the contact: ")

                contact_7["Phone number"] = input("Enter the phone number of the contact: ")

                contact_7["Home adress"] = input("Enter the home adress of the contact: ")

                contact_7_name = f"{contact_7['Name']} {contact_7['Surname']}"

            if contact_8_name == "":

                contact_8["Name"] = input("Enter the name of the contact: ")

                contact_8["Surname"] = input("Enter the surname of the contact: ")

                contact_8["Phone number"] = input("Enter the phone number of the contact: ")

                contact_8["Home adress"] = input("Enter the home adress of the contact: ")

                contact_8_name = f"{contact_8['Name']} {contact_8['Surname']}"

            if contact_9_name == "":

                contact_9["Name"] = input("Enter the name of the contact: ")

                contact_9["Surname"] = input("Enter the surname of the contact: ")

                contact_9["Phone number"] = input("Enter the phone number of the contact: ")

                contact_9["Home adress"] = input("Enter the home adress of the contact: ")

                contact_9_name = f"{contact_9['Name']} {contact_9['Surname']}"

            if contact_10_name == "":

                contact_10["Name"] = input("Enter the name of the contact: ")

                contact_10["Surname"] = input("Enter the surname of the contact: ")

                contact_10["Phone number"] = input("Enter the phone number of the contact: ")

                contact_10["Home adress"] = input("Enter the home adress of the contact: ")

                contact_10_name = f"{contact_10['Name']} {contact_10['Surname']}"

            else:
                print("Err:NoFreeSpace")

        elif operation == 4:

            select_contact()

            if contact_choosen == contact_1_name:

                contact_1["Name"] = input("Enter the name of the contact: ")

                contact_1["Surname"] = input("Enter the surname of the contact: ")

                contact_1["Phone number"] = input("Enter the phone number of the contact: ")

                contact_1["Home adress"] = input("Enter the home adress of the contact: ")

                contact_1_name = f"{contact_1['Name']} {contact_1['Surname']}"

            if contact_choosen == contact_2_name:

                contact_2["Name"] = input("Enter the name of the contact: ")

                contact_2["Surname"] = input("Enter the surname of the contact: ")

                contact_2["Phone number"] = input("Enter the phone number of the contact: ")

                contact_2["Home adress"] = input("Enter the home adress of the contact: ")

                contact_2_name = f"{contact_2['Name']} {contact_2['Surname']}"

            if contact_choosen == contact_3_name:

                contact_3["Name"] = input("Enter the name of the contact: ")

                contact_3["Surname"] = input("Enter the surname of the contact: ")

                contact_3["Phone number"] = input("Enter the phone number of the contact: ")

                contact_3["Home adress"] = input("Enter the home adress of the contact: ")

                contact_3_name = f"{contact_3['Name']} {contact_3['Surname']}"

            if contact_choosen == contact_4_name:

                contact_4["Name"] = input("Enter the name of the contact: ")

                contact_4["Surname"] = input("Enter the surname of the contact: ")

                contact_4["Phone number"] = input("Enter the phone number of the contact: ")

                contact_4["Home adress"] = input("Enter the home adress of the contact: ")

                contact_4_name = f"{contact_4['Name']} {contact_4['Surname']}"

            if contact_choosen == contact_5_name:

                contact_5["Name"] = input("Enter the name of the contact: ")

                contact_5["Surname"] = input("Enter the surname of the contact: ")

                contact_5["Phone number"] = input("Enter the phone number of the contact: ")

                contact_5["Home adress"] = input("Enter the home adress of the contact: ")

                contact_5_name = f"{contact_5['Name']} {contact_5['Surname']}"

            if contact_choosen == contact_6_name:

                contact_6["Name"] = input("Enter the name of the contact: ")

                contact_6["Surname"] = input("Enter the surname of the contact: ")

                contact_6["Phone number"] = input("Enter the phone number of the contact: ")

                contact_6["Home adress"] = input("Enter the home adress of the contact: ")

                contact_6_name = f"{contact_6['Name']} {contact_6['Surname']}"

            if contact_choosen == contact_7_name:

                contact_7["Name"] = input("Enter the name of the contact: ")

                contact_7["Surname"] = input("Enter the surname of the contact: ")

                contact_7["Phone number"] = input("Enter the phone number of the contact: ")

                contact_7["Home adress"] = input("Enter the home adress of the contact: ")

                contact_7_name = f"{contact_7['Name']} {contact_7['Surname']}"

            if contact_choosen == contact_8_name:

                contact_8["Name"] = input("Enter the name of the contact: ")

                contact_8["Surname"] = input("Enter the surname of the contact: ")

                contact_8["Phone number"] = input("Enter the phone number of the contact: ")

                contact_8["Home adress"] = input("Enter the home adress of the contact: ")

                contact_8_name = f"{contact_8['Name']} {contact_8['Surname']}"

            if contact_choosen == contact_9_name:

                contact_9["Name"] = input("Enter the name of the contact: ")

                contact_9["Surname"] = input("Enter the surname of the contact: ")

                contact_9["Phone number"] = input("Enter the phone number of the contact: ")

                contact_9["Home adress"] = input("Enter the home adress of the contact: ")

                contact_9_name = f"{contact_9['Name']} {contact_9['Surname']}"

            if contact_choosen == contact_10_name:

                contact_10["Name"] = input("Enter the name of the contact: ")

                contact_10["Surname"] = input("Enter the surname of the contact: ")

                contact_10["Phone number"] = input("Enter the phone number of the contact: ")

                contact_10["Home adress"] = input("Enter the home adress of the contact: ")

                contact_10_name = f"{contact_10['Name']} {contact_10['Surname']}"

            else:
                print("Err:ListNotFound")

        elif operation == 5:

            select_contact()

            if contact_choosen == contact_1_name:

                contact_1["Name"] = ""

                contact_1["Surname"] = ""

                contact_1["Phone number"] = ""

                contact_1["Home adress"] = ""

                contact_1_name = ""
                
            if contact_choosen == contact_2_name:

                contact_2["Name"] = ""

                contact_2["Surname"] = ""

                contact_2["Phone number"] = ""

                contact_2["Home adress"] = ""

                contact_2_name = ""
                
            if contact_choosen == contact_3_name:

                contact_3["Name"] = ""

                contact_3["Surname"] = ""

                contact_3["Phone number"] = ""

                contact_3["Home adress"] = ""

                contact_3_name = ""
                
            if contact_choosen == contact_4_name:

                contact_4["Name"] = ""

                contact_4["Surname"] = ""

                contact_4["Phone number"] = ""

                contact_4["Home adress"] = ""

                contact_4_name = ""
                
            if contact_choosen == contact_5_name:

                contact_5["Name"] = ""

                contact_5["Surname"] = ""

                contact_5["Phone number"] = ""

                contact_5["Home adress"] = ""

                contact_5_name = ""
                
            if contact_choosen == contact_6_name:

                contact_6["Name"] = ""

                contact_6["Surname"] = ""

                contact_6["Phone number"] = ""

                contact_6["Home adress"] = ""

                contact_6_name = ""
                
            if contact_choosen == contact_7_name:

                contact_7["Name"] = ""

                contact_7["Surname"] = ""

                contact_7["Phone number"] = ""

                contact_7["Home adress"] = ""

                contact_7_name = ""
                
            if contact_choosen == contact_8_name:

                contact_8["Name"] = ""

                contact_8["Surname"] = ""

                contact_8["Phone number"] = ""

                contact_8["Home adress"] = ""

                contact_8_name = ""
                
            if contact_choosen == contact_9_name:

                contact_9["Name"] = ""

                contact_9["Surname"] = ""

                contact_9["Phone number"] = ""

                contact_9["Home adress"] = ""

                contact_9_name = ""
                
            if contact_choosen == contact_10_name:

                contact_10["Name"] = ""

                contact_10["Surname"] = ""

                contact_10["Phone number"] = ""

                contact_10["Home adress"] = ""

                contact_10_name = ""

            else:
                print("Err:ContactNotFound")

        else:
            print("Err:OperationNotFound")
