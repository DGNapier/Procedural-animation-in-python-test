"""This is the files entry point, importing any other cogs to create the window."""  # pylint: disable=line-too-long

from window import create_window
from particle import Particle

root, canvas = create_window(800, 600)

test_particle = Particle(400, 300)

test_particle.draw(canvas)

root.mainloop()
