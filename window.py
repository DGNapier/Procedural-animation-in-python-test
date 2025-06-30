"""This python file will handle anything related to creating the Tkinter window."""  # pylint: disable=line-too-long

import tkinter as tk


def create_window(width, height, bg_color="black", on_mouse_move=None):
    """
    Creates a Tkinter window with a canvas of specified width, heighth, and background color.

    Attributes:
        width: Width of the window in pixels
        height: Height of the window in pixels
        bg_color: Background color of the canvas
        on_mouse_move: Function for mouse motion events (x, y)

    Returns:
        A tuple containing the root (window) and canvas objects
    """
    root = tk.Tk()
    root.geometry(f"{width}x{height}")
    canvas = tk.Canvas(root, width=width, height=height, bg=bg_color)
    canvas.pack()

    # Adding a mechanism so mouse motion events can update the main program
    if on_mouse_move:
        canvas.bind("<Motion>", lambda event: on_mouse_move(event.x, event.y))

    return root, canvas
