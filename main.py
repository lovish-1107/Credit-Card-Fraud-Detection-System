import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import subprocess
from time import strftime


# ================= FUNCTIONS =================
def open_login():
    try:
        subprocess.Popen(["python", "login.py"])
    except Exception as e:
        messagebox.showerror("Error", str(e))


def exit_fullscreen(event):
    root.attributes("-fullscreen", False)


def update_time():
    current_time = strftime('%H:%M:%S')
    clock.config(text=current_time)
    clock.after(1000, update_time)


# ================= MAIN WINDOW =================
root = tk.Tk()
root.title("Credit Card Fraud Detection System")
root.attributes("-fullscreen", True)
root.bind("<Escape>", exit_fullscreen)

# Premium Background
root.configure(bg="#020617")

# ================= TOP BAR =================
top_frame = tk.Frame(root, bg="#020617", height=60)
top_frame.pack(fill="x")

clock = tk.Label(
    top_frame,
    font=("Arial", 16, "bold"),
    fg="#00E5FF",
    bg="#020617"
)
clock.pack(side="left", padx=20, pady=10)

update_time()

title_top = tk.Label(
    top_frame,
    text="AI Powered Banking Security",
    font=("Arial", 16, "bold"),
    fg="#38BDF8",
    bg="#020617"
)
title_top.pack(side="right", padx=20)

# ================= MAIN FRAME =================
main_frame = tk.Frame(root, bg="#020617")
main_frame.pack(fill="both", expand=True)

# ================= LEFT SIDE =================
left_frame = tk.Frame(main_frame, bg="#020617")
left_frame.pack(side="left", fill="both", expand=True)

try:
    img = Image.open("atm machine.png")

    # Resize image
    img = img.resize((650, 500), Image.LANCZOS)

    atm_img = ImageTk.PhotoImage(img)

    image_label = tk.Label(
        left_frame,
        image=atm_img,
        bg="#020617"
    )
    image_label.pack(expand=True)

except Exception as e:
    print("Image Error:", e)

# ================= RIGHT SIDE =================
right_frame = tk.Frame(main_frame, bg="#020617")
right_frame.pack(side="right", fill="both", expand=True)

heading = tk.Label(
    right_frame,
    text="Credit Card\nFraud Detection\nSystem",
    font=("Helvetica", 34, "bold"),
    fg="#00E5FF",
    bg="#020617",
    justify="center"
)
heading.pack(pady=(80, 15))

tagline = tk.Label(
    right_frame,
    text="Secure • Intelligent • Real-Time Detection",
    font=("Arial", 14, "italic"),
    fg="#FBBF24",
    bg="#020617"
)
tagline.pack()

subtitle = tk.Label(
    right_frame,
    text="Machine Learning Based Fraud Prevention",
    font=("Arial", 14),
    fg="#CBD5E1",
    bg="#020617"
)
subtitle.pack(pady=10)

# ================= STATS =================
stats_frame = tk.Frame(
    right_frame,
    bg="#0F172A",
    bd=2,
    relief="ridge"
)
stats_frame.pack(pady=20, ipadx=20, ipady=10)

stats = tk.Label(
    stats_frame,
    text="✓ Accuracy : 99.2%\n✓ Transactions : 50,000+\n✓ Fraud Detected : 1,250",
    font=("Arial", 12, "bold"),
    fg="#22C55E",
    bg="#0F172A",
    justify="left"
)
stats.pack()

# ================= START BUTTON =================
start_btn = tk.Button(
    right_frame,
    text="🚀 Launch System",
    width=22,
    height=2,
    font=("Arial", 15, "bold"),
    bg="#14B8A6",
    fg="white",
    bd=0,
    cursor="hand2",
    activebackground="#0D9488",
    command=open_login
)
start_btn.pack(pady=20)

# ================= EXIT BUTTON =================
exit_btn = tk.Button(
    right_frame,
    text="❌ Exit",
    width=22,
    height=2,
    font=("Arial", 15, "bold"),
    bg="#EF4444",
    fg="white",
    bd=0,
    cursor="hand2",
    activebackground="#DC2626",
    command=root.destroy
)
exit_btn.pack()

# ================= FOOTER =================
footer = tk.Label(
    root,
    text="Powered by Machine Learning • SQLite Database • Python Tkinter",
    font=("Arial", 11),
    fg="#94A3B8",
    bg="#020617"
)
footer.pack(side="bottom", pady=15)

root.mainloop()