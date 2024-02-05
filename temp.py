import tkinter as tk
from tkinter import messagebox

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit + 459.67) * 5/9

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return kelvin * 9/5 - 459.67

def convert_temperature():
    try:
        temperature = float(entry_temp.get())
        original_unit = combo_original_unit.get().lower()
        target_units = []

        if original_unit == 'celsius':
            target_units.append(("Fahrenheit", celsius_to_fahrenheit(temperature)))
            target_units.append(("Kelvin", celsius_to_kelvin(temperature)))
        elif original_unit == 'fahrenheit':
            target_units.append(("Celsius", fahrenheit_to_celsius(temperature)))
            target_units.append(("Kelvin", fahrenheit_to_kelvin(temperature)))
        elif original_unit == 'kelvin':
            target_units.append(("Celsius", kelvin_to_celsius(temperature)))
            target_units.append(("Fahrenheit", kelvin_to_fahrenheit(temperature)))

        result = "\n".join([f"{unit}: {value}" for unit, value in target_units])
        messagebox.showinfo("Conversion Result", result)
    except ValueError:
        messagebox.showerror("Error", "Invalid temperature value entered.")

# Create main window
root = tk.Tk()
root.title("Temperature Converter")

# Create welcome label
welcome_label = tk.Label(root, text="Welcome to Temperature Converter", font=("Helvetica", 16))
welcome_label.pack(pady=10)

# Create temperature entry
entry_temp = tk.Entry(root, width=20, font=("Helvetica", 12))
entry_temp.pack(pady=5)

# Create unit selection dropdown
options = ["Celsius", "Fahrenheit", "Kelvin"]
combo_original_unit = tk.StringVar(root)
combo_original_unit.set(options[0])  # default value
unit_dropdown = tk.OptionMenu(root, combo_original_unit, *options)
unit_dropdown.pack(pady=5)

# Create convert button
convert_button = tk.Button(root, text="Convert", command=convert_temperature, font=("Helvetica", 12))
convert_button.pack(pady=5)

# Run the main event loop
root.mainloop()
