import math
from Anomalies import Anomalies
from Planets import Planets
import constants as c
import scipy.constants as spc
import numpy as np

def semimajor_eccentricity(ha, hp, planet):
    ra, rp = planet._radius + ha, planet._radius + ha
    semimajor_axis = (ra + rp)/2.
    eccentricity = (ra - rp)/(ra + rp)
    return semimajor_axis, eccentricity

def period_from_a(a, planet):
    period = 2. * spc.pi * math.sqrt(a**3/(planet._mass* spc.gravitational_constant))
    return period

def problem_4():
    r = np.array([-5650.0,-2650.0,2850.0])
    v = np.array([2.415,-7.032,-1.796])
    h = np.cross(r,v)
    mu = spc.gravitational_constant * Earth._mass
    eccentricity = np.linalg.norm(((np.linalg.norm(v)**2 - mu/np.linalg.norm(r)) * r - (np.dot(r,v)) * v)/(mu))
    specific_energy = 0.5 * np.linalg.norm(v)**2 - mu/np.linalg.norm(r)
    semimajor_axis = -(mu/(2. * specific_energy))
    inclination = math.degrees(math.acos(h[2]/np.linalg.norm(h)))
    fpa = math.degrees(math.acos(np.dot(r,v)/(np.linalg.norm(r) * np.linalg.norm(v)))) - 90.
    return h, specific_energy, eccentricity, semimajor_axis, inclination, fpa


if __name__ == "__main__":
    print("Problem #1:")
    Earth = Planets("Earth", c.earth_mass, c.earth_radius)
    #Case A
    A = Anomalies(0.15, 2. * Earth._radius,Earth, time_past_periapse=0)
    print("Case A:")
    print("True Anomaly: " + str(A.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(A.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(A.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(A.time_past_periapse) + " minutes")
    print("-------------------------------")
    B = Anomalies(.15,2.* Earth._radius,Earth, true_anomaly= 30.)
    print("Case B:")
    print("True Anomaly: " + str(B.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(B.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(B.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(B.time_past_periapse) + " minutes")
    print("-------------------------------")
    C = Anomalies(.15,2.* Earth._radius, Earth,eccentric_anomaly= 200.)
    print("Case C:")
    print("True Anomaly: " + str(C.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(C.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(C.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(C.time_past_periapse) + " minutes")
    print("-------------------------------")
    D = Anomalies(.15,2.* Earth._radius, Earth, true_anomaly= 90.)
    print("Case D:")
    print("True Anomaly: " + str(D.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(D.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(D.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(D.time_past_periapse) + " minutes")
    print("-------------------------------")
    E = Anomalies(.15,2.* Earth._radius, Earth, mean_anomaly= 270.)
    print("Case E:")
    print("True Anomaly: " + str(E.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(E.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(E.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(E.time_past_periapse) + " minutes")
    print("-------------------------------")
    F = Anomalies(.15,2.* Earth._radius, Earth, time_past_periapse= 25)
    print("Case F:")
    print("True Anomaly: " + str(F.true_anomaly)+ " degrees")
    print("Eccentric Anomaly: " + str(F.eccentric_anomaly)+ " degrees")
    print("Mean Anomaly: " + str(F.mean_anomaly) + " degrees")
    print("Time past Periapse: " + str(F.time_past_periapse) + " minutes")
    print("-------------------------------")

    print("Problem 2:")
    ha, hp = 551., 321.
    sa, ecc2 = semimajor_eccentricity(ha, hp, Earth)
    p2_anomaly_initial = Anomalies(ecc2, sa, Earth, true_anomaly=330.)
    time_to_deploy = p2_anomaly_initial.time_past_periapse + 65.
    p2_anomaly_final = Anomalies(ecc2, sa, Earth, time_past_periapse=time_to_deploy)
    print("The true anomaly at the time of deployment is " + str(p2_anomaly_final.true_anomaly))

    print("Problem 3:")
    ha_3_1, hp_3_1 = 817., 789.
    ha_3_2, hp_3_2 = 814., 794.
    sa_3_1, ecc_3_1 = semimajor_eccentricity(ha_3_1,hp_3_1, Earth)
    sa_3_2, ecc_3_2 = semimajor_eccentricity(ha_3_2, hp_3_2, Earth)
    period_1 = period_from_a(sa_3_1, Earth)
    period_2 = period_from_a(sa_3_2, Earth)
    print("The error in the semi-major axis is: " +str(abs(sa_3_2 - sa_3_1)) + " km")
    print("The error in the eccentricity is: " +str(abs(ecc_3_2 - ecc_3_1)))
    print("The error in the periods is: " +str(abs(period_2 - period_1)))

    print("Problem 4:")
    h, specific_energy, eccentricity, semimajor_axis, inclination, fpa = problem_4()
    print("L = :")
    print(h)
    print("specific energy: " + str(specific_energy))
    print("eccentricity: " + str(eccentricity))
    print("semimajor axis: " + str(semimajor_axis))
    print("inclination: " + str(inclination))
    print("flight path angle: " + str(fpa))