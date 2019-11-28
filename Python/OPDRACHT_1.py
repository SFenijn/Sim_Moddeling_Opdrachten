import numpy
import matplotlib.pyplot

def forward_euler():
    h=0.1
    g=9.81
    friction = 0.002
    s = -0.1

    num_steps = 1000
    t = numpy.zeros(num_steps+1)
    x = numpy.zeros(num_steps+1)
    v = numpy.zeros(num_steps+1)
    # verander begin snelheid v (lijkt op spring een duw geven)
    # v[0] = 5
    # verander begin positie x. (Lijkt op spring uitrekken en dan loslaten)
    x[0] = 10

    for step in range(num_steps):
        #schrijf hier code voor Euler-integratie
        t[step+1] = t[step] + h

        # Velocity zonder gravity met spring en friction.
        v[step + 1] = v[step] + s * x[step] - friction*v[step]

        x[step+1] = x[step] + v[step+1]*h

    return t,x,v

t,x,v = forward_euler()

def plot_me():
    axes_height = matplotlib.pyplot.subplot(211)
    matplotlib.pyplot.plot(t, x)
    axes_velocity = matplotlib.pyplot.subplot(212)
    matplotlib.pyplot.plot(t, v)
    axes_height.set_ylabel('Height in m')
    axes_velocity.set_ylabel('Velocity in m/s')
    axes_velocity.set_xlabel('Time in s')
    matplotlib.pyplot.show()

plot_me()