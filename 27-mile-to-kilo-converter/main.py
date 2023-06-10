from tkinter import *

# Global Constants
FONT = ("Arial", 20, "normal")

def calculate():
    """Calculates the conversion of miles to kilometers."""
    mi = float(entry.get())
    km = round(mi * 1.60934, 1)
    km_result.config(text=str(km))
    

# Instantiate root window object using Tk class
root = Tk()
root.title("Mile to Kilometer Converter")
root.config(padx=30, pady=30)
# root.geometry("500x300+710+390")
win_width = 400
win_height = 210
screen_width = root.winfo_screenwidth() # Returns monitor width (unit of pixels)
screen_height = root.winfo_screenheight() # Returns monitor height (units of pixels)
start_x = int(screen_width/2 - win_width/2)
start_y = int(screen_height/2 - win_height/2)
root.geometry(f"{win_width}x{win_height}+{start_x}+{start_y}") # Centers root window on any display resolution.

# Instantiate 'is equal to' Label object
is_equal_to = Label(text="is equal to", font=FONT)
is_equal_to.grid(column=0, row=1)

# Instantiate Entry object
entry = Entry(font=FONT, width=8)
entry.insert(END, string="0")
entry.grid(column=1, row=0)
entry.focus()

# Instantiate 'Miles' Label object
miles = Label(text="Miles", font=FONT)
miles.grid(column=2, row=0)

# Instantiate km_result Label object
km_result = Label(text="0", font=FONT, pady=10)
km_result.grid(column=1, row=1)

# Instantiate 'Km' Label object
km_unit = Label(text="Km", font=FONT)
km_unit.grid(column=2, row=1)

# Instantiate 'Calculate' Button object
calculate_button = Button(text="Calculate", font=FONT, command=calculate)
calculate_button.grid(column=1, row=2)


# Keeps the root window open and listens for events from window system.
root.mainloop()
