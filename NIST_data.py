import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


water = pd.read_csv("Water_nist.txt", sep=" ", header=None, skiprows=8, names=[
                         'Kin_energy', 'S_col', 'S_rad', 'S_total', 'CSDA',  'Radiation_yield', 'Density_effect', 'useless'])
lead = pd.read_csv("Lead_nist.txt", sep=" ", header=None, skiprows=8, names=[
                         'Kin_energy', 'S_col', 'S_rad', 'S_total', 'CSDA',  'Radiation_yield', 'Density_effect', 'useless'])
pvt = pd.read_csv("PVT_nist.txt", sep=" ", header=None, skiprows=8, names=[
                         'Kin_energy', 'S_col', 'S_rad', 'S_total', 'CSDA',  'Radiation_yield', 'Density_effect', 'useless'])
pvt_08pb = pd.read_csv("EJ256_08Pb.txt", sep=" ", header=None, skiprows=8, names=[
                         'Kin_energy', 'S_col', 'S_rad', 'S_total', 'CSDA',  'Radiation_yield', 'Density_effect', 'useless'])
water = water.iloc[:, :-1]
lead = lead.iloc[:, :-1]
pvt = pvt.iloc[:, :-1]


plt.plot(water.Kin_energy, water.S_total,   label='water')
plt.plot(lead.Kin_energy, lead.S_total,   label='lead')
plt.plot(pvt.Kin_energy, pvt.S_total,   label='pvt')
plt.plot(pvt_08pb.Kin_energy, pvt_08pb.S_total,   label='pvt_08pb')
plt.axvline(x = 6, linestyle=':')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Stopping power [MeV cm2/g]')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.show()

plt.plot(water.Kin_energy, water.S_rad,   label='water')
plt.plot(lead.Kin_energy, lead.S_rad,   label='lead')
plt.plot(pvt.Kin_energy, pvt.S_rad,   label='pvt')
plt.plot(pvt_08pb.Kin_energy, pvt_08pb.S_rad,   label='pvt_08pb')
plt.axvline(x = 6, linestyle=':')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Radiative stopping power [MeV cm2/g]')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.show()

plt.plot(water.Kin_energy, water.S_col,   label='water')
plt.plot(lead.Kin_energy, lead.S_col,   label='lead')
plt.plot(pvt.Kin_energy, pvt.S_col,   label='pvt')
plt.plot(pvt_08pb.Kin_energy, pvt_08pb.S_col,   label='pvt_08pb')
plt.axvline(x = 6, linestyle=':')
plt.xscale('log')
plt.yscale('log')
plt.ylabel('Collision stopping power [MeV cm2/g]')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.show()

plt.plot(water.Kin_energy, water.Density_effect, label='water')
plt.plot(lead.Kin_energy, lead.Density_effect, label='lead')
plt.plot(pvt.Kin_energy, pvt.Density_effect, label='pvt')
plt.plot(pvt_08pb.Kin_energy, pvt_08pb.Density_effect, label='pvt_08pb')
plt.axvline(x = 6, linestyle=':')
plt.xscale('log')
plt.ylabel('Density yeffect parameter')
plt.xlabel('Energy [MeV]')
plt.legend()
plt.show()


plt.plot(water.Kin_energy, water.CSDA, label='water')
plt.plot(lead.Kin_energy, lead.CSDA, label='lead')
plt.plot(pvt.Kin_energy, pvt.CSDA, label='pvt')
plt.plot(pvt_08pb.Kin_energy, pvt_08pb.CSDA, label='pvt_08pb')
plt.axvline(x = 6, linestyle=':')
#plt.xscale('log')
plt.ylabel('CSDA range [g/cm2]')
plt.xlabel('Energy [MeV]')
plt.xlim([0, 10])
plt.ylim([0, 10])
plt.legend()
plt.show()

