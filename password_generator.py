

# P A S S W O R D     G E N E R A T O R

import tkinter as tk
import random

class PasswordGenerator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator")
        self.window.geometry("400x250")  # Set the window size to 400x250
        self.window.configure(background="RoyalBlue1")  # RoyalBlue1 background

        self.label = tk.Label(self.window, text="PASSWORD GENERATOR", font=("Arial Black", 18, "bold"),
        fg="#fff", bg="RoyalBlue1", relief="ridge", borderwidth=2)  # white font on RoyalBlue1 background with a ridge border
        self.label.pack(pady=10)

        self.password_length_label = tk.Label(self.window, text="Length of password:", font=("Arial", 12),
        fg="#fff", bg="RoyalBlue1", relief="ridge", borderwidth=1)  # white font on RoyalBlue1 background with a ridge border
        self.password_length_label.pack()
        self.password_length_entry = tk.Entry(self.window, width=20, font=("Arial", 12), fg="#333", bg="#fff",
        relief="ridge", borderwidth=1)  # white background with dark gray font and a ridge border
        self.password_length_entry.pack()

        self.generate_button = tk.Button(self.window, text="Generate Password", command=self.generate_password,
        font=("Arial Black", 12, "bold"), fg="RoyalBlue1", bg="#fff", relief="ridge", borderwidth=2)  
        self.generate_button.pack(pady=10)

        self.password_label = tk.Label(self.window, text="", font=("Arial", 16), fg="#fff", bg="RoyalBlue1",
        relief="ridge", borderwidth=2)  # white font on RoyalBlue1 background with a ridge border
        self.password_label.pack()

    def generate_password(self):
        uppercase_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        lowercase_letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]
        digits = [str(i) for i in range(10)]
        special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '_']
        all_characters = uppercase_letters + lowercase_letters + digits + special_characters

        password_length = int(self.password_length_entry.get())
        password_list = random.sample(all_characters, password_length)
        password = ''.join(password_list)

        self.password_label.config(text="Your password is: " + password)

    def run(self):
        self.window.mainloop()

generator = PasswordGenerator()
generator.run()