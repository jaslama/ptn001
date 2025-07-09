import tkinter as tk
from tkinter import messagebox
import urllib.request
from datetime import datetime

# Store the original background color so it can be restored
original_bg = None

# Variable and entry for URL input with a default value
url_var = tk.StringVar(value='https://www.idnes.cz')


def download_html():
    """Download the specified URL and save it to a timestamped HTML file"""
    url = url_var.get()
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
        filename = f"OUT_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        with open(filename, 'wb') as f:
            f.write(html)
        messagebox.showinfo('Download', f'HTML page saved to {filename}')
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

# Entry for the URL so the user can specify where to download from
url_entry = tk.Entry(root, textvariable=url_var, width=40)
url_entry.pack(side=tk.TOP, padx=5, pady=5)

btn_a = tk.Button(root, text='A', command=download_html)
btn_b = tk.Button(root, text='B', command=change_to_red)
btn_c = tk.Button(root, text='C', command=restore_color)

btn_a.pack(side=tk.LEFT, padx=5, pady=5)
btn_b.pack(side=tk.LEFT, padx=5, pady=5)
btn_c.pack(side=tk.LEFT, padx=5, pady=5)

root.mainloop()
