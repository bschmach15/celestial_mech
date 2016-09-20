import math
from Planets import Planets as planet

class Orbit:

    def __init__(self, mass, planet = planet("Earth", 5.971 * (10**24),6378.0), apogee_alt = None, perigee_alt = None, eccentricity = None, semimajor_axis = None):
        self._planet = planet
        self._mass = mass
        # self._radius = None # I'm thinking this should be a method instead of a property
        self._eccentricity = eccentricity
        self._semimajor_axis = semimajor_axis
        self._apogee_alt = apogee_alt
        self._pergiee_alt = perigee_alt
        self._true_anomaly = None
        self._mean_anomaly = None
        self._eccentric_anomaly = None

    def semimajor_and_eccentricity_from_hA_hP(self):
        apogee_radius, perigee_radius = self._planet.get_radius() + self._apogee_alt, self._planet.get_radius()+ self._pergiee_alt
        self._semimajor_axis = (apogee_radius + perigee_radius)/2.0
        self._eccentricity = (apogee_radius - perigee_radius)/(apogee_radius + perigee_radius)
    