from tkinter import *

# Global Constants
FONT = ("Arial", 20, "normal")

def calculate_km():
    """Calculates the conversion of mile to kilometer."""
    mi = float(entry.get())
    km = round(mi * 1.60934, 1)
    result_value.config(text=km)


def calculate_mi():
    """Calculates the conversion of kilometer to mile."""
    km = float(entry.get())
    mi = round(km / 1.60934, 1)
    result_value.config(text=mi)


def mi_to_km_used():
    """Switch unit labels for mile to kilometer conversion."""
    root.title("Mile to Kilometer Converter")
    entry_unit.config(text="Mi")
    result_unit.config(text="Km")
    calculate_button.config(command=calculate_km)

  

def km_to_mi_used():
    """Switch unit labels for kilometer to mile conversion."""
    root.title("Kilometer to Mile Converter")
    entry_unit.config(text="Km")
    result_unit.config(text="Mi")
    calculate_button.config(command=calculate_mi)


# Instantiate root window object using Tk class
root = Tk()
root.title("Mile to Kilometer Converter")
root.config(padx=30, pady=30)
win_width = 450
win_height = 240
screen_width = root.winfo_screenwidth() # Returns monitor width (unit of pixels)
screen_height = root.winfo_screenheight() # Returns monitor height (units of pixels)
start_x = int(screen_width/2 - win_width/2)
start_y = int(screen_height/2 - win_height/2)
root.geometry(f"{win_width}x{win_height}+{start_x}+{start_y}") # Centers root window on any display resolution.


# Instantiate 'Mi to Km' and 'Km to Mi' Radiobutton objects
radio_state = IntVar()
radio_state.set(1)

mi_to_km = Radiobutton(text="Mi to Km", value=1, variable=radio_state, command=mi_to_km_used, font=("Arial", 15, "normal"))
mi_to_km.grid(column=0, row=2)

km_to_mi = Radiobutton(text="Km to Mi", value=2, variable=radio_state, command=km_to_mi_used, font=("Arial", 15, "normal"))
km_to_mi.grid(column=0, row=4)


# Instantiate 'is equal to' Label object
is_equal_to = Label(text="is equal to", font=FONT, padx=20)
is_equal_to.grid(column=0, row=1)


# Instantiate Entry object
entry = Entry(font=FONT, width=8)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
entry.focus()


# Instantiate unit (Mi/Km) Label object for Entry
entry_unit = Label(text="Mi", font=FONT)
entry_unit.grid(column=2, row=0)


# Instantiate unit (Km/Mi) Label object for result
result_unit = Label(text="Km", font=FONT)
result_unit.grid(column=2, row=1)


# Instantiate km_result Label object
result_value = Label(text="0.0", font=FONT, pady=10)
result_value.grid(column=1, row=1)


# Instantiate 'Calculate' Button object
calculate_button = Button(text="Calculate", font=FONT, command=calculate_km)
calculate_button.grid(column=1, row=2)




# Keeps the root window open and listens for events from window system.
root.mainloop()
