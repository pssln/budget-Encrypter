import random
import sys
import time
import string
import os
from datetime import datetime  # For generating unique file names based on timestamp

# Character set for encryption and decryption
chars = string.ascii_letters + ' ' + "1234567890!@#$%^&*()_+-={}:;'<>?√,[]\\|/∑π.∆Ω∞☼☾★♠♣♥♦✈⚡♜☢☣"
chars = list(chars)

# Function to load the key from the selected file
def load_key(key_file):
    with open(key_file, "r", encoding="utf-8") as file:
        return list(file.read())

# Function to generate and save a new key
def generate_and_save_key(key_file):
    key = chars.copy()
    random.shuffle(key)
    with open(key_file, "w", encoding="utf-8") as file:
        file.write(''.join(key))
    return key

# Key files to check
key_files = {
    "1": "undead.txt",
    "2": "forgotten.txt",
    "3": "sinner.txt",
    "4": "missUS.txt",
    "5": "drag33.txt",
    "6": "COMMONd3.txt"
}
terminal_width = 150

# Main program loop
while True:
    # Ask the user to select a key file
    print(".........******Y$metro******........")
    print(".........ENCRYPTION PROGRAM.........")
    print(".........******************.........")
    print("------------------------------------")
    print("Choose a number for key file:")
    print("------------------------------------")
    print("(1)............undead...............")
    print("(2)...........forgotten.............")
    print("(3)............sinner...............")
    print("(4)............missUS...............")
    print("(5)............drag33...............")
    print("(6)............COMMONd3.............")
    print("(0) to Exit")
    print("------------------------------------")
    
    choice = input("******Enter the number: ")

    # Check if the user wants to exit
    if choice == "0":
        print("-------------------------------")    
        print("Okay! Program will be shut down")
        print("-------------------------------")
        time.sleep(2)
        sys.exit()
        break

    if choice in key_files:
        key_file = key_files[choice]
        
        # Check if the selected key file exists
        if not os.path.exists(key_file):
            print("------------------------------------")
            print(f"Key file '{key_file}' is missing.")
            print("------------------------------------")
        
            print("------------------------------------------------------------------")
            print("If any key is missing, creating a new one might change the result.")
            create_new = input(f"Do you want to create a new '{key_file}'? (yes/no): ").lower()
            print("------------------------------------------------------------------")
            
            if create_new == "yes":
                generate_and_save_key(key_file)
                print("--------------------------------------------")
                print(f"Key file '{key_file}' created successfully!")
                print("--------------------------------------------")
            elif create_new == "no":
                print("-------------------------------")
                print("Okay!")
                print("-------------------------------")
                continue
            else:
                print("----------------------------------------")
                print("Invalid choice. Please enter 'yes' or 'no'.")
                print("----------------------------------------")
                time.sleep(2)
                continue
        else:
            # Load the existing key if the file is available
            key = load_key(key_file)
    else:
        print("----------------------------------------")
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
        print("----------------------------------------")
        time.sleep(2)
        continue

    # User choice for operation
    print(".........Choose an operation:.........")
    print("1........for Encrypting.........")
    print("2........for Decrypting.........")
    print("3........to Exit.........")
    
    choice = input(".........Enter Here: ")
    print("------------------")

    # Encrypting
    if choice == "1":
        code = input("Enter text to encrypt: ")
        ENCcode = ""
        for letter in code:
            index = chars.index(letter)
            ENCcode += key[index]
        
        print(f"Encrypted code is: {ENCcode}")
        
        # Ask user if they want to save the encrypted text
        save_to_file = input(f"Do you want to save the encrypted text? (yes/no): ").lower()
        
        if save_to_file == "yes":
            # Check if the KEYS! folder exists, and create it if it doesn't
            if not os.path.exists("KEYS!"):
                os.makedirs("KEYS!")
            
            # Ask for a custom filename after the user says yes
            custom_name = input(f"Enter the name for the encrypted file (e.g., 'undeadAlex'): ").strip()

            # Append the key name to the custom filename and save in KEYS! folder
            filename = f"KEYS!/{key_file.split('.')[0]}{custom_name}.txt"
            
            # Save the encrypted text to the file
            with open(filename, "w", encoding="utf-8") as file:
                file.write(ENCcode)
            print(f"Encrypted text has been saved to '{filename}'.")
        
    # Decrypting
    elif choice == "2":
        ENCcode = input("Enter text to decrypt: ")
        code = ""
        for letter in ENCcode:
            index = key.index(letter)
            code += chars[index]
        print(f"Original code is: {code}")

    # Exit the loop
    elif choice == "3":
        print("Goodbye!")
        break  # Exit the loop

    # Handle invalid input
    else:
        print("----------------------------------------")
        print("Invalid choice. Please enter 1, 2, or 3.")
        print("----------------------------------------")
        time.sleep(2)
        continue

    # Ask if the user wants to continue
    continue_choice = input("\nDo you want to perform another operation? (yes/no): ").lower()
    if continue_choice == "no":
        print("Thank you for using the program. Goodbye!")
        break  # Exit if the user doesn't want to continue
