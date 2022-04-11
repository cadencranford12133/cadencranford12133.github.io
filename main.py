from base64 import encode
from email import message
import tkinter as tk

root = tk.Tk()
root.title('Caesar Cipher')
root.geometry('600x600')

# 1st row of information
message_label = tk.label(
    root,
    text= 'Enter an message to encode:',
    font=('arial 16 bold'),
    bg='red',
    fg='#FF0'
)
message_label.grid(row=0,colum=zero)
root.mainloop()