from tkinter import *

# ---------------- SMART CONTRACT SIMULATION ----------------
class SimpleStorage:
    def __init__(self):
        self.stored_value = 0  # Simulated blockchain storage

    def set(self, value):
        self.stored_value = value

    def get(self):
        return self.stored_value


# Create contract object
contract = SimpleStorage()

# ---------------- GUI FUNCTIONS ----------------
def store_value():
    try:
        value = int(entry.get())
        contract.set(value)
        status_label.config(text="Value stored successfully ✔", fg="green")
    except:
        status_label.config(text="Please enter a valid number ❌", fg="red")

def get_value():
    value = contract.get()
    result_label.config(text=f"Stored Value: {value}")


# ---------------- GUI DESIGN ----------------
root = Tk()
root.title("Simple Storage Smart Contract (Python Simulation)")
root.geometry("420x300")

Label(root, text="Simple Storage Smart Contract", font=("Arial", 14, "bold")).pack(pady=10)

Label(root, text="Enter Value").pack()
entry = Entry(root, width=25)
entry.pack(pady=5)

Button(root, text="Store Value", width=20, command=store_value).pack(pady=10)
Button(root, text="Get Value", width=20, command=get_value).pack(pady=5)

status_label = Label(root, text="")
status_label.pack(pady=5)

result_label = Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()