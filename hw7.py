from Anomalies import Anomalies
from Orbital_Elements import Orbital_Elements
import numpy as np
from Planets import Earth

position = np.array([5492.000,3984.001,2.955])
velocity = np.array([-3.931,5.498,-3.665])

Orb_Elem1 = Orbital_Elements(posistion = position, velocity = velocity)
Orb_Elem1.calc_others()
# print(Orb_Elem1.anomalies.mean_anomaly)
Orb_Elem10 = Orb_Elem1
Orb_Elem1e6 = Orb_Elem1
Orb_Elem10.advance_time(100)
print(Orb_Elem1.anomalies.mean_anomaly)
## Have the mean anomaly for 100 seconds in the future now, so I need to convert that back into a true anomaly
## And then the other orbital parameters should not have changed, so I can just throw it back into the class
## And calculate

Orb_Elem1e6.advance_time(1000000)
print(Orb_Elem1.anomalies.mean_anomaly)








if __name__ == "__main__":
    pass