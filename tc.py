from tkinter import *

# functions
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return round(fahrenheit, 3)

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return round(celsius, 3)

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return round(celsius, 3)

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return round(kelvin, 3)

def convert():
    try:
        celsius = celsius_input.get(1.0, END)
        fahrenheit = fahrenheit_input.get(1.0, END)
        kelvin = kelvin_input.get(1.0, END)

        if len(celsius) > 1:
            celsius = float(celsius)
            fahrenheit = celsius_to_fahrenheit(celsius)
            kelvin = celsius_to_kelvin(celsius)
        elif len(kelvin) > 1:
            kelvin = float(kelvin)
            celsius = kelvin_to_celsius(kelvin)
            fahrenheit = celsius_to_fahrenheit(celsius)
        elif len(fahrenheit) > 1:
            fahrenheit = float(fahrenheit)
            celsius = fahrenheit_to_celsius(fahrenheit)
            kelvin = celsius_to_kelvin(celsius)

        celsius_input.delete(1.0, END)
        celsius_input.insert(END, celsius)
        fahrenheit_input.delete(1.0, END)
        fahrenheit_input.insert(END, fahrenheit)
        kelvin_input.delete(1.0, END)
        kelvin_input.insert(END, kelvin)

    except:
        print("error")

def clear():
    celsius_input.delete(1.0, END)
    fahrenheit_input.delete(1.0, END)
    kelvin_input.delete(1.0, END)

# window
root = Tk()
root.geometry('600x500')
root.resizable(0, 0)
root.config(bg='dark slate gray')  # Dark background color
root.title("Convert Temperature")

Label(root, text="Celsius", font='arial 20 bold', fg='white', bg='dark slate gray').place(x=50, y=50)
Label(root, text="Fahrenheit", font='arial 20 bold', fg='white', bg='dark slate gray').place(x=50, y=125)
Label(root, text="Kelvin", font='arial 20 bold', fg='white', bg='dark slate gray').place(x=50, y=200)

celsius_input = Text(root, font='arial 20', height=1, wrap=WORD, padx=5, pady=5, bg='gray')
celsius_input.place(x=225, y=50)
fahrenheit_input = Text(root, font='arial 20', height=1, wrap=WORD, padx=5, pady=5, bg='gray')
fahrenheit_input.place(x=225, y=125)
kelvin_input = Text(root, font='arial 20', height=1, wrap=WORD, padx=5, pady=5, bg='gray')
kelvin_input.place(x=225, y=200)

clearBtn = Button(root, text='Clear', font='arial 22 bold', padx=5, pady=5, command=clear, bg='red', fg='white')
clearBtn.place(x=300, y=300)
convertBtn = Button(root, text='Convert', font='arial 22 bold', padx=5, pady=5, command=convert, bg='green', fg='white')
convertBtn.place(x=150, y=300)

root.mainloop()
