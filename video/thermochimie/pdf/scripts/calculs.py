"""Toutes les valeurs numériques et données de figures du cours de thermochimie.
Chaque bloc imprime des valeurs étiquetées, reprises telles quelles dans le LaTeX."""
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq
import os
D = os.path.join(os.path.dirname(__file__), '..', 'data')
R, F, T0 = 8.314, 96485.0, 298.15
ln10 = np.log(10)
print(f"RT ln10 / F (298 K) = {R*T0*ln10/F:.5f} V")

# Données (298 K) : DfH kJ/mol, Sm J/K/mol, DfG kJ/mol, Cp J/K/mol
d = {
 'N2':(0,191.6,0,29.1),'H2':(0,130.7,0,28.8),'O2':(0,205.2,0,29.4),
 'NH3':(-45.9,192.8,-16.4,35.1),'CH4':(-74.6,186.3,-50.5,35.7),
 'Cl2':(0,223.1,0,33.9),'CH3Cl':(-81.9,234.6,None,None),'HCl':(-92.3,186.9,-95.3,29.1),
 'CO2':(-393.5,213.8,-394.4,37.1),'CO':(-110.5,197.7,-137.2,29.1),
 'H2Ol':(-285.8,70.0,-237.1,75.3),'H2Og':(-241.8,188.8,-228.6,33.6),
 'Cgr':(0,5.7,0,8.5),'CaCO3':(-1207.6,91.7,-1129.1,83.5),'CaO':(-634.9,38.1,-603.3,42.0),
 'Ag2O':(-31.1,121.3,-11.2,None),'ZnO':(-350.5,43.7,-320.5,None),
}
def rx(eq):
    H = sum(n*d[s][0] for s,n in eq.items())
    S = sum(n*d[s][1] for s,n in eq.items())
    return H, S
def hdr(t): print(f"\n=== {t}")

hdr("Coherence DfG = DfH - T DfS (NH3, H2O l)")
for sp, el in [('NH3',{'N2':0.5,'H2':1.5}),('H2Ol',{'H2':1,'O2':0.5})]:
    dS = d[sp][1]-sum(n*d[s][1] for s,n in el.items())
    print(sp, f"DfS={dS:.1f}  DfG calc={d[sp][0]-T0*dS/1000:.1f}  table={d[sp][2]}")

hdr("CH4 + Cl2 -> CH3Cl + HCl")
H,_ = rx({'CH3Cl':1,'HCl':1,'CH4':-1,'Cl2':-1}); print(f"DrH = {H:.1f} kJ/mol")

hdr("Synthese NH3 : N2 + 3H2 = 2NH3")
H,S = rx({'NH3':2,'N2':-1,'H2':-3})
G298 = H - T0*S/1000
K = lambda T: np.exp(-(H*1e3 - T*S)/(R*T))
print(f"DrH={H:.1f} kJ/mol DrS={S:.1f} J/K/mol DrG(298)={G298:.2f} kJ/mol K(298)={K(T0):.3e}")
Ti = H*1e3/S; print(f"T inversion = {Ti:.0f} K = {Ti-273.15:.0f} C")
for T in (500, 673, 723, 773):
    print(f"T={T} DrG={(H*1e3-T*S)/1e3:.1f} kJ/mol K={K(T):.3e} lnK={np.log(K(T)):.2f}")
# Van't Hoff intégré entre 298 et 723
print(f"VH integre: K723 = K298*exp(-DrH/R(1/723-1/298)) = {K(T0)*np.exp(-H*1e3/R*(1/723-1/T0)):.3e}")
# Mélange à 723 K
pN2,pH2,pNH3 = 50,150,20
Q = pNH3**2/(pN2*pH2**3); print(f"Q melange (50,150,20 bar) = {Q:.3e}; K(723)={K(723):.3e}; Q<K: {Q<K(723)}")
print(f"DrG = RT ln(Q/K) = {R*723*np.log(Q/K(723))/1e3:.1f} kJ/mol")
Ts = np.linspace(300, 900, 61)
np.savetxt(f"{D}/nh3_drg.dat", np.c_[Ts, (H*1e3-Ts*S)/1e3], header='T DrG_kJ', comments='')
Ts2 = np.linspace(400, 900, 11)
np.savetxt(f"{D}/nh3_vh.dat", np.c_[1000/Ts2, np.log(K(Ts2))], header='invT_milli lnK', comments='')
# équilibre à 723 K, P=200 bar, mélange stoechiométrique 1:3
for P in (1, 50, 200, 300):
    f = lambda x: (2*x)**2*(4-2*x)**2/((1-x)*(3-3*x)**3)/P**2 - K(723)
    x = brentq(f, 1e-9, 1-1e-9); print(f"723 K, P={P} bar : xi={x:.4f}  x_NH3={2*x/(4-2*x):.3f}")

