import tkinter as tk
from tkinter import messagebox
import sqlite3


def login():
    username = username_entry.get()
    password = password_entry.get()

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE username=? AND password=?
    """, (username, password))

    user = cursor.fetchone()
    conn.close()

    if user:
        messagebox.showinfo("Success", "Login Successful")
        root.destroy()
        import dashboard
    else:
        messagebox.showerror("Error", "Invalid Username or Password")


# ---------------- MAIN WINDOW ----------------
root = tk.Tk()
root.title("Login System")

# FULLSCREEN ENABLE
root.attributes("-fullscreen", True)

# ESC to exit fullscreen
root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

root.configure(bg="#0f172a")


# ---------------- CENTER CARD ----------------
card = tk.Frame(root, bg="#111827")
card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=420)


# Title
title = tk.Label(
    card,
    text="Welcome Back 👋",
    font=("Helvetica", 22, "bold"),
    bg="#111827",
    fg="#38bdf8"
)
title.pack(pady=25)

subtitle = tk.Label(
    card,
    text="Login to continue",
    font=("Arial", 11),
    bg="#111827",
    fg="#9ca3af"
)
subtitle.pack()


# Username Label
tk.Label(
    card,
    text="Username",
    font=("Arial", 11, "bold"),
    bg="#111827",
    fg="white"
).pack(pady=(25, 5))


username_entry = tk.Entry(
    card,
    width=30,
    bg="#1f2937",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Arial", 11)
)
username_entry.pack(ipady=6)


# Password Label
tk.Label(
    card,
    text="Password",
    font=("Arial", 11, "bold"),
    bg="#111827",
    fg="white"
).pack(pady=(20, 5))


password_entry = tk.Entry(
    card,
    width=30,
    show="*",
    bg="#1f2937",
    fg="white",
    insertbackground="white",
    relief="flat",
    font=("Arial", 11)
)
password_entry.pack(ipady=6)


# ---------------- BUTTON HOVER ----------------
def on_enter(e):
    login_btn["bg"] = "#2563eb"


def on_leave(e):
    login_btn["bg"] = "#1d4ed8"


# Login Button
login_btn = tk.Button(
    card,
    text="Login",
    width=25,
    height=1,
    font=("Arial", 12, "bold"),
    bg="#1d4ed8",
    fg="white",
    activebackground="#2563eb",
    activeforeground="white",
    bd=0,
    cursor="hand2",
    command=login
)
login_btn.pack(pady=30)

login_btn.bind("<Enter>", on_enter)
login_btn.bind("<Leave>", on_leave)


# Footer
footer = tk.Label(
    root,
    text="Press ESC to exit fullscreen",
    font=("Arial", 10),
    bg="#0f172a",
    fg="#64748b"
)
footer.pack(side="bottom", pady=20)


root.mainloop()