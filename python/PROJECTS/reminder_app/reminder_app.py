import tkinter as tk
from tkinter import messagebox
from win10toast import ToastNotifier
import time
import threading

notifier = ToastNotifier()

# 🔔 Function to show notification
def show_notification(title, message):
    notifier.show_toast(
        title,       # ✅ positional
        message,     # ✅ positional
        duration=10,
        threaded=True
    )

# ⏱️ Function to handle reminder logic
def set_reminder():
    title = title_entry.get()
    message = message_entry.get()
    delay = time_entry.get()

    if not title or not message or not delay:
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        delay_seconds = int(delay)
    except ValueError:
        messagebox.showerror("Error", "Time must be a number!")
        return

    messagebox.showinfo("Reminder Set", f"Reminder will pop in {delay} seconds!")

    # Run reminder in a separate thread so GUI doesn’t freeze
    def wait_and_notify():
        time.sleep(delay_seconds)
        show_notification(title, message)

    threading.Thread(target=wait_and_notify).start()

# 💖 GUI Setup
root = tk.Tk()
root.title("💖 Reminder App")
root.geometry("350x300")
root.resizable(False, False)
root.config(bg="#fdf6f0")

# 📝 Labels and Entries
tk.Label(root, text="Reminder Title:", bg="#fdf6f0").pack(pady=(20, 0))
title_entry = tk.Entry(root, width=30)
title_entry.pack(pady=5)

tk.Label(root, text="Message:", bg="#fdf6f0").pack()
message_entry = tk.Entry(root, width=30)
message_entry.pack(pady=5)

tk.Label(root, text="After how many seconds?", bg="#fdf6f0").pack()
time_entry = tk.Entry(root, width=10)
time_entry.pack(pady=5)

# 📌 Set Button
tk.Button(root, text="Set Reminder 💌", command=set_reminder, bg="#ff87a2", fg="white", font=("Arial", 12, "bold")).pack(pady=20)

# 🪟 Start GUI loop
root.mainloop()
