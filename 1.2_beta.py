'''
Authors: Odysseus-Abraham Kirikopoulos
Copyright notice: The following program is protected from European Commission, Article 17. More details: https://ec.europa.eu/commission/presscorner/detail/en/IP_21_1807
(C) ALL RIGHTS RESERVED - ODYSSEUS-ABRAHAM KIRIKOPOULOS - 2022
Version: 1.2 beta
'''

#Variables
contact_1 = ""
contact_1_full_name = ""
contact_1_phone = ""
contact_1_address = ""
contact_1_info = [contact_1_full_name , contact_1_phone , contact_1_address]
contact_2 = ""
contact_2_full_name = ""
contact_2_phone = ""
contact_2_address = ""
contact_2_info = [contact_2_full_name , contact_2_phone , contact_2_address]
contact_3 = ""
contact_3_full_name = ""
contact_3_phone = ""
contact_3_address = ""
contact_3_info = [contact_3_full_name , contact_3_phone , contact_3_address]
contact_4 = ""
contact_4_full_name = ""
contact_4_phone = ""
contact_4_address = ""
contact_4_info = [contact_4_full_name , contact_4_phone , contact_4_address]
contact_5 = ""
contact_5_full_name = ""
contact_5_phone = ""
contact_5_address = ""
contact_5_info = [contact_5_full_name , contact_5_phone , contact_5_address]
contact_6 = ""
contact_6_full_name = ""
contact_6_phone = ""
contact_6_address = ""
contact_6_info = [contact_6_full_name , contact_6_phone , contact_6_address]
contact_7 = ""
contact_7_full_name = ""
contact_7_phone = ""
contact_7_address = ""
contact_7_info = [contact_7_full_name , contact_7_phone , contact_7_address]
contact_8 = ""
contact_8_full_name = ""
contact_8_phone = ""
contact_8_address = ""
contact_8_info = [contact_8_full_name , contact_8_phone , contact_8_address]
contact_9 = ""
contact_9_full_name = ""
contact_9_phone = ""
contact_9_address = ""
contact_9_info = [contact_9_full_name , contact_9_phone , contact_9_address]
contact_10 = ""
contact_10_full_name = ""
contact_10_phone = ""
contact_10_address = ""
contact_10_info = [contact_10_full_name , contact_10_phone , contact_10_address]
options = "Select one: [Name]\n[Phone Number]\n[Address]"
contact_options = f"Select a contact to open:\n1) {contact_1}\n2) {contact_2}\n3) {contact_3}\n4) {contact_4}\n5) {contact_5}\n6) {contact_6}\n7) {contact_7}\n8) {contact_8}\n9) {contact_9}\n10) {contact_10}"
operation = 0
contact_choosen = 0
option = 0

#Startup
print("Lanching...\n")
print("Author: Odysseus-Abraham Kirikopoulos")
print("Copyrigh notice: (C) ALL RIGHTS RESERVED - ODYSSEUS ABRAHAM KIRIKOPOULOS - 2022")
print("Build Version: 1.2 Beta\n\n\n")

#Menu
print("MY CONTACT LIST")
print("You are in the main menu. Select an operation")

#Operations

