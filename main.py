from re import A
from tkinter import *
from webbrowser import BackgroundBrowser





wires = {
    "name" : "Wire\n",
    "info" : "Wires are pieces of metal that transport electricity. They are usually flexible"
    "which makes them easier to use. These electrical conductors are key to all electrical"
    "devices, from the electric circuit board in a computer to the transformer in a neighborhood,"
    "or even the electrical transmission system carrying electric power hundreds of kilometers."
    "Without wires electricity would be unavailable for everyone, making them a necessary"
    "component to modern life. Depending on their purpose, wires can have varying sizes and"
    "compositions."
}




def wire_button_press():
    name = wires["name"]
    info = wires["info"]
    print(name)
    print(info)

















if __name__ == "__main__":
    root = Tk()
    root.title("Electronics Documentation")
    root.geometry("400x250")
    root.resizable(False, False)
    
    top_frame = Frame(root)
    top_frame.pack(side = "top", fill=BOTH)
    bottom_frame = Frame(root, width=100)
    bottom_frame.pack(side = "bottom", fill=BOTH, expand = True)
    
    top_row = Frame(bottom_frame)
    top_row.pack(side = TOP)
    bottom_row = Frame(bottom_frame)
    bottom_row.pack(side = BOTTOM)
    
    listbox = Listbox(top_frame, width = 250, height = 15)
    listbox.pack()
    
    wire = Button(top_row, text = "Wire", command = wire_button_press)
    wire.pack(side = LEFT, padx=3, pady=1)
    
    switch = Button(top_row, text = "Switch")
    switch.pack(side = LEFT, padx=3, pady=1)

    resistor = Button(top_row, text = "Resistor")
    resistor.pack(side = LEFT, padx=3, pady=1)

    capacitor = Button(top_row, text = "Capacitor")
    capacitor.pack(side = LEFT, padx=3, pady=1)

    light_bulb = Button(bottom_row, text = "Light Bulb")
    light_bulb.pack(side = LEFT, padx=3, pady=1)

    inductor = Button(bottom_row, text = "Inductor")
    inductor.pack(side = LEFT, padx=3, pady=1)

    diode = Button(bottom_row, text = "Diode")
    diode.pack(side = LEFT, padx=3, pady=1)

    transistor = Button(bottom_row, text = "Transistor")
    transistor.pack(side = LEFT, padx=3, pady=1)
    
    root.mainloop()