from Modelos import *
from Variantes import *
from matplotlib import pyplot
def f1(x):
    return 5+0*x
def f2(x):
    return 8-2*x
x = range(0, 5)
pyplot.plot(x, [f1(i) for i in x])
pyplot.plot(x, [f2(i) for i in x])
# Establecer el color de los ejes.
pyplot.axhline(0, color="black")
pyplot.axvline(0, color="black")
# Limitar los valores de los ejes.
pyplot.xlim(0, 5)
pyplot.ylim(0, 7)
# Guardar gráfico como imágen PNG.
pyplot.savefig("output.png")
# Mostrarlo.
pyplot.show()