import pyautogui
import time
import tkinter as tk

def screenshot():
    name = int(round(time.time()*1000))
    name = f'screenshot/{name}.png'
    img = pyautogui.screenshot(name)
    img.show()

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

screenshot_button = tk.Button(
    frame,
    text="Take Screenshot",
    command=screenshot
)
screenshot_button.pack(side=tk.LEFT)


close_button = tk.Button(
    frame,
    text="Close Program",
    command=quit
)
close_button.pack(side=tk.LEFT)

root.mainloop()