import tkinter as tk
from tkinter import messagebox
from typing import List, Dict
from Splitwise import Splitwise
from App import SplitwiseUI

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = SplitwiseUI(root)
    root.mainloop()