hdr("CaCO3(s) = CaO(s) + CO2(g)")
H,S = rx({'CaO':1,'CO2':1,'CaCO3':-1})
K = lambda T: np.exp(-(H*1e3 - T*S)/(R*T))
print(f"DrH={H:.1f} kJ/mol DrS={S:.1f} J/K/mol T(K=1)={H*1e3/S:.0f} K ({H*1e3/S-273.15:.0f} C)")
T, V = 1100, 10e-3
Pe = K(T)*1e5; neq = Pe*V/(R*T)
print(f"K(1100)={K(T):.3f} -> P_eq={Pe/1e5:.3f} bar ; n_CO2,eq (10 L) = {neq*1e3:.1f} mmol")
for n0 in (0.10, 0.05):
    if n0 > neq: print(f"n0={n0}: equilibre, xi={neq:.4f} mol, reste CaCO3 {n0-neq:.4f}")
    else: print(f"n0={n0}: rupture, P={n0*R*T/V/1e5:.3f} bar < {K(T):.3f}, DrG={R*T*np.log(n0*R*T/V/1e5/K(T))/1e3:.2f} kJ/mol")
n0s = np.linspace(0, 0.15, 151); P = np.minimum(n0s*R*T/V/1e5, K(T))
np.savetxt(f"{D}/caco3.dat", np.c_[n0s*1e3, P], header='n0_mmol P_bar', comments='')

hdr("Combustion CH4 : flamme adiabatique")
H,_ = rx({'CO2':1,'H2Og':2,'CH4':-1,'O2':-2})
Hl,_ = rx({'CO2':1,'H2Ol':2,'CH4':-1,'O2':-2})
print(f"DrH (H2O g) = {H:.1f} ; DrH (H2O l) = {Hl:.1f} kJ/mol")
Cair = d['CO2'][3]+2*d['H2Og'][3]+8*d['N2'][3]
CO2 = d['CO2'][3]+2*d['H2Og'][3]
print(f"Sum Cp air = {Cair:.1f} J/K -> Tf = {T0 - H*1e3/Cair:.0f} K ; O2 pur: Sum Cp = {CO2:.1f} -> Tf = {T0 - H*1e3/CO2:.0f} K")
n = 1e5*1/(R*T0); print(f"1 m3 CH4 a 1 bar/298 K : n = {n:.1f} mol ; Q (H2O l) = {n*Hl/1e3:.1f} MJ = {n*Hl/3600:.2f} kWh")

hdr("Boudouard C(gr) + CO2 = 2CO")
H,S = rx({'CO':2,'CO2':-1,'Cgr':-1})
K = lambda T: np.exp(-(H*1e3 - T*S)/(R*T))
print(f"DrH={H:.1f} DrS={S:.1f} T(K=1)={H*1e3/S:.0f} K K(1000)={K(1000):.3f} K(800)={K(800):.3e}")
for P, ninert in ((1,0),(10,0),(1,4)):
    f = lambda x: (2*x)**2/((1-x)*(1+x+ninert))*P - K(1000)
    x = brentq(f, 1e-12, 1-1e-12); print(f"P={P} bar, n_inerte={ninert}: xi={x:.3f}  x_CO={2*x/(1+x+ninert):.3f}")
print(f"formule xi=sqrt(K/(4P+K)) P=1: {np.sqrt(K(1000)/(4+K(1000))):.3f} ; P=10: {np.sqrt(K(1000)/(40+K(1000))):.3f}")

