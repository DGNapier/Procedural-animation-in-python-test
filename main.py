"""This is the files entry point, importing any other cogs to create the window."""  # pylint: disable=line-too-long

from window import create_window
from particle import Particle


class App:
    """
    Main application class for simulation and rendering.
    """

    def __init__(self):
        # Creating window and canvas
        self.root, self.canvas = create_window(
            800, 600, on_mouse_move=self.on_mouse_move
        )

        # Test particle at center
        self.particle = Particle(400, 300)
        self.particle_id = self.particle.draw(self.canvas)

        self.mouse_pos = [400, 300]

        self.running = True
        self.animate()

    def on_mouse_move(self, x, y):
        """
        Callback for mouse motion events, updates mouse position

        Arguments:
            x: mouse x-coordinates
            y: mouse y-coordinates
        """
        self.mouse_pos = [x, y]

    def animate(self):
        """
        Animation loop to update and redraw particle
        """
        if not self.running:
            return

        # Update particle position to follow mouse
        self.particle.update_position(*self.mouse_pos)

        self.canvas.delete("all")
        self.particle_id = self.particle.draw(self.canvas)

        self.root.after(16, self.animate)

    def run(self):
        """
        Start the Tkinter event loop.
        """
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