while(operation != 6):
    print("1) View your contact list\n2) View a contact\n3) Create a contact\n4) Edit a contact\n5) Delete a contact\n6) Exit")
    while True:
        operation = input("Select an operation: ")

        if(operation == "1"):
            print(f"1) {contact_1}\n2) {contact_2}\n3) {contact_3}\n4) {contact_4}\n5) {contact_5}\n6) {contact_6}\n7) {contact_7}\n8) {contact_8}\n9) {contact_9}\n10) {contact_10}")
            break

        if(operation == "2"):
            print(contact_options)
            contact_choosen = input()
            if(contact_choosen == contact_1):
                print(contact_1_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_2):
                print(contact_2_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_3):
                print(contact_3_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_4):
                print(contact_4_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_5):
                print(contact_5_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_6):
                print(contact_6_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_7):
                print(contact_7_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_8):
                print(contact_8_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_9):
                print(contact_9_info)
                contact_choosen = 0
                break
            if(contact_choosen == contact_10):
                print(contact_10_info)
                contact_choosen = 0
                break
            else:
                print("Err404c: Unknown Contact")
                contact_choosen = 0
                break

        if(operation == "3"):
            if(contact_1 == ""):
                contact_1 = input("Name the contact: ")
                contact_1_full_name = input("What's the name of the contact: ")
                contact_1_phone = input("What's the phone number of the contact: ")
                contact_1_address = input("What's the address of the contact: ")
                contact_1_info = [contact_1_full_name , contact_1_phone , contact_1_address]
            elif(contact_2 == ""):
                contact_2 = input("Name the contact: ")
                contact_2_full_name = input("What's the name of the contact: ")
                contact_2_phone = input("What's the phone number of the contact: ")
                contact_2_address = input("What's the address of the contact: ")
                contact_2_info = [contact_2_full_name , contact_2_phone , contact_2_address]
            elif(contact_3 == ""):
                contact_3 = input("Name the contact: ")
                contact_3_full_name = input("What's the name of the contact: ")
                contact_3_phone = input("What's the phone number of the contact: ")
                contact_3_address = input("What's the address of the contact: ")
                contact_3_info = [contact_3_full_name , contact_3_phone , contact_3_address]
            elif(contact_4 == ""):
                contact_4 = input("Name the contact: ")
                contact_4_full_name = input("What's the name of the contact: ")
                contact_4_phone = input("What's the phone number of the contact: ")
                contact_4_address = input("What's the address of the contact: ")
                contact_4_info = [contact_4_full_name , contact_4_phone , contact_4_address]
            elif(contact_5 == ""):
                contact_5 = input("Name the contact: ")
                contact_5_full_name = input("What's the name of the contact: ")
                contact_5_phone = input("What's the phone number of the contact: ")
                contact_5_address = input("What's the address of the contact: ")
                contact_5_info = [contact_5_full_name , contact_5_phone , contact_5_address]
            elif(contact_6 == ""):
                contact_6 = input("Name the contact: ")
                contact_6_full_name = input("What's the name of the contact: ")
                contact_6_phone = input("What's the phone number of the contact: ")
                contact_6_address = input("What's the address of the contact: ")
                contact_6_info = [contact_6_full_name , contact_6_phone , contact_6_address]
            elif(contact_7 == ""):
                contact_7 = input("Name the contact: ")
                contact_7_full_name = input("What's the name of the contact: ")
                contact_7_phone = input("What's the phone number of the contact: ")
                contact_7_address = input("What's the address of the contact: ")
                contact_7_info = [contact_7_full_name , contact_7_phone , contact_7_address]
            elif(contact_8 == ""):
                contact_8 = input("Name the contact: ")
                contact_8_full_name = input("What's the name of the contact: ")
                contact_8_phone = input("What's the phone number of the contact: ")
                contact_8_address = input("What's the address of the contact: ")
                contact_8_info = [contact_8_full_name , contact_8_phone , contact_8_address]
            elif(contact_9 == ""):
                contact_9 = input("Name the contact: ")
                contact_9_full_name = input("What's the name of the contact: ")
                contact_9_phone = input("What's the phone number of the contact: ")
                contact_9_address = input("What's the address of the contact: ")
                contact_9_info = [contact_9_full_name , contact_9_phone , contact_9_address]
            elif(contact_10 == ""):
                contact_10 = input("Name the contact: ")
                contact_10_full_name = input("What's the name of the contact: ")
                contact_10_phone = input("What's the phone number of the contact: ")
                contact_10_address = input("What's the address of the contact: ")
                contact_10_info = [contact_10_full_name , contact_10_phone , contact_10_address]
            else:
                print("Err503strg: Contact limit reached")

        if(operation == "4"):
            print(contact_options)
            contact_choosen = input()
            if(contact_choosen == contact_1):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_1_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_1_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_1_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_2):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_2_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_2_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_2_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_3):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_3_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_3_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_3_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_4):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_4_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_4_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_4_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_5):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_5_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_5_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_5_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_6):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_6_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_6_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_6_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_7):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_7_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_7_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_7_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_8):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_8_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_8_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_8_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_9):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_9_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_9_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_9_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            if(contact_choosen == contact_10):
                print(options)
                option = input()
                if(option == "Name"):
                    contact_10_full_name = input("Edit the full name: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Phone Number"):
                    contact_10_phone = input("Edit the phone number: ")
                    option = 0
                    contact_choosen = 0
                    break
                if(option == "Address"):
                    contact_10_address = input("Edit the address")
                    option = 0
                    contact_choosen = 0
                    break
                else:
                    print("Err404eco: Unknown Operation")
                    break
            
            if(operation == "5"):
                print(contact_options)
                contact_choosen = input()
                if(contact_choosen == contact_1):
                    contact_1 = ""
                    contact_1_info = ""
                    contact_1_full_name = ""
                    contact_1_phone = ""
                    contact_1_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_2):
                    contact_2 = ""
                    contact_2_info = ""
                    contact_2_full_name = ""
                    contact_2_phone = ""
                    contact_2_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_3):
                    contact_3 = ""
                    contact_3_info = ""
                    contact_3_full_name = ""
                    contact_3_phone = ""
                    contact_3_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_4):
                    contact_4 = ""
                    contact_4_info = ""
                    contact_4_full_name = ""
                    contact_4_phone = ""
                    contact_4_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_5):
                    contact_5 = ""
                    contact_5_info = ""
                    contact_5_full_name = ""
                    contact_5_phone = ""
                    contact_5_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_6):
                    contact_6 = ""
                    contact_6_info = ""
                    contact_6_full_name = ""
                    contact_6_phone = ""
                    contact_6_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_7):
                    contact_7 = ""
                    contact_7_info = ""
                    contact_7_full_name = ""
                    contact_7_phone = ""
                    contact_7_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_8):
                    contact_8 = ""
                    contact_8_info = ""
                    contact_8_full_name = ""
                    contact_8_phone = ""
                    contact_8_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_9):
                    contact_9 = ""
                    contact_9_info = ""
                    contact_9_full_name = ""
                    contact_9_phone = ""
                    contact_9_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                if(contact_choosen == contact_10):
                    contact_10 = ""
                    contact_10_info = ""
                    contact_10_full_name = ""
                    contact_10_phone = ""
                    contact_10_address = ""
                    print("Everything has been deleted")
                    contact_choosen = 0
                    break
                else:
                    print("Err404dc: Unknown Contact")
                    break
            
            else:
                print("Err404op: Unknown Operation")
                break



# * (C) - ODYSSEUS ABRAHAM KIRIKOPOULOS - ALL RIGHTS RESERVED - 2022 *