import tkinter as tk

#Setup window, size, title, and make it nonresizable
root = tk.Tk()
root.geometry("400x400")
root.title('Calculator')
root.resizable(0,0)

###################FUNCTIONS###################
#These functions will update the entry window 
#showing the user their expression to be calculated

def click(x):
    global text
    text = text + str(x)
    inputTxt.set(text)

root.mainloop()