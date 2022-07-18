import tkinter as tk

#Setup window, size, title, and make it nonresizable
root = tk.Tk()
root.geometry("400x400")
root.title('Calculator')
root.resizable(0,0)

#Create a frame to hold the input box
inputFrame = tk.Frame(root, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
inputFrame.pack(side=tk.TOP)

#CREATE THE INPUT AREA
inputField = tk.Entry(inputFrame, font=('times new roman', 18, 'bold'),justify=tk.RIGHT)
inputField.grid(row=0, column=0)
inputField.pack(ipadx=400,ipady=10)

#CREATE FRAME FOR BUTTONS
buttonFrame = tk.Frame(root, width=400, height=350, bg="grey")
buttonFrame.pack()

#FIRST ROW OF BUTTONS
clear = tk.Button(buttonFrame, text="Clear", fg="black", width=45, height=3, bd=0, bg="#eee", cursor="hand2").grid(row=0, column=0, columnspan=3, padx=1, pady=1)
divide = tk.Button(buttonFrame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2").grid(row = 0, column = 3, padx = 1, pady = 1)
root.mainloop()