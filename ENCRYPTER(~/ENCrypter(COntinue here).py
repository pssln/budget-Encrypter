import random
import os
import string
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog
import json

# Character set for encryption and decryption
chars = string.ascii_letters + ' ' + "1234567890!@#$%^&*()_+-={}:;'<>?√,[]\\|/∑π.∆Ω∞☼☾"
chars = list(chars)

# Key files dictionary
key_files = {}
key = []  # Current loaded key
key_file = ""  # Current key file name
key_list_file = "key_files.json"  # JSON file to store key files

# Function to load the key from the selected file
def load_key(key_file):
    with open(key_file, "r", encoding="utf-8") as file:
        return list(file.read())

# Function to generate and save a new key
def create_new_key():
    file_name = simpledialog.askstring("Create New Key", "Enter a name for the new key file:",
                                    parent=root)
    
    if file_name:
        # Prompt the user to select the directory to save the key
        directory = filedialog.askdirectory(title="Select Directory to Save Key")
        
        if not directory:  # If user cancels the directory selection
            
            return
        
        # Create the full path for the new key file
        file_path = os.path.join(directory, file_name.strip() + ".txt")
        
        # Check if the file already exists in the chosen directory
        if os.path.exists(file_path):
            messagebox.showerror("Error", f"Key file '{file_path}' already exists!")
            create_new_key()
        
        # Create a unique shuffled key
        new_key = chars.copy()
        random.shuffle(new_key)
        
        # Save the new key to the specified file
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(''.join(new_key))
        
        # Add to the key list and save it
        key_number = str(len(key_files) + 1)
        key_files[key_number] = file_path
        save_key_list()
        view_key_lists()  # Save the updated key list
        #create_new_key()

# Function to add a custom key file
def add_custom_key():
    file_path = filedialog.askopenfilename(
        title="Select Key File",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    if file_path:
        if not os.path.exists(file_path):
            messagebox.showerror("Error", "File not found!")
            return
        key_name = os.path.basename(file_path)
        key_number = str(len(key_files) + 1)
        key_files[key_number] = file_path  # Add to key_files dictionary
        save_key_list()  # Save the updated key list
        
        view_key_lists()
         # Refresh the key menu

# Function to remove a key file
# Function to remove a key file
def remove_key_file():
    # Clear any previous buttons or labels
    for widget in root.winfo_children():
        widget.destroy()

    # Display heading for removing a key file
    tk.Label(root, text="Select a Key File to Remove", font=("Terminal", 28, "bold"), bg='black', fg='#00ff00').pack(pady=80)

    # Function to remove the selected key file when a button is clicked
    def on_remove_key(num):
        file_to_remove = key_files.pop(num)  # Remove the selected key from the dictionary
        
        # Check if the file exists and delete it
        if os.path.exists(file_to_remove):
            try:
                os.remove(file_to_remove)  # Delete the .txt file
            except Exception as e:
                messagebox.showerror("File Error", f"Unable to delete the file:\n{e}")
        
        save_key_list()  # Save the updated key list
        remove_key_file()  # Refresh the key menu after removal

    # Create a button for each key file
    for num, name in key_files.items():
        button = tk.Button(
            root, 
            text=f"{os.path.basename(name)}", 
            command=lambda n=num: on_remove_key(n), 
            width=20, 
            font='Terminal',
            bg='black', 
            fg='#00ff00'
        )
        button.pack(pady=5)

    # Add an "Exit" button to return to the key menu
    tk.Button(root, text="Exit", command=view_key_lists, width=20, bg='darkred', font=('Terminal',20), fg='white').pack(pady=80)

# Function to select a key and load it
def select_key_file(key_choice):
    global key, key_file
    key_file = key_files[key_choice]
    key = load_key(key_file)
    show_main_menu()  # Proceed to the encryption/decryption menu

# Function to save the key list to a JSON file
def save_key_list():
    with open(key_list_file, "w") as file:
        json.dump(key_files, file)

# Function to load the key list from the JSON file
def load_key_list():
    global key_files
    if os.path.exists(key_list_file):
        with open(key_list_file, "r") as file:
            key_files = json.load(file)

# Function to show the key selection menu with hover effect
def show_key_menu():
    root.geometry("900x550")
    root.config(bg='black') 
    root.resizable(False,False) # Black background for the window
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="budget ENCRYPTER",
              font=("Terminal", 41, "bold"),
              bg='black',
              highlightthickness=15,        # Thickness of the border
              highlightbackground='green', # Outer line color (when not focused)
              highlightcolor='white',
              fg='#00ff00').pack(pady=70)
    

    spacer = tk.Label(root, text="",bg='black', height=6)  # Height controls the vertical space
    spacer.pack()

    dick= tk.Label(root, text="yungMtro", font=("Terminal", 20, ), fg="red", bg="black")
    dick.place(x=193, y=203)   
    dick1= tk.Label(root, text="prsa or", font=("Terminal", 12,), fg="red", bg="black")
    dick1.place(x=198, y=190)   
    dick3= tk.Label(root, text="Made by", font=("Terminal", 10), fg="red", bg="black")
    dick3.place(x=200, y=180)  
    dick3= tk.Label(root, text="1101010111001", font=("Terminal", 10), fg="lightgreen", bg="black")
    dick3.place(x=600, y=200)
    dick3= tk.Label(root, text="10001001101", font=("Terminal", 10), fg="lightgreen", bg="black")
    dick3.place(x=600, y=215)
    dick3= tk.Label(root, text="0011011", font=("Terminal", 10), fg="lightgreen", bg="black")
    dick3.place(x=600, y=230)

    # Add, Remove, and Create Key Buttons
    tk.Button(root, text="START", font=('Terminal',20, 'bold'), fg='black',bg='darkgreen', command=view_key_lists, width=17).pack(pady=5)
      
    # Button to view Key Lists
    
    
    tk.Button(root, text="Exit", font=('terminal',20, 'bold'), fg='black', bg='darkred', command=root.quit, width=10).pack(pady=10)


def view_key_lists():
    root.geometry("1000x1000")
    root.resizable(True,True)
    # Clear the current window contents
    for widget in root.winfo_children():
        widget.destroy()

    # Check if key files exist
    if not key_files:
        tk.Label(root, text="No Available Key Files", font=("Terminal", 41, "bold"), bg='black', highlightthickness=15,        
                  highlightbackground='green', fg='#00ff00').pack(pady=50)
        tk.Label(root,
                  text="No keys available right now.\nAdd or Create one",
                  font=('Terminal', 20),
                  bg='black', fg='red').pack(pady=50)
        spacer = tk.Label(root, text="", bg='black', height=10)  # Height controls the vertical space
        spacer.pack()

    else:
        # Label to display the "Available Key Files"
        tk.Label(root, text="Available Key Files", font=("Terminal", 41, "bold"), bg='black', highlightthickness=15,
                  highlightbackground='green', fg='#00ff00').pack(pady=10)
        


        # Function to show the path when hovering over a key
        def show_key_path(key_choice):
            path_label.config(text=f"{key_files[key_choice]}")

        # Function to hide the path when mouse leaves a key
        def hide_key_path():
            path_label.config(text="")
            

        # Create a canvas and a frame to hold the key buttons
        canvas_frame = tk.Frame(root, bg="black")
        canvas_frame.pack(fill=tk.BOTH, expand=True)

        # Create the canvas with a specific width and height
        canvas = tk.Canvas(canvas_frame, bg="black", width=20, height=350)
        canvas.pack(side=tk.LEFT, fill=tk.X, expand=True)

        #scrollbar = tk.Scrollbar(canvas_frame, orient="horizontal", command=canvas.xview)
        #scrollbar.pack(side=tk.BOTTOM, fill=tk.X)

        #canvas.config(xscrollcommand=scrollbar.set)

        # Create a frame inside the canvas to hold the key buttons
        key_frame = tk.Frame(canvas, bg="black")
        canvas.create_window((75, 0), window=key_frame, anchor="nw")
        
        #spacer = tk.Label(root, text="", bg='black', height=5)  # Height controls the vertical space
        #spacer.pack()
        

        path_label = tk.Label(root, text="", bg='black', fg="yellow", font=("Terminal", 13))
        path_label.pack(pady=0)
        # Set the grid to arrange buttons horizontally
        column = 0  # Start from the first column
        row = 0     # Start from the first row

        # Create the buttons for each key file
        for num, name in key_files.items():
            base_name = os.path.basename(name).split('.')[0]
            button = tk.Button(key_frame, text=f"{base_name}",width='10', command=lambda n=num: select_key_file(n),
                             font='Terminal', bg='black', fg='#00ff00')
            button.grid(row=row, column=column, padx=5, pady=5)

            button.bind("<Enter>", lambda event, n=num: show_key_path(n))  # Display path when hovering over button
            button.bind("<Leave>", lambda event: hide_key_path())  # Hide path when mouse leaves button

            column += 1  # Move to the next column
            if column > 5:  # After every 5 buttons, move to the next row
                column = 0
                row += 1

        # Update the canvas scroll region after all buttons are created
        key_frame.update_idletasks()
        canvas.config(scrollregion=canvas.bbox("all"))

        # Add the Remove Key File button
        tk.Button(root, text="Remove Key File", font=('system', 20), bg='black', fg='#00ff00', command=remove_key_file, width=30).pack(pady=5)
        spacer = tk.Label(root, text="", bg='black', height=1)  # Height controls the vertical space
        spacer.pack()

    # Add the Add, Create, and Back buttons
    tk.Button(root, text="Add Key File", font=('Terminal', 20), bg='darkgreen', fg='black', command=add_custom_key, width=30).pack(pady=5)
    tk.Button(root, text="Create a New Key", font=('Terminal', 20), bg='darkgreen', fg='black', command=create_new_key, width=30).pack(pady=5)
    tk.Button(root, text="Back", command=show_key_menu, font=('Terminal', 20), bg='darkred', fg='black', width=30).pack(pady=30)

# Function to show the main menu (after selecting a key)
def show_main_menu():
    root.geometry("900x550")
    
    for widget in root.winfo_children():
        widget.destroy()

    tk.Label(root, text="Encryption/Decryption", font=("Terminal", 25, "bold"), bg='black', fg='#00ff00').pack(pady=10)
    selected_key_label = tk.Label(root, text=f"Selected Key:   {os.path.basename(key_file)}", font=("Terminal", 15), bg='black', fg='yellow')
    selected_key_label.pack(pady=10)

    # Text Entry for Encrypt/Decrypt
    tk.Label(root, text="Enter Text:",font=('Terminal',15,), bg='black', fg='#00ff00').pack()
    global text_entry
    text_entry = tk.Text(root, height=5, width=50, bg='black',font=('Terminal',18), fg='#00ff00', insertbackground='white')
    text_entry.pack(pady=10)

    tk.Label(root, text="Result:",font=('Terminal',15,), bg='black', fg='#00ff00').pack()
    global output_text
    output_text = tk.Text(root, height=5, width=50, bg='black',font=('Terminal',18), fg='#00ff00', insertbackground='white')
    output_text.pack(pady=5)

    # Buttons for Encrypt/Decrypt and Save
    button_frame = tk.Frame(root, bg='black')
    button_frame.pack(pady=10)
    tk.Button(button_frame, text="Encrypt",font=('Terminal',17), command=encrypt_text, width=12, bg='green', fg='black').grid(row=0, column=0, padx=0)
    tk.Button(button_frame, text="Decrypt",font=('Terminal',17), command=decrypt_text, width=12, bg='red', fg='black').grid(row=0, column=1, padx=0)
    tk.Button(button_frame, text="Save Encrypted Code",font=('Terminal',17), command=save_to_file, width=19, bg='black', fg='#00ff00').grid(row=0, column=2, padx=0)
    tk.Button(button_frame, text="Exit",  command=view_key_lists,font=('Terminal',17), width=10, bg='darkred', fg='black').grid(row=0, column=3, padx=0)


# Function to encrypt text
def encrypt_text():
    code = text_entry.get("1.0", tk.END).strip()
    if not code:
        messagebox.showwarning("Input Error", "Please enter text to encrypt.")
        return
    ENCcode = "".join(key[chars.index(letter)] if letter in chars else letter for letter in code)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, ENCcode)

# Function to decrypt text
def decrypt_text():
    ENCcode = text_entry.get("1.0", tk.END).strip()
    if not ENCcode:
        messagebox.showwarning("Input Error", "Please enter text to decrypt.")
        return
    code = "".join(chars[key.index(letter)] if letter in key else letter for letter in ENCcode)
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, code)

# Function to save the output to a file
def save_to_file():
    output_content = output_text.get("1.0", tk.END).strip()
    if not output_content:
        messagebox.showwarning("Save Error", "There is no encrypted or decrypted text to save.")
        return
    save_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    if save_path:
        with open(save_path, "w", encoding="utf-8") as file:
            file.write(output_content)


# Create the main GUI window
root = tk.Tk()
root.title("budget Encrypter")
root.geometry("900x600")
root.resizable(True, True)
root.config(bg='black')

# Load the saved key list when the program starts
load_key_list()

# Start with the key selection menu
show_key_menu()

# Run the GUI loop
root.mainloop()
