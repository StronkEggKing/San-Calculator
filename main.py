# Packages/Scripts/Services
import tkinter as tk
import CalFuncs
import time
import threading


# Main Function
def trigger_horror_bsod(root_window):
    bsod = tk.Toplevel(root_window)
    bsod.geometry(f"{bsod.winfo_screenwidth()}x{bsod.winfo_screenheight()}")
    # bsod.overrideredirect(True)
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
        pass # maybe alert user?

    try:
        value = float(user_input)
        answer = CalFuncs.calculate(value)
        Text = "San of " + str(value) + " is: " + str(answer)
        var.set(Text)
    except Exception as e:
        var.set("Error: " + str(e))

def SubmitInv():
    user_input = entry.get().strip()

    try:
        value = float(user_input)
        if value == 131681894400:
            trigger_horror_bsod(window)
            return
    except ValueError:
        pass # maybe alert user?

    try:
        value = float(user_input)
        answer = CalFuncs.CalculateInv(value)
        InvText = "San inverse of "+str(value)+" is: "+str(answer)
        varinv.set(InvText)
    except Exception as e:
        var.set("Error: " + str(e))

# Variables
WindowBGColor = "#121212"

EntryBGColor = "#eeeeee"

TextColor = "#000000"

InputFont = "JetBrainsMono Nerd Font Propo"
OutputFont = "JetBrainsMono Nerd Font Propo"
SubmitFont = "JetBrainsMono Nerd Font Propo"

InputFontSize = 40
OutputFontSize = 30
SubmitFontSize = 30

InputBorderSize = "2px"
OutputBorderSize = "0px"
SubmitBorderSize = "2px"

InputWidth= 20
OutputWidth = 40
SubmitWidth = 20

InputAlignment = "center"
OutputAlignment = "center"
SubmitAlignment = "center"

# UI
# Window

window = tk.Tk()

window.title("San Calculator")
#icon = PhotoImage(file="")
#window.iconphoto(True,icon)
window.config(background=WindowBGColor)

MainFrame = tk.LabelFrame(window)

# Normal
# Input Label
inputl = tk.Label(window, text="Input")

inputl.config(font=(InputFont, InputFontSize))
inputl.config(background=WindowBGColor)
inputl.config(fg=EntryBGColor)

inputl.pack()

# Input Box
entry = tk.Entry()

entry.config(font=(InputFont, InputFontSize))
entry.config(bg=EntryBGColor)
entry.config(fg=WindowBGColor)

entry.pack()

# Submit button
submit = tk.Button(window, text="Calculate", command=Submit, justify=SubmitAlignment)

submit.pack()

# Output Label
outputl = tk.Label(window, text="Output")

outputl.config(font=(OutputFont, OutputFontSize))
outputl.config(background=WindowBGColor)
outputl.config(fg=EntryBGColor)

outputl.pack()

# Output Box
scrollbar = tk.Scrollbar(window, orient="horizontal")

var = tk.StringVar()

l = tk.Entry(window, textvariable=var, justify=OutputAlignment)

l.config(font=(OutputFont, OutputFontSize))
l.config(background=WindowBGColor)
l.config(fg=TextColor)
l.config(bd=OutputBorderSize)
l.config(width=OutputWidth)
l.config(xscrollcommand=scrollbar.set)
l.config(state="readonly")

l.pack()

var.set("")

scrollbar.config(command=l.xview)
scrollbar.pack(fill="x")

# Inverse
# Input Label
inputlinv = tk.Label(window, text="Input")

inputlinv.config(font=(InputFont, InputFontSize))
inputlinv.config(background=WindowBGColor)
inputlinv.config(fg=EntryBGColor)

inputlinv.pack()

# Input Box
entryinv = tk.Entry()

entryinv.config(font=(InputFont, InputFontSize))
entryinv.config(bg=EntryBGColor)
entryinv.config(fg=WindowBGColor)

entryinv.pack()

# Submit button
submitinv = tk.Button(window, text="Calculate Inverse", command=SubmitInv)

submitinv.pack()

# Output Label
outputlinv = tk.Label(window, text="Output")

outputlinv.config(font=(OutputFont, OutputFontSize))
outputlinv.config(background=WindowBGColor)
outputlinv.config(fg=EntryBGColor)

outputlinv.pack()

# Output Box
scrollbarINV = tk.Scrollbar(window, orient="horizontal")

varinv = tk.StringVar()

linv = tk.Entry(window, textvariable=varinv, justify=OutputAlignment)

linv.config(font=(OutputFont, OutputFontSize))
linv.config(background=WindowBGColor)
linv.config(fg=TextColor)
linv.config(bd=OutputBorderSize)
linv.config(width=OutputWidth)
linv.config(xscrollcommand=scrollbarINV.set)
linv.config(state="readonly")
linv.pack()

varinv.set("")

scrollbarINV.config(command=linv.xview)
scrollbarINV.pack()

MainFrame.pack(fill="x", padx=5, pady=5)

window.mainloop()