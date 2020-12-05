import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

frame = tk.Frame(root, bg = "#80c1ff")
frame.place(relx=0.1,rely=0.1,relwidth = 0.8, relheight = 0.8)

button = tk.Button(frame, text = "text button", bg ="grey" )
button.pack()

root.mainloop()
