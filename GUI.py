from tkinter import *
from PIL import Image, ImageTk
import speechtotext
import action

root = Tk()
root.title("Khushi's Assistant")
root.geometry("675x800")
root.config(bg="#F4C2C2")
root.resizable(False, False)

# ask function
def ask():
    user_val=speechtotext.speechtotext()
    bot_val=action.Action(user_val)
    text.insert(END, "User-->: " + user_val + "\n")
    text.insert(END, "Bot--> " + bot_val + "\n")
    if bot_val != None:
        text.insert(END, "BOT<--------\n"+str(bot_val)+"\n")
    if bot_val=="Ok, have a nice day":
        root.destroy()


# send func
def send():
    send = entry.get()
    bot=action.Action(send)
    text.insert(END, "User-->: " + send + "\n")
    text.insert(END, "Bot-->: " + bot + "\n")
    if bot != None:
        text.insert(END, "BOT<--------\n"+str(bot)+"\n")   
    if bot=="Ok, have a nice day":
        root.destroy()

# del func
def del_text():
    text.delete(1.0, END)

# ===== Frame (title + image) =====
frame = LabelFrame(root, padx=50, pady=10, borderwidth=3, relief="raised", bg="#F4C2C2")
frame.grid(row=0, column=0, padx=20, pady=20)

# Title label
text_label = Label(frame, text="Khushi's AI Assistant",
                   font=("comic Sans ms", 14, "bold"),
                   bg="#975891", fg="white")
text_label.grid(row=0, column=0, pady=5)

# Image
image = ImageTk.PhotoImage(Image.open("Assistant.webp"))
image_label = Label(frame, image=image, bg="#F4C2C2")
image_label.grid(row=1, column=0, pady=10)

# ===== Text Box (below frame) =====
text = Text(root, font=('courier', 10, 'bold'),
            bg="#F1AAF2", height=6, width=50)
text.grid(row=1, column=0, pady=10)

# ===== Entry Box (below text box) =====
entry = Entry(root, justify=CENTER, font=("Arial", 12), width=45)
entry.grid(row=2, column=0, pady=10)

# ===== Buttons (below entry) =====
button_frame = Frame(root, bg="#F4C2C2")
button_frame.grid(row=3, column=0, pady=15)

Button1 = Button(button_frame, text="ASK", bg="#F4C2C2",
                 pady=16, padx=40, borderwidth=3, relief=SOLID, command=ask)
Button1.grid(row=0, column=0, padx=10)

Button3 = Button(button_frame, text="DELETE", bg="#F4C2C2",
                 pady=16, padx=40, borderwidth=3, relief=SOLID, command=del_text)
Button3.grid(row=0, column=1, padx=10)

Button2 = Button(button_frame, text="SEND", bg="#F4C2C2",
                 pady=16, padx=40, borderwidth=3, relief=SOLID, command=send)
Button2.grid(row=0, column=2, padx=10)

root.mainloop()
