import tkinter as tk
from tkinter import ttk
DECIMALS = 18
INITIAL_SUPPLY = 1000
def show_output(name, symbol):
    total_supply = INITIAL_SUPPLY * (10 ** DECIMALS)
    output = tk.Toplevel()
    output.title("ERC20 Token Dashboard")
    output.geometry("500x300")
    output.configure(bg="#ebeef4")
    card = tk.Frame(
        output,
        bg="#E1E6F3",
        highlightthickness=2,
        highlightbackground="#38bdf8"
    )
    card.place(relx=0.5, rely=0.5, anchor="center", width=420, height=230)
    tk.Label(
        card,
        text="ERC20 TOKEN DETAILS",
        font=("Segoe UI", 16, "bold"),
        fg="#38bdf8",
        bg="#E0E3EB"
    ).pack(pady=15)
    info = tk.Frame(card, bg="#EAEFF8")
    info.pack(pady=10)
    def info_row(title, value):
        tk.Label(
            info,
            text=title,
            font=("Segoe UI", 11, "bold"),
            fg="#e5e7eb",
            bg="#E5E8F0"
        ).pack(anchor="w", padx=2)
        tk.Label(
            info,
            text=value,
            font=("Segoe UI", 11),
            fg="#a5f3fc",
            bg="#E5E9F1"
        ).pack(anchor="w", padx=40, pady=(0, 10))

    info_row("Token Name", name)
    info_row("Token Symbol", symbol)
    info_row("Total Supply", str(total_supply))
def submit():
    name = name_entry.get().strip()
    symbol = symbol_entry.get().strip()
    if name and symbol:
        show_output(name, symbol)
# Main Window
root = tk.Tk()
root.title("ERC20 Token Creator")
root.geometry("450x300")
root.configure(bg="#020617")

container = tk.Frame(root, bg="#020617")
container.pack(expand=True)
tk.Label(
    container,
    text="Create ERC20 Token",
    font=("Segoe UI", 18, "bold"),
    fg="#38bdf8",
    bg="#E0E1E5"
).pack(pady=20)
tk.Label(container, text="Token Name", font=("Segoe UI", 11), fg="white", bg="#020617").pack(anchor="w")
name_entry = ttk.Entry(container, width=35)
name_entry.pack(pady=5)
tk.Label(container, text="Token Symbol", font=("Segoe UI", 11), fg="white", bg="#020617").pack(anchor="w")
symbol_entry = ttk.Entry(container, width=35)
symbol_entry.pack(pady=5)
ttk.Style().configure("TButton", font=("Segoe UI", 11, "bold"), padding=6)
ttk.Button(container, text="Generate Token", command=submit).pack(pady=25)
root.mainloop()