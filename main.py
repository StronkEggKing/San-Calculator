import tkinter as tk
import CalFuncs
import time
import threading

def trigger_horror_bsod(root_window):
    bsod = tk.Toplevel(root_window)
    bsod.geometry(f"{bsod.winfo_screenwidth()}x{bsod.winfo_screenheight()}")
    bsod.overrideredirect(True)
    bsod.attributes("-fullscreen", True)
    bsod.configure(bg="#0a0a7a")

    text = tk.Label(
        bsod,
        text=":(\nYour device ran into a problem and needs to restart.\n"
             "We're just collecting some error info, and then we'll restart for you.\n\n0% complete",
        fg="white", bg="#0a0a7a",
        font=("Consolas", 30),
        justify="left"
    )
    text.place(relx=0.08, rely=0.25)

    corrupted = [
        ":(\nYour device ran into a problem and needs to restart.\n"
        "We're just collecting some error info,\n0% complete",

        ":(\nYour device ran into a problem\nWe're just          some error info\n—% complete",

        ":(\nYour device ran\n         collecting some\n—% complete",

        ":(\nYour device\n        error\n—% complete",

        ":\n      r\n—% complete",

        ""
    ]

    def do_corrupted_step(idx):
        if idx < len(corrupted):
            text.config(text=corrupted[idx])
            bsod.after(800, lambda: do_corrupted_step(idx+1))
        else:
            start_fade()

    def start_fade():
        fade_step(10, 10, 122)

    def fade_step(r, g, b):
        if r > 0:
            r2 = max(0, r - 1)
            g2 = max(0, g - 1)
            b2 = max(0, b - 2)
            new_color = f"#{r2:02x}{g2:02x}{b2:02x}"
            bsod.config(bg=new_color)
            text.config(bg=new_color)
            bsod.after(30, lambda: fade_step(r2, g2, b2))
        else:
            show_scary()

    def show_scary():
        scary = tk.Label(
            bsod,
            text="WHO TAUGHT YOU THAT NUMBER",
            fg="#dddddd", bg="black",
            font=("Consolas", 54)
        )
        scary.place(relx=0.15, rely=0.4)
        blink_scary(0, scary)

    def blink_scary(count, lbl):
        if count < 30:
            color = "#ffffff" if (count % 2 == 0) else "#000000"
            bsod.configure(bg= "#000000" if (count % 2 == 0) else "#ffffff")
            lbl.config(fg=color)
            bsod.after(100, lambda: blink_scary(count+1, lbl))
        else:
            bsod.after(1000, lambda: cleanup(lbl))

    def cleanup(lbl):
        lbl.config(text="")
        bsod.config(bg="black")
        bsod.after(1000, bsod.destroy)

    bsod.after(2000, lambda: do_corrupted_step(0))


def Submit():
    user_input = entry.get().strip()
    try:
        value = float(user_input)
        if value == 131681894400:
            trigger_horror_bsod(window)
            return
    except ValueError:
        pass

    try:
        value = float(user_input)
        answer = CalFuncs.calculate(value)
        var.set("San of " + str(value) + " is: " + str(answer))
    except Exception as e:
        var.set("Error: " + str(e))


def SubmitInv():
    user_input = entryinv.get().strip()
    try:
        value = float(user_input)
        if value == 131681894400:
            trigger_horror_bsod(window)
            return
    except ValueError:
        pass

    try:
        value = float(user_input)
        answer = CalFuncs.CalculateInv(value)
        varinv.set("San inverse of " + str(value) + " is: " + str(answer))
    except Exception as e:
        varinv.set("Error: " + str(e))


window = tk.Tk()
window.title("San Calculator")
window.config(background="#121212")
window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)

main = tk.Frame(window, bg="#121212", padx=10, pady=10)
main.grid(row=0, column=0, sticky="nsew")

# Ensure the main frame expands
main.grid_columnconfigure(0, weight=1)
main.grid_columnconfigure(1, weight=1)
main.grid_rowconfigure(0, weight=0)  # header labels
main.grid_rowconfigure(1, weight=0)  # inputs/buttons
main.grid_rowconfigure(2, weight=1)  # output expands if needed

# ============ INPUT (normal) ============
lbl_in = tk.Label(main, text="Input", fg="#eeeeee", bg="#121212",
                  font=("JetBrainsMono Nerd Font Propo", 24))
lbl_in.grid(row=0, column=0, sticky="w", pady=(0,5))

entry = tk.Entry(main, font=("JetBrainsMono Nerd Font Propo", 24),
                 bg="#eeeeee", fg="#121212")
entry.grid(row=1, column=0, sticky="ew", padx=(0,5), pady=5)

btn = tk.Button(main, text="Calculate", command=Submit,
                font=("JetBrainsMono Nerd Font Propo", 24))
btn.grid(row=1, column=1, sticky="ew", padx=(5,0), pady=5)

# ============ OUTPUT (normal) ============
lbl_out = tk.Label(main, text="Output", fg="#eeeeee", bg="#121212",
                   font=("JetBrainsMono Nerd Font Propo", 20))
lbl_out.grid(row=2, column=0, sticky="w", pady=(10,5))

var = tk.StringVar()
out_entry = tk.Entry(main, textvariable=var, font=("JetBrainsMono Nerd Font Propo", 20),
                     bg="#121212", fg="#000000", state="readonly")
out_entry.grid(row=3, column=0, columnspan=2, sticky="ew", pady=(0,10))

# ============ INPUT (inverse) ============
lbl_in_inv = tk.Label(main, text="Input (Inverse)", fg="#eeeeee", bg="#121212",
                      font=("JetBrainsMono Nerd Font Propo", 24))
lbl_in_inv.grid(row=4, column=0, sticky="w", pady=(10,5))

entryinv = tk.Entry(main, font=("JetBrainsMono Nerd Font Propo", 24),
                    bg="#eeeeee", fg="#121212")
entryinv.grid(row=5, column=0, sticky="ew", padx=(0,5), pady=5)

btn_inv = tk.Button(main, text="Calculate Inverse", command=SubmitInv,
                    font=("JetBrainsMono Nerd Font Propo", 24))
btn_inv.grid(row=5, column=1, sticky="ew", padx=(5,0), pady=5)

# ============ OUTPUT (inverse) ============
lbl_out_inv = tk.Label(main, text="Output", fg="#eeeeee", bg="#121212",
                       font=("JetBrainsMono Nerd Font Propo", 20))
lbl_out_inv.grid(row=6, column=0, sticky="w", pady=(10,5))

varinv = tk.StringVar()
out_entry_inv = tk.Entry(main, textvariable=varinv, font=("JetBrainsMono Nerd Font Propo", 20),
                         bg="#121212", fg="#000000", state="readonly")
out_entry_inv.grid(row=7, column=0, columnspan=2, sticky="ew", pady=(0,10))

window.mainloop()