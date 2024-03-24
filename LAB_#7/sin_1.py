from matplotlib import animation
import numpy as np
import matplotlib.pyplot as plt
import webbrowser


def anim_sin():
    #plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')
    t = np.linspace(0, 3*np.pi, 62)
    s = np.sin(t)
    fig = plt.figure(figsize=(6, 3))
    line, = plt.plot(t, s, 'b', lw=2)

    def animate(theta):
        s = np.sin((t-theta)*2) * 0.5
        line.set_data(t, s)
        return line,

    plt.xlabel('t')
    plt.ylabel('s')
    plt.title('Animation_Sin')
    anim = animation.FuncAnimation(fig, animate, frames=np.linspace(0, 2*np.pi, 52), interval=100, blit=True)
    anim.save('sin.gif', writer='imagemagick')
    webbrowser.open('sin.gif')
