
from tkinter import *
from electronics import *


def wire_button_press():
    name = wires["name"]
    info = wires["info"]
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", str(name))
    info_display.insert(3.0, str(info))


def switch_button_press():
    name = switches["name"]
    info = switches["info"]
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", str(name))
    info_display.insert(3.0, str(info))
    

def resistor_button_press():
    name = resistors["name"]
    info = resistors["info"]
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", str(name))
    info_display.insert(3.0, str(info))    

def capacitor_button_press():
    name = capacitors["name"]
    info = capacitors["info"]
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", str(name))
    info_display.insert(3.0, str(info))    

def light_bulb_button_press():
    name = light_bulbs["name"]
    info = light_bulbs["info"]
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", str(name))
    info_display.insert(3.0, str(info))    

def diode_button_press():
    name = diodes["name"]
    info = diodes["info"]
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", str(name))
    info_display.insert(3.0, str(info))    

def transistor_button_press():
    name = transistors["name"]
    info = transistors["info"]
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", str(name))
    info_display.insert(3.0, str(info))


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
    
    info_display = Text(top_frame, wrap=WORD, width = 250, height = 15)
    info_display.pack()
    info_display.delete(1.0, END)
    info_display.insert("end -1 chars", welcome_message)
    
    wire = Button(top_row, text = "Wire", command = wire_button_press)
    wire.pack(side = LEFT, padx=3, pady=1)
    
    switch = Button(top_row, text = "Switch", command = switch_button_press)
    switch.pack(side = LEFT, padx=3, pady=1)

    resistor = Button(top_row, text = "Resistor", command = resistor_button_press)
    resistor.pack(side = LEFT, padx=3, pady=1)

    capacitor = Button(top_row, text = "Capacitor", command = capacitor_button_press)
    capacitor.pack(side = LEFT, padx=3, pady=1)

    light_bulb = Button(bottom_row, text = "Light Bulb", command = light_bulb_button_press)
    light_bulb.pack(side = LEFT, padx=3, pady=1)

    # inductor = Button(bottom_row, text = "Inductor", command = diode_button_press)
    # inductor.pack(side = LEFT, padx=3, pady=1)

    diode = Button(bottom_row, text = "Diode", command = diode_button_press)
    diode.pack(side = LEFT, padx=3, pady=1)

    transistor = Button(bottom_row, text = "Transistor", command = transistor_button_press)
    transistor.pack(side = LEFT, padx=3, pady=1)
    
    
    root.mainloop()
    
