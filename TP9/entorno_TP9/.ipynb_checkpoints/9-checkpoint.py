#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
#* EffortModel
#* Programa para procesar modelos lineales mediante correlación por cuadrados mínimos
#* 
#* UADER - FCyT
#* Ingeniería de Software II
#*
#* Dr. Pedro E. Colla
#* copyright (c) 2023,2024
#*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=
import numpy as np
import pandas as pd
import argparse
import statsmodels.api as sm
import sys
import os
import matplotlib.pyplot as plt

#*------------------------------------------------------------------------------------------------
#* Definición de datasets
#*------------------------------------------------------------------------------------------------
dataset1 = {
    'LOC': [794, 1336, 1572, 1572, 1126],
    'Esfuerzo': [1.07, 1.34, 2.27, 2.39, 0.93]
}

dataset2 = {
    'LOC': [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],
    'Esfuerzo': [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
}

#*------------------------------------------------------------------------------------------------
#* Inicialización del programa
#*------------------------------------------------------------------------------------------------
version="8.0"
linear=False
exponential=False
os.system('clear')

#*------------------------------------------------------------------------------------------------
#* Procesa argumentos
#*------------------------------------------------------------------------------------------------
ap = argparse.ArgumentParser()

ap.add_argument("-v", "--version", required=False, help="version", action="store_true")
ap.add_argument("-x", "--exponential", required=False, help="Exponential model", action="store_true")
ap.add_argument("-l", "--linear", required=False, help="Linear model", action="store_true")
ap.add_argument("--dataset1", required=False, help="Usar dataset Proyectos A–E", action="store_true")
ap.add_argument("--dataset2", required=False, help="Usar dataset histórico LOC–Esfuerzo", action="store_true")

args = vars(ap.parse_args())

if args['version']:
   print("Program %s version %s" % (sys.argv[0],version))
   sys.exit(0)

if args['linear']:
   print("Modelo lineal seleccionado")
   linear=True

if args['exponential']:
   print("Modelo exponencial seleccionado")
   exponential=True

if not linear and not exponential:
   print("Debe indicar modelo lineal (-l) o exponencial (-x) o ambos")

#*-----------------------------------------------------------------------------------------------
#* Selección de dataset
#*-----------------------------------------------------------------------------------------------
if args['dataset1']:
    print("Usando Dataset 1 (Proyectos A–E)")
    data = dataset1
elif args['dataset2']:
    print("Usando Dataset 2 (Histórico LOC–Esfuerzo)")
    data = dataset2
else:
    print("⚠️ No se seleccionó dataset, por defecto se usará Dataset 1 (Proyectos A–E)")
    data = dataset1

df = pd.DataFrame(data)

#*------------------------------------------------------------------------------------------------
#* Correlación LOC vs Esfuerzo
#*------------------------------------------------------------------------------------------------
correlation = df['LOC'].corr(df['Esfuerzo'])
print(f"Correlación LOC–Esfuerzo: {correlation:.4f}")

#*------------------------------------------------------------------------------------------------
#* Procesa modelo lineal
#*------------------------------------------------------------------------------------------------
if linear:
   a, b = np.polyfit(df['LOC'], df['Esfuerzo'], 1)
   R = np.corrcoef(df['LOC'], df['Esfuerzo'], 1)
   R2 = R * R
   r_value = R2[1][0]

   print("Modelo lineal E=%.6f + %.6f*LOC" % (b,a))
   print("El R-squared=%.4f (lineal)" % (r_value))

   lbl=("Modelo lineal (R-Sq=%.2f)" % (r_value))
   plt.plot(df['LOC'], a*df['LOC']+b,label=lbl,color='red')

#*------------------------------------------------------------------------------------------------
#* Procesa modelo exponencial
#*------------------------------------------------------------------------------------------------
if exponential:
   df['logEsfuerzo'] = np.log(df['Esfuerzo'])
   df['logLOC'] = np.log(df['LOC'])

   X = df['logLOC']
   Y = df['logEsfuerzo']
   X = sm.add_constant(X)

   mx= sm.OLS(Y, X).fit()
   print(mx.summary())

   k = np.exp(mx.params['const'])
   b = mx.params['logLOC']

   print("Modelo exponencial E=%.6f*(LOC^%.6f)" % (k,b))
   print("El R-squared=%.2f (exponencial)" % (mx.rsquared))

   lbl=("Modelo exponencial (R-Sq=%.2f)" % (mx.rsquared))
   plt.plot(df['LOC'], k*(df['LOC']**b),label=lbl,color='green')

#*------------------------------------------------------------------------------------------------
#* Gráfico
#*------------------------------------------------------------------------------------------------
plt.scatter(df['LOC'], df['Esfuerzo'], label='Datos históricos')
plt.xlabel('Complejidad [LOC]')
plt.ylabel('Esfuerzo (persona-mes)')
plt.legend()
plt.show()
