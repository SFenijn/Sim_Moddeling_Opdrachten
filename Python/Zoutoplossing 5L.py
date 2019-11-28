import numpy
import matplotlib.pyplot

# Een tank bevat 1000 liter puur water.
# Vanaf t=0 vloeit er met een constante snelheid van 6 L/min een zoutoplossing de tank in.
# Het water in de tank wordt goed geroerd.
# Aan de andere kant van de tank stroomt er ook weer water weg met een snelheid van 6 L/min.
# De concentratie van het zout in de instromende oplossing is 0.1 kg/L.

# Bepaal mbv numerieke methoden het verloop in de tijd van de zoutconcentratie in de tank. Plot het verloop.

# aantal stappen dat we nemen. Één stap is één minuut.
num_steps = 50


# hoeveelheid zout dat per stap in de tank komt. 0.1kg/L * 6L
v = 0.1 * 6  # 0.6

# zoutgehalte in de tank op het begin moment.
z = [0]

# De stap groote die we zetten.
t = numpy.arange(num_steps+1)

# aanmaak van numpy array.
z = numpy.zeros(num_steps+1)

for step in range(num_steps):
    z[step+1] = z[step] + (v - (5/1000*z[step])) * t[step]


def plot_me():
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, z)
    axes_height.set_ylabel('Zout in Kg')
    axes_height.set_xlabel('Time in minutes')
    matplotlib.pyplot.show()


plot_me()