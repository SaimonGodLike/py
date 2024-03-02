import tkinter as tk
from PIL import ImageTk, Image

def peace(event):
    button.config(image=s2)

def look(event):
    button.config(image=s1)

def click():
    button.config(image=s3)
    new_window()

def restore_state(event=None):
    button.config(image=s1)
    root.destroy()

def new_window():
    new_window = tk.Toplevel(root)
    new_window.geometry("1000x500")
    new_window.configure(bg="gray")
    
    img1_idle = ImageTk.PhotoImage(Image.open("start.png"))
    img1_hover = ImageTk.PhotoImage(Image.open("start1.png"))
    img1_click = ImageTk.PhotoImage(Image.open("start.png"))
    img2_idle = ImageTk.PhotoImage(Image.open("start.png"))
    img2_hover = ImageTk.PhotoImage(Image.open("start1.png"))
    img2_click = ImageTk.PhotoImage(Image.open("start.png"))
    img3_idle = ImageTk.PhotoImage(Image.open("start.png"))
    img3_hover = ImageTk.PhotoImage(Image.open("start1.png"))
    img3_click = ImageTk.PhotoImage(Image.open("start.png"))

    button1 = tk.Button(new_window, image=img1_idle, relief=tk.FLAT)
    button1.pack(side="top", pady=5)
    button2 = tk.Button(new_window, image=img2_idle, relief=tk.FLAT)
    button2.pack(side="top", pady=5)
    button3 = tk.Button(new_window, image=img3_idle, relief=tk.FLAT)
    button3.pack(side="top", pady=5)

    def on_enter1(event):
        button1.config(image=img1_hover)

    def on_leave1(event):
        button1.config(image=img1_idle)

    def on_click1():
        button1.config(image=img1_click)

    def restore_state1(event=None):
        button1.config(image=img1_idle)

    def on_enter2(event):
        button2.config(image=img2_hover)

    def on_leave2(event):
        button2.config(image=img2_idle)

    def on_click2():
        button2.config(image=img2_click)

    def restore_state2(event=None):
        button2.config(image=img2_idle)

    def on_enter3(event):
        button3.config(image=img3_hover)

    def on_leave3(event):
        button3.config(image=img3_idle)

    def on_click3():
        button3.config(image=img3_click)

    def restore_state3(event=None):
        button3.config(image=img3_idle)

    button1.bind("<Enter>", on_enter1)
    button1.bind("<Leave>", on_leave1)
    button1.bind("<Button-1>", on_click1)
    button1.bind("<ButtonRelease-1>", restore_state1)

    button2.bind("<Enter>", on_enter2)
    button2.bind("<Leave>", on_leave2)
    button2.bind("<Button-1>", on_click2)
    button2.bind("<ButtonRelease-1>", restore_state2)

    button3.bind("<Enter>", on_enter3)
    button3.bind("<Leave>", on_leave3)
    button3.bind("<Button-1>", on_click3)
    button3.bind("<ButtonRelease-1>", restore_state3)



root = tk.Tk()
root.geometry("1000x500")
root.configure(bg="gray")


s1 = ImageTk.PhotoImage(Image.open("start.png"))
s2 = ImageTk.PhotoImage(Image.open("start1.png"))
s3 = ImageTk.PhotoImage(Image.open("start.png"))

button = tk.Button(root, image=s1, relief=tk.FLAT, command=click)
button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button.bind("<Enter>", peace)
button.bind("<Leave>", look)
button.bind("<Button-1>", restore_state)

root.mainloop()
