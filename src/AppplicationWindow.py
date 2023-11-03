import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("My first GUI")
tk.Label(mainWindow, text="This is a text").pack()
tk.Button(mainWindow, text="Test").pack()
mainWindow.mainloop()
