import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3


def load_users():

    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT id, username
    FROM users
    """)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        tree.insert(
            "",
            "end",
            values=row
        )

    update_statistics()


def delete_user():

    selected = tree.selection()

    if not selected:

        messagebox.showerror(
            "Error",
            "Select a User"
        )

        return

    user_id = tree.item(
        selected[0]
    )["values"][0]

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id=?",
        (user_id,)
    )

    conn.commit()
    conn.close()

    messagebox.showinfo(
        "Success",
        "User Deleted Successfully"
    )

    load_users()


def update_statistics():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COUNT(*) FROM users"
    )

    total_users = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM transactions"
    )

    total_transactions = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM transactions
    WHERE prediction='Fraud'
    """)

    fraud_count = cursor.fetchone()[0]

    conn.close()

    users_label.config(
        text=f"👥 Total Users : {total_users}"
    )

    transaction_label.config(
        text=f"💳 Total Transactions : {total_transactions}"
    )

    fraud_label.config(
        text=f"🚨 Fraud Transactions : {fraud_count}"
    )


root = tk.Tk()

root.title("Admin Panel")

root.attributes("-fullscreen", True)

root.bind(
    "<Escape>",
    lambda e: root.attributes("-fullscreen", False)
)

root.configure(bg="#020617")

heading = tk.Label(
    root,
    text="👨‍💼 Admin Panel",
    font=("Helvetica", 30, "bold"),
    bg="#020617",
    fg="#00E5FF"
)

heading.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Manage Users and Monitor Fraud Statistics",
    font=("Arial", 13),
    bg="#020617",
    fg="#94A3B8"
)

subtitle.pack()

stats_frame = tk.Frame(
    root,
    bg="#0F172A",
    bd=2,
    relief="ridge"
)

stats_frame.pack(
    pady=20,
    ipadx=40,
    ipady=15
)

users_label = tk.Label(
    stats_frame,
    text="",
    font=("Arial", 13, "bold"),
    fg="#38BDF8",
    bg="#0F172A"
)

users_label.pack(pady=5)

transaction_label = tk.Label(
    stats_frame,
    text="",
    font=("Arial", 13, "bold"),
    fg="#22C55E",
    bg="#0F172A"
)

transaction_label.pack(pady=5)

fraud_label = tk.Label(
    stats_frame,
    text="",
    font=("Arial", 13, "bold"),
    fg="#EF4444",
    bg="#0F172A"
)

fraud_label.pack(pady=5)

style = ttk.Style()

style.theme_use("clam")

style.configure(
    "Treeview",
    background="#1E293B",
    foreground="white",
    fieldbackground="#1E293B",
    rowheight=35,
    font=("Arial", 11)
)

style.configure(
    "Treeview.Heading",
    background="#2563EB",
    foreground="white",
    font=("Arial", 12, "bold")
)

style.map(
    "Treeview",
    background=[("selected", "#2563EB")]
)

columns = (
    "ID",
    "Username"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

tree.heading(
    "ID",
    text="ID"
)

tree.heading(
    "Username",
    text="Username"
)

tree.column(
    "ID",
    width=150,
    anchor="center"
)

tree.column(
    "Username",
    width=400,
    anchor="center"
)

tree.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=20
)

delete_btn = tk.Button(
    root,
    text="🗑 Delete User",
    font=("Arial", 13, "bold"),
    bg="#EF4444",
    fg="white",
    bd=0,
    cursor="hand2",
    width=20,
    height=2,
    activebackground="#DC2626",
    command=delete_user
)

delete_btn.pack(pady=20)

footer = tk.Label(
    root,
    text="Press ESC to exit fullscreen",
    font=("Arial", 10),
    fg="#64748B",
    bg="#020617"
)

footer.pack(
    side="bottom",
    pady=10
)

load_users()

root.mainloop()