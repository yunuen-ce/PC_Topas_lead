import numpy as np
import matplotlib.pyplot as plt
import math
# Sensitive volume
import pandas as pd

r = 0.05  # cm
h = 0.1  # cm
vol = math.pi * r ** 2 * h

density = [1.032, 1.1145, 1.13518, 1.5479, 2.0638, 11.35]
density_water = [1, 1.032, 1.1145, 11.35]
density_pvt = [1.032, 1.1145, 2.0638, 11.35]
mass_water = vol * np.array(density_water)
mass_pvt = vol * np.array(density_pvt)
print(mass_water)
print(mass_pvt)

# TOPAS simulations
# material , density,  dose, uncertainty, histories, energy,
data_pvtlead = [['PVT', 1.032, 8.1643805E-13, 1.742E-10, 800000000],
                ['PVT + 0.8% lead', 1.1145, 8.1537054E-13, 1.728E-10, 400000000],
                ['PVT + 1% lead', 1.13518, 8.1258222E-13, 1.731E-10, 400000000],
                ['PVT + 5% lead', 1.5479, 7.9821691E-13, 1.675E-10, 400000000],
                ['PVT + 10% lead', 2.0638, 7.8286862E-13, 1.628E-10, 400000000],
                ['Lead', 11.35, 7.4228687E-13, 1.450E-10, 400000000]
                ]
data_water = [['water', 1, 7.9810887E-13, 1.724E-10, 400000000],
              ['water_pvt', 1.032, 8.1728924E-13, 1.753E-10, 800000000],
              ['water_pvt08', 1.1145, 8.3370683E-13, 1.767E-10, 800000000],
              ['water_lead', 11.3, 7.66296E-13, 1.47E-10, 800000000]
              ]
dose_pvtlead = pd.DataFrame(data_pvtlead, columns=['material', 'density', 'dose', 'unc', 'histories'])
dose_water = pd.DataFrame(data_water, columns=['material', 'density', 'dose', 'unc', 'histories'])

dose_pvtlead.unc = dose_pvtlead.unc / np.sqrt(dose_pvtlead.histories)
dose_water.unc = dose_water.unc / np.sqrt(dose_water.histories)

# EGSnrc
det_water = [1.545655e-11, 0.42399]
det_pvt = [1.477662e-11, 0.42408]
det_08pb = [1.452196e-11, 0.43661]
det_10pb = [1.270548e-11, 0.42898]
EGSnrc = np.array([det_water, det_pvt, det_08pb, det_10pb])
# SUBSET for comparison
TOPAS = np.zeros([4, 2])
TOPAS[0] = np.array(dose_water.dose[dose_water.material == 'water'], dose_water.unc[dose_water.material == 'water'])
TOPAS[1] = np.array(dose_pvtlead.dose[dose_pvtlead.material == 'PVT'], dose_pvtlead.unc[dose_pvtlead.material == 'PVT'])
TOPAS[2] = np.array(dose_pvtlead.dose[dose_pvtlead.material == 'PVT + 0.8% lead'],
                    dose_pvtlead.unc[dose_pvtlead.material == 'PVT + 0.8% lead'])
TOPAS[3] = np.array(dose_pvtlead.dose[dose_pvtlead.material == 'PVT + 10% lead'],
                    dose_pvtlead.unc[dose_pvtlead.material == 'PVT + 10% lead'])

egs_labels = ['water', 'pvt', 'pvt + 0.8 % pb', 'pvt + 10 % pb']
plt.errorbar(range(len(egs_labels)), EGSnrc[:, 0] / EGSnrc[1, 0],
             yerr=(EGSnrc[:, 0] / EGSnrc[1, 0]) * np.sqrt((EGSnrc[:, 1] / 100) ** 2 + (EGSnrc[:, 1] / 100) ** 2),
             fmt='o', linestyle=':', label='EGSnrc')
plt.errorbar(range(len(egs_labels)), TOPAS[:, 0] / TOPAS[1, 0],
             yerr=(TOPAS[:, 0] / TOPAS[1, 0]) * np.sqrt(
                 (TOPAS[:, 1] / TOPAS[:, 0] / 100) ** 2 + (TOPAS[0, 1] / TOPAS[1, 0] / 100) ** 2),
             fmt='s', linestyle=':', label='TOPAS')

