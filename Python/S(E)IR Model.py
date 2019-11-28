import numpy
import matplotlib.pyplot

# Werk de SIR-casus uit 'Differential equations in action' uit met andere getallen. Baseer de grootte van de populatie,
# het gemiddelde aantal contacten per dag en de kans op infectie op je eigen studentnummer.
# Voorbeeld:
# Bij studentnummer 16 9 44 96 wordt de grootte van de populatie 96 miljoen, het gemiddelde aantal contacten per dag 44
# en de kans op infectie 9%.
# a. Stel een SIR-model op voor jouw situatie. Laat duidelijk zien hoe de constanten zijn afgeleid.
# b. Hoeveel mensen moeten gevaccineerd worden om een epidemie te voorkomen?
# c. Introduceer een latency van twee dagen in je model en maak plots van het verloop van de ziekte in jouw populatie.

# aantal stappen dat we nemen. Één stap is één minuut.
num_steps = 50
# grote van populatie
s = numpy.zeros(num_steps+1)
s[0] = 17000000
# infected populatie
i = numpy.zeros(num_steps+1)
# genezen populateie
r = numpy.zeros(num_steps+1)
# aantal contacten per dag
c = 54
# % kans op infectie
k = 0.71
# De stap groote die we zetten.
t = numpy.arange(num_steps+1)
# duratie van ziekte
d = 5

# kans op infectie
a = k / s[0] * c
print(a)


for step in range(num_steps):
    # model voor supcepteble personen
    s[step+1] = s[step] - (a * i[step] * s[step])
    # model voor infectie
    i[step+1] = i[step] + (a * i[step] * s[step]) - ((1 / d) * i[step])
    # model voor recovery
    r[step+1] = r[step] + (1 / d) * i[step]


def plot_me():
    axes_height = matplotlib.pyplot.subplot()
    matplotlib.pyplot.plot(t, s)
    axes_height.set_ylabel('Aantal p ziek kan worden')
    matplotlib.pyplot.show()


plot_me()