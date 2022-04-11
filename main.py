import tkinter as tk

root = tk.Tk()
root.title('Caesar Cipher')
root.geometry('600x600')
root.columnconfigure(1,weight=1)

# 1st row of information
message_Label = tk.Label(
    root,
    text= 'Enter an message to encode:',
    font=('arial 16 bold'),
    bg='red',
    fg='#FF0'
)
message_Label.grid(row=0,column=0)
message_var = tk.StringVar(root) # holds the text from message _input
message_input = tk.Entry(
    root,
    textvariable=message_var
)
message_input.grid(row=0,column=1,sticky=(tk.N,tk.E,tk.W,tk.S),padx=10)

#row 2
encoded_Label = tk.Label(
    root,
    text= 'EYour encoded messege is here:',
    font=('arial 16 bold'),
    bg='green',
    fg='pink'
)
encoded_Label.grid(row=1,column=0)

root.mainloop()