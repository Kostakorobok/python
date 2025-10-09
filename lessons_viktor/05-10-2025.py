import tkinter as tk
from tkinter import ttk

def feet_to_meters():
  feet = float(feet_text.get("1.0", "end-1c"))
  meters = feet * 0.3048
  result_label.config(text=f"{meters}")

def meters_to_feet():
    pass

window = tk.Tk()
window.title("Feet to Meters converter")
window.geometry("300x300")

prep_row = ttk.Label(window, width = 10, text = "Enter feet:")
prep_row.grid(row = 0, column = 0, padx = 1, pady = 1)

feet_text = tk.Text(window, height = 1, width = 45)
feet_text.grid(row = 1, column = 0, padx = 1, pady = 1)

feet_text["state"] = "normal"

convert_button = ttk.Button(window, text = "convert!", command = feet_to_meters)
convert_button.grid(row = 2, column = 0, padx = 1, pady = 1)

result_label = ttk.Label(window, text = "")
result_label.grid(row = 3, column = 0, padx = 1, pady = 1)

window.mainloop()