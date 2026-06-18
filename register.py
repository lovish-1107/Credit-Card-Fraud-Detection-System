import tkinter as tk
from tkinter import messagebox
import sqlite3


def register_user():

    username = username_entry.get()
    password = password_entry.get()

    if username == "" or password == "":
        messagebox.showerror(
            "Error",
            "All fields are required"
        )
        return

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    try:
        cursor.execute("""
        INSERT INTO users(username,password)
        VALUES(?,?)
        """, (username, password))

        conn.commit()

        messagebox.showinfo(
            "Success",
            "Registration Successful"
        )

        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    except sqlite3.IntegrityError:
        messagebox.showerror(
            "Error",
            "Username already exists"
        )

    conn.close()


# Exit fullscreen
def exit_fullscreen(event):
    root.attributes("-fullscreen", False)


# Button hover effects
def on_enter(e):
    register_btn["bg"] = "#0D9488"


def on_leave(e):
    register_btn["bg"] = "#14B8A6"


# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("User Registration")

# Fullscreen
root.attributes("-fullscreen", True)
root.bind("<Escape>", exit_fullscreen)

# Background Color
root.configure(bg="#020617")

# ================= CARD =================
card = tk.Frame(
    root,
    bg="#0F172A",
    bd=2,
    relief="ridge"
)

card.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=500,
    height=500
)

# ================= TITLE =================
title = tk.Label(
    card,
    text="Create Account 📝",
    font=("Helvetica", 24, "bold"),
    fg="#00E5FF",
    bg="#0F172A"
)
title.pack(pady=(30, 10))

subtitle = tk.Label(
    card,
    text="Register to use Fraud Detection System",
    font=("Arial", 11),
    fg="#94A3B8",
    bg="#0F172A"
)
subtitle.pack()

# ================= USERNAME =================
tk.Label(
    card,
    text="Username",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#0F172A"
).pack(pady=(30, 5))

username_entry = tk.Entry(
    card,
    width=30,
    font=("Arial", 12),
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    relief="flat"
)
username_entry.pack(ipady=8)

# ================= PASSWORD =================
tk.Label(
    card,
    text="Password",
    font=("Arial", 12, "bold"),
    fg="white",
    bg="#0F172A"
).pack(pady=(20, 5))

password_entry = tk.Entry(
    card,
    show="*",
    width=30,
    font=("Arial", 12),
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    relief="flat"
)
password_entry.pack(ipady=8)

# ================= REGISTER BUTTON =================
register_btn = tk.Button(
    card,
    text="✅ Register",
    width=20,
    height=2,
    font=("Arial", 12, "bold"),
    bg="#14B8A6",
    fg="white",
    bd=0,
    cursor="hand2",
    activebackground="#0D9488",
    command=register_user
)
register_btn.pack(pady=35)

register_btn.bind("<Enter>", on_enter)
register_btn.bind("<Leave>", on_leave)

# ================= FOOTER =================
footer = tk.Label(
    root,
    text="Press ESC to exit fullscreen",
    font=("Arial", 10),
    fg="#64748B",
    bg="#020617"
)
footer.pack(side="bottom", pady=20)

root.mainloop()