import tkinter as tk
import sqlite3
import matplotlib.pyplot as plt


def load_statistics():

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM transactions")
    total = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM transactions
    WHERE prediction='Fraud'
    """)
    fraud = cursor.fetchone()[0]

    cursor.execute("""
    SELECT COUNT(*)
    FROM transactions
    WHERE prediction='Legitimate'
    """)
    legit = cursor.fetchone()[0]

    conn.close()

    if total == 0:
        fraud_rate = 0
    else:
        fraud_rate = round((fraud / total) * 100, 2)

    total_label.config(
        text=f"💳 Total Transactions : {total}"
    )

    fraud_label.config(
        text=f"🚨 Fraud Transactions : {fraud}"
    )

    legit_label.config(
        text=f"✅ Legitimate Transactions : {legit}"
    )

    rate_label.config(
        text=f"📈 Fraud Rate : {fraud_rate}%"
    )

    return fraud, legit


def show_pie_chart():

    fraud, legit = load_statistics()

    plt.figure(figsize=(6, 6))

    plt.pie(
        [fraud, legit],
        labels=["Fraud", "Legitimate"],
        autopct="%1.1f%%"
    )

    plt.title("Fraud Detection Analysis")

    plt.show()


def show_bar_chart():

    fraud, legit = load_statistics()

    plt.figure(figsize=(6, 5))

    plt.bar(
        ["Fraud", "Legitimate"],
        [fraud, legit]
    )

    plt.title("Transaction Classification")

    plt.ylabel("Count")

    plt.show()


def create_button(text, command, color="#2563EB"):

    btn = tk.Button(
        root,
        text=text,
        width=25,
        height=2,
        font=("Arial", 13, "bold"),
        bg=color,
        fg="white",
        bd=0,
        cursor="hand2",
        command=command
    )

    btn.pack(pady=10)

    def enter(e):
        btn["bg"] = "#1D4ED8"

    def leave(e):
        btn["bg"] = color

    btn.bind("<Enter>", enter)
    btn.bind("<Leave>", leave)

    return btn


root = tk.Tk()

root.title("Fraud Analytics Dashboard")

root.attributes("-fullscreen", True)

root.bind(
    "<Escape>",
    lambda e: root.attributes("-fullscreen", False)
)

root.configure(bg="#020617")

heading = tk.Label(
    root,
    text="📊 Fraud Analytics Dashboard",
    font=("Helvetica", 30, "bold"),
    bg="#020617",
    fg="#00E5FF"
)

heading.pack(pady=30)

subtitle = tk.Label(
    root,
    text="Real-Time Fraud Statistics & Visualization",
    font=("Arial", 13),
    bg="#020617",
    fg="#94A3B8"
)

subtitle.pack(pady=5)

stats_frame = tk.Frame(
    root,
    bg="#0F172A",
    bd=2,
    relief="ridge"
)

stats_frame.pack(
    pady=30,
    ipadx=40,
    ipady=20
)

total_label = tk.Label(
    stats_frame,
    text="",
    font=("Arial", 15, "bold"),
    fg="#38BDF8",
    bg="#0F172A"
)

total_label.pack(pady=10)

fraud_label = tk.Label(
    stats_frame,
    text="",
    font=("Arial", 15, "bold"),
    fg="#EF4444",
    bg="#0F172A"
)

fraud_label.pack(pady=10)

legit_label = tk.Label(
    stats_frame,
    text="",
    font=("Arial", 15, "bold"),
    fg="#22C55E",
    bg="#0F172A"
)

legit_label.pack(pady=10)

rate_label = tk.Label(
    stats_frame,
    text="",
    font=("Arial", 18, "bold"),
    fg="#FBBF24",
    bg="#0F172A"
)

rate_label.pack(pady=15)

load_statistics()

create_button(
    "🥧 Show Pie Chart",
    show_pie_chart
)

create_button(
    "📊 Show Bar Chart",
    show_bar_chart
)

create_button(
    "🔄 Refresh Statistics",
    load_statistics,
    "#14B8A6"
)

footer = tk.Label(
    root,
    text="Powered by Machine Learning • SQLite • Python",
    font=("Arial", 11),
    fg="#64748B",
    bg="#020617"
)

footer.pack(
    side="bottom",
    pady=20
)

root.mainloop()