# Modelo 2
# Importar el módulo SymPy
import sympy as sym
from sympy import symbols
from sympy.plotting import plot
f1 = "10-x" #<=
f2 = "x-1" #>=
f3 = "4" # <=
Z1 = "(16-x)/2"
Z2 = "(14-x)/2"
Z3 = "(13-x)/2"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -15, 15))
# Sol: Z=13 x1=5 x2=4