hdr("G(xi) isomerisation A(g)=B(g), P=P0")
dG0 = -2.0e3; Kab = np.exp(-dG0/(R*T0)); xe = Kab/(1+Kab)
print(f"DrG0=-2.0 kJ/mol -> K={Kab:.3f}, xi_eq={xe:.3f}")
x = np.linspace(1e-4, 1-1e-4, 400)
Gl = x*dG0/1e3; Gm = R*T0*((1-x)*np.log(1-x)+x*np.log(x))/1e3
np.savetxt(f"{D}/gxi.dat", np.c_[x, Gl+Gm, Gl, Gm], header='xi G Glin Gmix', comments='')
Ge = xe*dG0/1e3 + R*T0*((1-xe)*np.log(1-xe)+xe*np.log(xe))/1e3
print(f"G(xi_eq) = {Ge:.3f} kJ ; DrG(xi=0.3)={(dG0+R*T0*np.log(0.3/0.7))/1e3:.2f} ; DrG(0.9)={(dG0+R*T0*np.log(0.9/0.1))/1e3:.2f}")
for xx in (0.3, 0.9):
    print(f"G({xx}) = {(xx*dG0+R*T0*((1-xx)*np.log(1-xx)+xx*np.log(xx)))/1e3:.3f}")

hdr("Potentiels standard")
print(f"Calomel: 0.79 - 0.03*pKs(17.9) = {0.797 - R*T0*ln10/(2*F)*17.9:.3f} V (avec 0.79-0.03*17.3 = {0.79-0.03*17.3:.2f})")
print(f"Fe3+/Fe = (0.77 + 2*(-0.44))/3 = {(0.77+2*(-0.44))/3:.4f} V")
print(f"O2/H2O = 2*237.1e3/(4F) = {2*237.1e3/(4*F):.3f} V")
Ecu = 2*0.34-0.16; Kd = 10**((Ecu-0.16)/0.06)
print(f"Cu+/Cu = {Ecu:.2f} V ; dismutation K = 10^{(Ecu-0.16)/0.06:.1f} = {Kd:.2e}")

hdr("Pile Daniell")
e0 = 0.34-(-0.76); print(f"e0 = {e0:.2f} V ; DrG0 = {-2*F*e0/1e3:.1f} kJ/mol ; log K = 2*1.10/0.06 = {2*e0/0.06:.1f} (0.0592: {2*e0/(R*T0*ln10/F):.1f})")
xi = 1/65.4; q = 2*F*xi; print(f"1 g Zn : xi = {xi*1e3:.2f} mmol, Q = {q:.0f} C = {q/3600:.3f} A.h ; W ~ Q e0 = {q*e0:.0f} J")
c0, Vc = 0.10, 50e-3; ximax = c0*Vc
xis = np.linspace(0, ximax*(1-1e-9), 4000)
E = e0 - R*T0*ln10/(2*F)*np.log10((c0+xis/Vc)/(c0-xis/Vc))
G = -2*F*np.concatenate([[0], np.cumsum(0.5*(E[1:]+E[:-1])*np.diff(xis))])/1e3
sel = np.r_[0:3900:30, 3900:4000:2, 3999]
np.savetxt(f"{D}/daniell.dat", np.c_[2*F*xis[sel], E[sel], G[sel]], header='q E G_kJ', comments='')
print(f"ximax={ximax*1e3} mmol, Qmax={2*F*ximax:.0f} C ; E a 50%: {E[2000]:.3f} V ; a 99%: {e0 - R*T0*ln10/(2*F)*np.log10(1.99/0.01):.3f} V; G final={G[-1]:.3f} kJ vs -2F e0 ximax = {-2*F*e0*ximax/1e3:.3f}")

hdr("Pile a combustible H2/O2")
print(f"e0 = 237.1e3/(2F) = {237.1e3/(2*F):.3f} V ; rendement max = 237.1/285.8 = {237.1/285.8:.3f}")

