"""This python file will handle anything related to creating the Tkinter window."""  # pylint: disable=line-too-long

import tkinter as tk


def create_window(width, height, bg_color="black"):
    """
    Creates a Tkinter window with a canvas of specified width, heighth, and background color.

    Attributes:
        width: Width of the window in pixels
        height: Height of the window in pixels
        bg_color: Background color of the canvas

    Returns:
        A tuple containing the root (window) and canvas objects
    """
    root = tk.Tk()
    root.geometry(f"{width}x{height}")
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color)
    canvas.pack()
    return root, canvas
