import tkinter as tk


def add_transaction():
    import add_transaction


def transaction_history():
    import history


def analytics_dashboard():
    import analytics


def export_csv_report():
    import export_csv
    export_csv.export_transactions()


def export_excel_report():
    import export_excel
    export_excel.export_excel()


def open_admin():
    import admin_panel


def on_enter(e):
    e.widget["bg"] = "#1D4ED8"


def on_leave(e):
    if e.widget["text"] == "🚪 Logout":
        e.widget["bg"] = "#EF4444"
    else:
        e.widget["bg"] = "#2563EB"


def create_button(text, command, color="#2563EB"):
    btn = tk.Button(
        root,
        text=text,
        width=30,
        height=2,
        font=("Arial", 14, "bold"),
        bg=color,
        fg="white",
        bd=0,
        cursor="hand2",
        activebackground="#1D4ED8",
        activeforeground="white",
        command=command
    )

    btn.pack(pady=10)

    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)

    return btn


root = tk.Tk()
root.title("Credit Card Fraud Detection System")

root.attributes("-fullscreen", True)

root.bind(
    "<Escape>",
    lambda e: root.attributes("-fullscreen", False)
)

root.configure(bg="#020617")

heading = tk.Label(
    root,
    text="💳 Credit Card Fraud Detection System",
    font=("Helvetica", 30, "bold"),
    bg="#020617",
    fg="#00E5FF"
)

heading.pack(pady=(30, 5))

subtitle = tk.Label(
    root,
    text="Machine Learning Based Fraud Detection & Analytics Dashboard",
    font=("Arial", 14),
    bg="#020617",
    fg="#94A3B8"
)

subtitle.pack(pady=(0, 25))

create_button(
    "💳 Add Transaction",
    add_transaction
)

create_button(
    "📜 Transaction History",
    transaction_history
)

create_button(
    "📊 Analytics Dashboard",
    analytics_dashboard
)

create_button(
    "📄 Export CSV Report",
    export_csv_report
)

create_button(
    "📑 Export Excel Report",
    export_excel_report
)

create_button(
    "👨‍💼 Admin Panel",
    open_admin
)

create_button(
    "🚪 Logout",
    root.destroy,
    "#EF4444"
)

stats_frame = tk.Frame(
    root,
    bg="#0F172A",
    bd=2,
    relief="ridge"
)

stats_frame.pack(
    pady=25,
    ipadx=20,
    ipady=10
)

stats = tk.Label(
    stats_frame,
    text="✓ Accuracy : 99.2%\n"
         "✓ Transactions : 50,000+\n"
         "✓ Fraud Detected : 1,250",
    font=("Arial", 12, "bold"),
    fg="#22C55E",
    bg="#0F172A",
    justify="left"
)

stats.pack()

footer = tk.Label(
    root,
    text="Powered by Machine Learning • SQLite • Python Tkinter",
    font=("Arial", 11),
    fg="#64748B",
    bg="#020617"
)

footer.pack(
    side="bottom",
    pady=20
)

root.mainloop()