hdr("Pile bouton Zn/Ag2O : Zn + Ag2O -> ZnO + 2Ag")
G0 = d['ZnO'][2]-d['Ag2O'][2]; print(f"DrG0 = {G0:.1f} kJ/mol ; e0 = {-G0*1e3/(2*F):.3f} V")
n = 0.50/231.7; q = 2*F*n; print(f"0.50 g Ag2O: n = {n*1e3:.3f} mmol, Q = {q:.0f} C = {q/3.6:.0f} mA.h ; W = {q*(-G0*1e3/(2*F)):.0f} J = {q*(-G0*1e3/(2*F))/3600*1000:.0f} mW.h")
print(f"Zn necessaire : {n*65.4*1e3:.0f} mg")

hdr("Reacteur adiabatique (simulation)")
n0, DrH, C, Ea, k298 = 1.0, -120e3, 3.0e3, 80e3, 2.0e-4
k = lambda T: k298*np.exp(-Ea/R*(1/T-1/T0))
def f(t, y):
    xi, T = y; v = k(T)*(n0-xi); return [v, -DrH*v/C]
ts = np.linspace(0, 3600, 361)
sol = solve_ivp(f, (0, 3600), [0, T0], t_eval=ts, rtol=1e-8, atol=1e-10)
iso = n0*(1-np.exp(-k298*ts))
np.savetxt(f"{D}/adiab.dat", np.c_[ts/60, sol.y[1]-273.15, sol.y[0], iso], header='tmin TC xi xiiso', comments='')
print(f"DeltaT_ad = {-DrH*n0/C:.1f} K ; T final = {sol.y[1][-1]-273.15:.1f} C ; xi(10 min) adiab={np.interp(600,ts,sol.y[0]):.3f} iso={np.interp(600,ts,iso):.3f}")
print(f"t_1/2 adiab = {np.interp(0.5, sol.y[0], ts)/60:.1f} min ; iso = {np.log(2)/k298/60:.1f} min ; k(T_f)/k(298) = {k(T0-DrH*n0/C)/k298:.1f}")

hdr("Exercice calorimetrie neutralisation")
DrH = -285.8 - (-230.0); print(f"DrH neutralisation = {DrH:.1f} kJ/mol")
Ceau = 200*4.18; Ccal = 120; xi = 0.100
print(f"C eau = {Ceau:.0f} J/K ; dT theo (sans cal) = {-xi*DrH*1e3/Ceau:.2f} K ; avec cal = {-xi*DrH*1e3/(Ceau+Ccal):.2f} K")
print(f"DrH mesure (dT=5.8 K) = {-(Ceau+Ccal)*5.8/xi/1e3:.1f} kJ/mol")

hdr("Exercice pile a combustible")
DrH, DrS = -285.8, 70.0-130.7-0.5*205.2
print(f"par mol H2 : DrS = {DrS:.1f} J/K/mol ; de/dT = {DrS/(2*F)*1e3:.3f} mV/K")
for T in (298.15, 353.15):
    G = DrH*1e3 - T*DrS; print(f"T={T}: DrG={G/1e3:.1f} kJ/mol e0={-G/(2*F):.4f} V")
n = 1000/2.016; print(f"1 kg H2: n={n:.0f} mol ; W = {n*237.1e3/1e6:.1f} MJ = {n*237.1e3/3.6e6:.1f} kWh ; q = {2*F*n:.3e} C = {2*F*n/3600:.0f} A.h")
print(f"air P_O2=0.2: e = 1.229 + 0.059/4*log10(0.2) = {1.229+0.0592/4*np.log10(0.2):.3f}")

hdr("Exercice cuivre")
lnK = 0.36*F/(R*T0); print(f"K dismutation = {np.exp(lnK):.3e} ; DrG0 = {-F*0.36/1e3:.1f} kJ/mol")
for K in (1e6, np.exp(lnK)):
    print(f"K={K:.2e}: [Cu+] residuel = {np.sqrt(0.005/K):.2e}")
# exact
f = lambda c: (0.010-c)/2/c**2 - 1e6
print("exact (K=1e6):", brentq(f, 1e-9, 0.01))

hdr("Exercice pile bouton duree")
q = 416; print(f"duree a 2 uA : {q/2e-6:.3e} s = {q/2e-6/3.156e7:.1f} ans")