plt.xticks(range(len(egs_labels)), egs_labels)
plt.ylabel('Dose/Dose[water]')
plt.legend()
plt.show()

# Energy simulations
# material , density,  dose, uncertainty, histories, energy,
data_energy_water = [['water', 1, 4.06E-06, 0.000865821, 800000000],
                     ['water_pvt', 1.032, 4.26E-06, 0.00090554, 800000000],
                     ['water_pvt08', 1.1145, 4.53E-06, 0.000964286, 800000000],
                     ['water_lead', 11.3, 4.33E-05, 0.008305073, 800000000]]
data_energy_pvtlead = [['PVT', 1.032, 4.10931943638226E-06, 0.00087897, 800000000],
                       ['PVT + 0.8% lead', 1.1145, 4.43002713696295E-06, 0.000940074, 400000000],
                       ['PVT + 10% lead', 2.0638, 7.83E-06, 0.001640342, 400000000],
                       ['Lead', 11.35, 4.17E-05, 0.008072565, 400000000]
                       ]

energy_water = pd.DataFrame(data_energy_water, columns=['material', 'density', 'energy', 'unc', 'histories'])
energy_pvtlead = pd.DataFrame(data_energy_pvtlead, columns=['material', 'density', 'energy', 'unc', 'histories'])
energy_water.unc = energy_water.unc / np.sqrt(energy_water.histories)
energy_pvtlead.unc = energy_pvtlead.unc / np.sqrt(energy_pvtlead.histories)
x = range(4)

plt.plot(x, dose_water.dose / dose_water.dose[0], marker='s', label='dose topas')
plt.plot(x, energy_water.energy / energy_water.energy[0], marker='d',  label='energy topas')
plt.plot(x, mass_water / mass_water[0],  marker='o', label='mass')
plt.plot(x, (energy_water.energy / mass_water) / (energy_water.energy[0] / mass_water[0]),  marker='*', label='Dose manual')
plt.ylabel('scorer/scorer[0]')
plt.xlabel('Density [g/cm3]')
plt.xticks(x, density_water)
plt.title('water')
plt.legend()
plt.show()

plt.plot(x, dose_pvtlead.dose[0:4] / dose_pvtlead.dose[0],  marker='s', label='dose topas')
plt.plot(x, energy_pvtlead.energy / energy_pvtlead.energy[0], marker='d', label='energy topas')
plt.plot(x, mass_pvt / mass_pvt[0],  marker='o', label='mass')
plt.plot(x, (energy_pvtlead.energy / mass_pvt) / (energy_pvtlead.energy[0] / mass_pvt[0]), marker='*', label='Dose manual')
plt.ylabel('scorer/scorer[0]')
plt.xlabel('')
plt.xticks(x, energy_pvtlead.material)
plt.title('pvt + lead')
plt.legend()
plt.show()


'''
EGSnrc results:
Finished simulation

Total cpu time for this run:            0.04 (sec.) 0.0000(hours)
CPU time including previous runs:       5837186.34 (sec.) 1621.4406 (hours)
Histories per hour:                     1.38938e+06   
Number of random numbers used:          144960360330081
Number of electron CH steps:            7.1178e+12    
Number of all electron steps:           8.37222e+12   


 last case = 2252800080 fluence = 1.408e+08

Geometry                        Cavity dose      
-----------------------------------------------
Setup_det10Pb             1.270548e-11 +/- 0.42898  % 
Setup_det08Pb             1.452196e-11 +/- 0.43661  % 
Setup_detPVT              1.477662e-11 +/- 0.42408  % 
Setup_detwater            1.545655e-11 +/- 0.42399  % 


Geometry 1           Geometry 2              Dose ratio
Setup_det08Pb        Setup_detwater           0.93953  +/- 0.00572
Setup_det10Pb        Setup_detwater           0.82201  +/- 0.00496
Setup_detPVT         Setup_detwater           0.95601  +/- 0.00573


'''