import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

from predict import predict_fraud


def predict_transaction():

    try:
        amount = float(amount_entry.get())
        transaction_type = type_var.get()

        prediction, fraud_probability = predict_fraud(amount)

        transaction_time = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO transactions
        (
            amount,
            transaction_time,
            transaction_type,
            prediction,
            fraud_probability
        )
        VALUES(?,?,?,?,?)
        """,
        (
            amount,
            transaction_time,
            transaction_type,
            prediction,
            fraud_probability
        ))

        conn.commit()
        conn.close()

        if prediction == "Fraud":
            result_label.config(
                text=f"⚠ FRAUD DETECTED\nProbability: {fraud_probability}",
                fg="#EF4444"
            )

            messagebox.showwarning(
                "Fraud Alert",
                f"Suspicious Transaction Detected!\nRisk Score = {fraud_probability}"
            )

        else:
            result_label.config(
                text=f"✅ LEGITIMATE\nProbability: {fraud_probability}",
                fg="#22C55E"
            )

            messagebox.showinfo(
                "Transaction Safe",
                f"Legitimate Transaction\nRisk Score = {fraud_probability}"
            )

        amount_entry.delete(0, tk.END)

    except Exception as e:
        messagebox.showerror(
            "Error",
            f"Error: {e}"
        )


def on_enter(e):
    predict_btn["bg"] = "#0D9488"


def on_leave(e):
    predict_btn["bg"] = "#14B8A6"


root = tk.Tk()

root.title("Add Transaction")

root.attributes("-fullscreen", True)

root.bind(
    "<Escape>",
    lambda e: root.attributes("-fullscreen", False)
)

root.configure(bg="#020617")

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
    width=650,
    height=700
)

heading = tk.Label(
    card,
    text="💳 New Transaction",
    font=("Helvetica", 28, "bold"),
    bg="#0F172A",
    fg="#00E5FF"
)

heading.pack(pady=20)

subtitle = tk.Label(
    card,
    text="Real-Time Credit Card Fraud Detection",
    font=("Arial", 12),
    bg="#0F172A",
    fg="#94A3B8"
)

subtitle.pack()

tk.Label(
    card,
    text="Transaction Amount",
    font=("Arial", 12, "bold"),
    bg="#0F172A",
    fg="white"
).pack(pady=(35, 8))

amount_entry = tk.Entry(
    card,
    width=30,
    font=("Arial", 14),
    bg="#1E293B",
    fg="white",
    insertbackground="white",
    relief="flat"
)

amount_entry.pack(ipady=8)

tk.Label(
    card,
    text="Transaction Type",
    font=("Arial", 12, "bold"),
    bg="#0F172A",
    fg="white"
).pack(pady=(30, 8))

type_var = tk.StringVar()
type_var.set("Online")

type_menu = tk.OptionMenu(
    card,
    type_var,
    "Online",
    "POS",
    "ATM",
    "Transfer"
)

type_menu.config(
    bg="#2563EB",
    fg="white",
    font=("Arial", 12),
    width=15
)

type_menu.pack(pady=10)

predict_btn = tk.Button(
    card,
    text="🔍 Predict Fraud",
    width=22,
    height=2,
    font=("Arial", 13, "bold"),
    bg="#14B8A6",
    fg="white",
    bd=0,
    cursor="hand2",
    activebackground="#0D9488",
    command=predict_transaction
)

predict_btn.pack(pady=35)

predict_btn.bind("<Enter>", on_enter)
predict_btn.bind("<Leave>", on_leave)

result_label = tk.Label(
    card,
    text="Prediction Result Will Appear Here",
    font=("Arial", 13, "bold"),
    bg="#1E293B",
    fg="#CBD5E1",
    width=35,
    height=4
)

result_label.pack(pady=25)

footer = tk.Label(
    root,
    text="Press ESC to exit fullscreen",
    font=("Arial", 10),
    bg="#020617",
    fg="#64748B"
)

footer.pack(side="bottom", pady=20)

root.mainloop()