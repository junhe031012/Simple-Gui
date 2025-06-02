import tkinter as tk
from tkinter import messagebox
import csv
import os

class SurvivorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Survivor Registration")

        # Create Labels and Entry widgets
        tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=5, sticky='e')
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(root, text="Age:").grid(row=1, column=0, padx=10, pady=5, sticky='e')
        self.age_entry = tk.Entry(root)
        self.age_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(root, text="Gender:").grid(row=2, column=0, padx=10, pady=5, sticky='e')
        self.gender_entry = tk.Entry(root)
        self.gender_entry.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(root, text="Latitude:").grid(row=3, column=0, padx=10, pady=5, sticky='e')
        self.latitude_entry = tk.Entry(root)
        self.latitude_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Label(root, text="Longitude:").grid(row=4, column=0, padx=10, pady=5, sticky='e')
        self.longitude_entry = tk.Entry(root)
        self.longitude_entry.grid(row=4, column=1, padx=10, pady=5)

        tk.Label(root, text="Inventory (item:quantity, separate by comma):").grid(row=5, column=0, columnspan=2, padx=10, pady=5)
        self.inventory_entry = tk.Entry(root, width=40)
        self.inventory_entry.grid(row=6, column=0, columnspan=2, padx=10, pady=5)

        # Submit Button
        submit_button = tk.Button(root, text="Submit", command=self.submit_data)
        submit_button.grid(row=7, column=0, columnspan=2, pady=10)

        # CSV file path
        self.csv_file = 'survivors_data.csv'

        # Check if file exists, if not, create header
        if not os.path.exists(self.csv_file):
            with open(self.csv_file, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Age', 'Gender', 'Latitude', 'Longitude', 'Inventory'])

    def submit_data(self):
        name = self.name_entry.get()
        age = self.age_entry.get()
        gender = self.gender_entry.get()
        latitude = self.latitude_entry.get()
        longitude = self.longitude_entry.get()
        inventory = self.inventory_entry.get()

        if not (name and age and gender and latitude and longitude and inventory):
            messagebox.showerror("Input Error", "All fields are required.")
            return

        try:
            age = int(age)
            latitude = float(latitude)
            longitude = float(longitude)
        except ValueError:
            messagebox.showerror("Input Error", "Age must be integer; Latitude and Longitude must be float.")
            return

        # Save data into CSV
        with open(self.csv_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, gender, latitude, longitude, inventory])

        messagebox.showinfo("Success", f"Survivor {name} has been registered successfully!")

        # Clear inputs after successful submission
        self.clear_inputs()

    def clear_inputs(self):
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.gender_entry.delete(0, tk.END)
        self.latitude_entry.delete(0, tk.END)
        self.longitude_entry.delete(0, tk.END)
        self.inventory_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = SurvivorApp(root)
    root.mainloop()
