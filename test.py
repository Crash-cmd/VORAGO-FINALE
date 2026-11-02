import tkinter as tk

root = tk.Tk()
root.geometry("400x300")

# Create a sample widget
label = tk.Label(root, text="Hello, World!", font=("Arial", 16))
label.pack(pady=20)

# Force Tkinter to calculate geometry/layout before the mainloop runs
root.update_idletasks()

# Get widths
current_width = label.winfo_width()
requested_width = label.winfo_reqwidth()

print(f"Current Width: {current_width} pixels")
print(f"Requested Width: {requested_width} pixels")

root.mainloop()