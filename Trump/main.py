import tkinter as tk
from PIL import Image, ImageTk
import requests


def get_quote():
    """Pull random Trump quote from API Endpoint."""
    response = requests.get(url='https://api.whatdoestrumpthink.com/api/v1/quotes/random/')
    response.raise_for_status()
    data = response.json()
    quote = data['message']
    canvas.itemconfig(trump_quote, text=quote)
    


root = tk.Tk()
root.title('Trump said...')
root.resizable(width=False, height=False)
trump_icon = tk.PhotoImage(file='trump_icon.png')
root.iconphoto(False, trump_icon)

canvas = tk.Canvas(width=520, height=764,background='white')
quote_pil_img = Image.open('quote_bubble.png')
resized_quote_pil_img = quote_pil_img.resize((425, 425))
quote_rendered_img = ImageTk.PhotoImage(image=resized_quote_pil_img)
canvas.create_image(300, 200, image=quote_rendered_img)
trump_quote = canvas.create_text(300, 150, text='Hi. My name is Trump!',
                    width=325, font=('Arial', 18, 'bold'), anchor='center')
canvas.pack()

trump = tk.PhotoImage(file='trump.png')
button = tk.Button(image=trump, borderwidth=0, highlightthickness=0,
                    activebackground='white', command=get_quote).place(x=0, y=400)

click_me_label = tk.Label(text='← Click me!', font=('Arial', 30, 'bold'), fg='red', bg='white')
click_me_label.place(x=225, y=500)

root.mainloop()
