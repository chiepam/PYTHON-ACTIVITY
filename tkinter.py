import tkinter as tk

def on_button_click():
    label.config(text="Hello, Tkinter!")

root = tk.Tk()
root.title("Simple Tkinter App")
root.geometry("300x200")  # Set window size

label = tk.Label(root, text="Click the button!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_button_click)
button.pack()

root.mainloop()
