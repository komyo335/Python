import tkinter as tk

window = tk.Tk()
window.title("Color Game")

def start_game(event):
    print("Game started!")  # will trigger when you press Enter

# Create entry field
e = tk.Entry(window)
window.bind('<Return>', start_game)  # Press Enter to start
e.pack()
e.focus_set()  # Cursor automatically active in entry

window.mainloop()
