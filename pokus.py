import tkinter as tk
from tkinter import messagebox
import urllib.request

# Store the original background color so it can be restored
original_bg = None


def download_html():
    """Download www.idnes.cz and save it as A.html"""
    try:
        with urllib.request.urlopen('https://www.idnes.cz') as response:
            html = response.read()
        with open('A.html', 'wb') as f:
            f.write(html)
        messagebox.showinfo('Download', 'HTML page saved to A.html')
    except Exception as exc:
        messagebox.showerror('Error', f'Failed to download page: {exc}')


def change_to_red():
    """Change the window color to red, preserving the original color."""
    global original_bg
    if original_bg is None:
        original_bg = root.cget('bg')
    root.configure(bg='red')


def restore_color():
    """Restore the window color to the original color."""
    if original_bg is not None:
        root.configure(bg=original_bg)


root = tk.Tk()
root.title('Pokus Form')

btn_a = tk.Button(root, text='A', command=download_html)
btn_b = tk.Button(root, text='B', command=change_to_red)
btn_c = tk.Button(root, text='C', command=restore_color)

btn_a.pack(side=tk.LEFT, padx=5, pady=5)
btn_b.pack(side=tk.LEFT, padx=5, pady=5)
btn_c.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
