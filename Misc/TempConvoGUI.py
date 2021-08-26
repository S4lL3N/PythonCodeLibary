import tkinter as tk

def celsiusToFahrenheit(event):
    data = tempEntry.get()
    fahrenheit = float(data)
    celsius = (fahrenheit - 32) * 5 / 9
    answer = str(round(celsius, 2))
    label2.configure(text="The converted temperature is:  " + answer + " Degrees Celsius")
    #print("Celsius:", round(celsius, 2))


def fehrenheitToCelsius(event):
    data1 = tempEntry.get()
    celsius1 = float(data1)
    fahrenheit1 = 9 / 5 * celsius1 + 32
    answer1 = str(round(fahrenheit1, 2))
    label2.configure(text="The converted temperature is:  " + answer1 + " Degrees Fahrenheit")
    #print("Fahrenheit:", round(fahrenheit1, 2))


root = tk.Tk()
root.title("Temperature Conversion")

label = tk.Label(text=" Temperature Conversion ").grid(row=0, column=0, columnspan=2)
label1 = tk.Label(text=" Enter a temperature to convert: ", ).grid(row=1, column=0, sticky="E")

icon = tk.PhotoImage(file='Feed-Me.png')
root.tk.call('wm', 'iconphoto', root._w, icon)

tempEntry = tk.Entry(root)
tempEntry.grid(row=1, column=1)

button = tk.Button(text="Fahrenheit To Celsius", fg="blue")
button.bind("<Button-1>", celsiusToFahrenheit)
button.grid(row=2, column=0)

button1 = tk.Button(text="Celsius To Fahrenheit", fg="red")
button1.bind("<Button-1>", fehrenheitToCelsius)
button1.grid(row=2, column=1)

label2 = tk.Label(root, text="The converted temperature is:")
label2.grid(row=3, column=0, columnspan=2)

root.mainloop()