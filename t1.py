# import library
import requests
import tkinter as tk
from tkinter import END, Text
from tkinter.ttk import Button

# create a main window
root = tk.Tk()
root.title('Quoter')
root.attributes("-fullscreen", True)
# function that will get the data
# from the API
def get_quote():
	# API request
	r = requests.get('https://api.quotable.io/random')
	data = r.json()
	quote = data['content']
	
	# deletes all the text that is currently
	# in the TextBox
	text_box.delete('1.0', END)
	
	# inserts new data into the TextBox
	text_box.insert(END, quote)


text_box = Text(root, height=10, width=50)
get_button = Button(root, text="Get Quote", command=get_quote)

text_box.pack()
get_button.pack()
root.mainloop()
