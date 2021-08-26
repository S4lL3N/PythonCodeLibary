import tkinter as tk

# creates a window named root
root = tk.Tk()
# gives window a title
root.title("S4lL3N")
# window height and width in pixels
#root.geometry("500x500")
logo = tk.PhotoImage("Feed-Me.png")

# ------------Labels-------------------------------------------------------

label1 = tk.Label(text=" Lable 1 ", width=55).grid(row=0, column=0)
label2 = tk.Label(text=" Lable 2 ", width=55).grid(row=1, column=0, sticky="E")

# ----------------Buttons----------------------------------------------

button = tk.Button(text="click me", fg="blue")
button.grid(row=2, column=0)

button = tk.Button(text="click me", fg="red")
button.grid(row=3, column=0)

checkbutton = tk.Checkbutton(root, text="check box")
checkbutton.grid(row=4, column=1)

checkbutton1 = tk.Checkbutton(root, text="check box 2")
checkbutton1.grid(row=5, column=1)

checkbutton2 = tk.Checkbutton(root, text="check box 3")
checkbutton2.grid(row=6, columnspan=2)

# -----------Entry-------------------------------------------

entry = tk.Entry(root)
entry.grid(row=1, column=1)

entry1 = tk.Entry(root)
entry1.grid(row=4, column=0)

entry2 = tk.Entry(root)
entry2.grid(row=5, column=0)

# -------------------------------------------------------------------------
# buttons with functions
def printName():
    print("shae allen")

button3 = tk.Button(root, text="this button has a function", command=printName )
button3.grid(row=7, column=0)

def namePrint(event):
    print("python is fun")

button4 = tk.Button(root, text="this button has a function 2")
# <button-1> is the left mouse click, runs the namePrint function
button4.bind("<Button-1>", namePrint)
button4.grid(row=8, column=0)

def leftClick(event):
    print("Left click")
def rightClick(event):
    print("Right click")
def scroll(event):
    print("Scroll button click")
def leftArrow(event):
    print("left key")
def rightArrow(event):
    print("right key")
def upArrow(event):
    print("up key")
def downArrow(event):
    print("down key")
def enter(event):
    print("enter key")

# <Button-3> is the right mouse click
root.bind("<Button-3>", rightClick)
# <Button-2> is the mouse scroll button
root.bind("<Button-2>", scroll)
# <Left> is the left arrow key
root.bind("<Left>", leftArrow)
# <Right> is the right arrow key
root.bind("<Right>", rightArrow)
root.bind("<Up>", upArrow)
root.bind("<Down>",downArrow)
#root.bind("<Return>", enter)

# -------------------------calculator------------------------------------
def evaluate(event):
    data = entry3.get()
    label3.configure(text="answer :" + str(eval(data)))

entry3 = tk.Entry(root)
entry3.bind("<Return>", evaluate)
entry3.grid(row=9, column=0)
label3 = tk.Label(root)
label3.grid(row=9, column=1)

# -------------------------message box------------------------------------
import tkinter.messagebox
tk.messagebox.showinfo(title= "window title", message="hello S4lL3N!")

answer = tk.messagebox.askquestion(title="question 1", message="do you know the muffin man?")

if answer == "yes":
    tk.messagebox.showinfo(title="sweet", message="the one on mulberry lane?")
if answer == "no":
    tk.messagebox.showinfo(title="too bad", message="Never mind then")

# ------------------------------drop down menu-----------------------------------
def randomFun():
    print("this can be any function")

mainMenu = tk.Menu(root)
root.configure(menu=mainMenu)
subMenu = tk.Menu(mainMenu)
mainMenu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="Random Function", command=randomFun)
subMenu.add_command(label="New file ect ect", command=randomFun)

# -------------------------canvas-------------------------------------------------
window = tk.Tk()
window.title("Canvas")
canvas = tk.Canvas(window, width=300, height=300)
canvas.pack()
canvas.create_rectangle(20, 20, 100, 270)
canvas.create_line(0, 0, 300, 300)
canvas.create_polygon(50, 50, 25, 75, 60, 60, 55, 20)


root.mainloop()
window.mainloop()
