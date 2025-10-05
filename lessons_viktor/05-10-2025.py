import tkinter as tk
from tkinter import ttk

def feet_to_meters():
  feet = float(feet_text.get("1.0", "end-1c"))
  meters = feet * 0.3048
  result_label.config(text=f"{meters}")

window = tk.Tk()
window.title("Feet to Meters converter")
window.geometry("300x300")

prep_row = ttk.Label(window, width = 10, text = "Enter feet:")
prep_row.pack()

feet_text = tk.Text(window, height = 1, width = 45)
feet_text.pack()

feet_text["state"] = "normal"

convert_button = ttk.Button(window, text = "convert!", command = feet_to_meters)
convert_button.pack()

result_label = ttk.Label(window, text = "")
result_label.pack(pady=10)

window.mainloop()