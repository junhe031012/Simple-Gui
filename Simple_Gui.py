import tkinter as tk
from tkinter import messagebox

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

    def submit_data(self):
        # Collect the data
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

        inventory_items = {}
        try:
            for item in inventory.split(","):
                key, value = item.strip().split(":")
                inventory_items[key.strip()] = int(value.strip())
        except Exception as e:
            messagebox.showerror("Input Error", "Inventory format incorrect. Example: Water:10, Food:5")
            return

        # Show the result
        result_message = f"Survivor Registered:\n\nName: {name}\nAge: {age}\nGender: {gender}\nLocation: ({latitude}, {longitude})\nInventory:"
        for item, qty in inventory_items.items():
            result_message += f"\n- {item}: {qty}"
        
        messagebox.showinfo("Registration Successful", result_message)

if __name__ == "__main__":
    root = tk.Tk()
    app = SurvivorApp(root)
    root.mainloop()