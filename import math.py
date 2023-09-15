import math
mEarth = 5.97600 * math.pow(10, 24)
mPlanet = float(input("Write the mass of another planet:"))
rPlaner = float(input("Write the distance to planet:"))
G = 6.6743 * math.pow(10, -11)
F = G * mEarth * mPlanet / rPlaner**2
print(F)