"""This python file will handl anything related to the Particle class, encapsulating all particle-related logic and attributes."""  # pylint: disable=line-too-long


class Particle:
    """
    Represents a particle in 2D space with position, previous position, and mass.

    Attributes:
        position (list): Current [x, y] coordinates of particle
        previous_position (list): Previous [x, y] coordinates for Verlet integration
        mass (float): Mass of the particle (1.0 default)
    """

    def __init__(self, x, y, mass=1.0):
        self.position = [x, y]
        self.previous_position = [x, y]
        self.mass = mass

    def draw(self, canvas, radius=5, color="white"):
        """
        Draws the particle on the given canvas as a circle.

        Attributes:
            canvas: Tkinter canvas to draw on
            radius: Radius of the particle circle (size in pixels)
            Color: Color of the particle
        """

        x, y = self.position
        canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color)
