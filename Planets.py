

class Planets:
    """Name Should be passed as a string
    mass should be in kg
    radius should be in km"""

    def __init__(self, name, mass, radius):
        self._name = str(name)
        self._mass = mass
        self._radius = radius

    def get_radius(self):
        return self._radius
