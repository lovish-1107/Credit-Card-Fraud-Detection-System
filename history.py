import tkinter as tk
from tkinter import ttk
import sqlite3


def load_data():

    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM transactions
    ORDER BY id DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        tree.insert(
            "",
            "end",
            values=row
        )


def search_transaction():

    transaction_id = search_entry.get()

    if transaction_id == "":
        load_data()
        return

    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM transactions
    WHERE id=?
    """, (transaction_id,))

    rows = cursor.fetchall()

    conn.close()

    for row in rows:
        tree.insert(
            "",
            "end",
            values=row
        )


root = tk.Tk()

root.title("Transaction History")

root.attributes("-fullscreen", True)

root.bind(
    "<Escape>",
    lambda e: root.attributes("-fullscreen", False)
)

root.configure(bg="#020617")

heading = tk.Label(
    root,
    text="📜 Transaction History",
    font=("Helvetica", 30, "bold"),
    bg="#020617",
    fg="#00E5FF"
)

heading.pack(pady=20)

subtitle = tk.Label(
    root,
    text="View and Search Transaction Records",
    font=("Arial", 13),
    bg="#020617",
    fg="#94A3B8"
)

subtitle.pack(pady=5)

search_frame = tk.Frame(
    root,
    bg="#020617"
)

search_frame.pack(pady=20)

tk.Label(
    search_frame,
    text="Transaction ID",
    font=("Arial", 12, "bold"),
    bg="#020617",
    fg="white"
).pack(side=tk.LEFT, padx=5)

search_entry = tk.Entry(
    search_frame,
    font=("Arial", 12),
    width=20,
    bg="#1E293B",
    fg="white",
    insertbackground="white"
)

search_entry.pack(
    side=tk.LEFT,
    padx=10,
    ipady=5
)

search_btn = tk.Button(
    search_frame,
    text="🔍 Search",
    font=("Arial", 11, "bold"),
    bg="#14B8A6",
    fg="white",
    bd=0,
    cursor="hand2",
    padx=15,
    command=search_transaction
)

search_btn.pack(side=tk.LEFT, padx=5)

refresh_btn = tk.Button(
    search_frame,
    text="🔄 Refresh",
    font=("Arial", 11, "bold"),
    bg="#2563EB",
    fg="white",
    bd=0,
    cursor="hand2",
    padx=15,
    command=load_data
)

refresh_btn.pack(side=tk.LEFT, padx=5)

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
    "Amount",
    "Time",
    "Type",
    "Status",
    "Probability"
)

tree = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for col in columns:
    tree.heading(col, text=col)
    tree.column(
        col,
        width=200,
        anchor="center"
    )

tree.pack(
    fill="both",
    expand=True,
    padx=30,
    pady=20
)

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

load_data()

root.mainloop()