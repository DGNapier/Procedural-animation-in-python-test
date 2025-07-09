"""This python file will handle anything related to the Particle class, encapsulating all particle-related logic and attributes."""  # pylint: disable=line-too-long


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
        
        Returns:
            Canvas object ID of the drawn oval
        """

        x, y = self.position # This is creating a bounding box. x - radius, y - radius is the top left of the particle.
        return canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=color) # x + radius, y + radius is the bottom right of the particle.

    def update_position(self, x, y):
        """
        This is for updating a particle's position and previouis position to new coordinates.

        Attributes:
            x: new x coordinates
            y: new y coordinates
        """
        self.position = [x, y]
        self.previous_position = [x, y]
