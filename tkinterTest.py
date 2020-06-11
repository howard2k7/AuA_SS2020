import tkinter as tk

window = tk.Tk(className='Hi there...')
window.geometry("400x500")

frame_a = tk.Frame(master=window, relief="sunken", borderwidth = 5)
frame_b = tk.Frame()

greeting = tk.Label(
    master= frame_a,
    text="Maze",
    fg = "white",
    bg = "black",
    width = 10,
    height = 12)
greeting.pack()

button = tk.Button(
    master=frame_b,
    text = "Click it!",
    width=25,
    height = 10,
    bg = "yellow",
    fg = "blue"
)
button.pack()

frame_b.pack()
frame_a.pack()

textbox = tk.Entry(
    width = 50,
    fg="green",
    bg="red"
)
textbox.insert(0, "Put text here...")
textbox.pack()



window.mainloop()

