import math
import numpy as np
Pu1=float(input("Introdueix la potència necessària per a escalfar l'aigua [W]: "))
Imax=float(input("Introdueix la intensitat màxima per cadascuna de les cel·les d'una placa [A]: "))
ncel=float(input("Introdueix el número de cel·les per placa: "))


nplaques=Pu1/(((0.61*(1+(1/1.62)*np.log((8.36-Imax)/8.36)))*ncel)*Imax)

print (nplaques)
