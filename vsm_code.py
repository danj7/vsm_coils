import numpy as np
import matplotlib.pyplot as plt

def G_r(y_c, z_c, radius, integration_steps = 1000):
    """
    Returns array of sensitivity of wire loop at position (0,y_c,z_c) of a given radius.

    Parameters
    ----------
    y_c:    list or array-like
        Multiple y coordinates can be input, this i used to generate the solenoid shape.
    z_c:    float
        Z-coordinate of loop(s).
    radius: float
        Radius of loop(s).
    integration_steps:   int
        Number of steps in integration.
    """
    y_c = y_c.reshape(y_c.shape[0], 1)
    theta = np.linspace(0,2*np.pi,integration_steps)
    result = ( (radius*np.cos(theta))*(radius**2 + y_c**2 + z_c**2 - 2*z_c*radius*np.cos(theta))**1.5
              + 3.0*(radius*np.cos(theta) - z_c)*(z_c*radius*np.cos(theta) - radius**2)
              *(radius**2 + y_c**2 + z_c**2 - 2*z_c*radius*np.cos(theta))**0.5
    )/( (radius**2 + y_c**2 + z_c**2 - 2*z_c*radius*np.cos(theta))**3. )
    return result.sum(axis=-1)

def G_solenoid(y_c, z_c, radius, nturns, wire_diam=0.006325):
    """
    Returns sensitivity of a solenoid-like set of wire loops with y_c as center of first loop.

    Parameters
    ----------
    y_c:    float
        Y-coordinate of first loop.
    z_c:    float
        Z-coordinate of first loop. Same for all.
    radius: float
        Radius of loops.
    nturns:    int
        Number of wire turns in the solenoid.
    wire_diam: float
        Diameter of wire used. By default it is set to AWG 42 wire.
    """
    y_c = np.linspace(y_c, y_c + wire_diam*nturns, nturns)
    return G_r(y_c, z_c, radius).sum(axis=-1)

def G_coil(y_c, z_c, radius_int, radius_ext, height, wire_diam=0.006325):
    """
    Reutrns sensitivity of an entire detection coil.

    Pamaters
    --------
    y_c:    float
        Y-coordinate of first loop.
    z_c:    float
        Z-coordinate of first loop. Same for all.
    radius_int: float
        Internal radius of core/smallest radius in the coil.
    radius_ext: float
        External radius of core/largest radius in the coil.
    height:    float
        Height of core.
    wire_diam: float
        Diameter of wire used. By default it is set to AWG 42 wire.
    """
    assert (y_c>0),"Minimum y-coordinate must be positive."
    assert (z_c>=radius_ext), "Minimum z-coordinate must be at least equal to external radius."
    assert (radius_ext>radius_int), "External radius must be greater than internal radius."
    nturns = int(height / wire_diam)
    nlayers = int( (radius_ext - radius_int) / wire_diam)
    G_c = np.array([ G_solenoid(y_c, z_c, radius_int + wire_diam*nr, nturns, wire_diam) for nr in range(nlayers) ])
    return G_c.sum(axis=-1)
#
def main():
    y_cs = np.arange(0.1, 3.1, .1) #position of center of first loop
    z_cs = [1.5, 1.7, 2., 2.5, 3.]

    radius_int = 1.0
    radius_ext = 1.5
    height = 0.8

    G_ysep = np.array([[G_coil(y_c, z_c, radius_int, radius_ext,height) for y_c in y_cs ] for z_c in z_cs])

    plt.figure(1)
    plt.clf()
    plt.title('Sensitivity as funciton of $y$-separation')

    for i in range(len(z_cs)):
        plt.plot(y_cs, G_ysep[i]/G_ysep.max(), '.-', label='$z_c =$'+str(z_cs[i]))
    #
    plt.xlabel('$y$ separation')
    plt.ylabel('Normalized Sensitivity')
    plt.legend()
    plt.grid()
    plt.show()

    z_cs = np.arange(1.5, 3.2, .1)
    y_cs = [.1, .5, 1., 1.5, 2.]

    radius_int = 1.0
    radius_ext = 1.5
    height = 0.8

    G_zsep = np.array([[ G_coil( y_c, z_c, radius_int, radius_ext, height ) for z_c in z_cs] for y_c in y_cs])

    plt.figure(2)
    plt.clf()
    plt.title('Sensitivity as funciton of $z$-separation')

    for i in range(len(y_cs)):
        plt.plot(z_cs, G_zsep[i]/G_zsep.max(), '.-', label='$y_c=$'+str(y_cs[i]))
    #
    plt.xlabel('$z$ separation')
    plt.ylabel('Normalized Sensitivity')
    plt.legend()
    plt.grid()
    plt.show()

    y_c = 0.5
    z_c = 1.5
    radia_int = [0.2, .4, .6, .8, 1.0, 1.2, 1.4]
    radia_ext_max = 2.6
    height = 0.8


    G_rint = [[ G_coil(y_c, z_c, r_int, r_ext, height) for r_ext in np.arange(r_int + .1, radia_ext_max, .1)]
                       for r_int in radia_int]

    G_rint_max = 0
    for i in range(len(G_rint)):
        G_rint_max = max(G_rint_max, max(G_rint[i]))

    plt.figure(3)
    plt.clf()
    plt.title('Sensitivity as funciton of $R_{ext}$')

    for i in range(len(radia_int)):
        plt.plot( np.arange(radia_int[i] + .1, radia_ext_max, .1)
                 , np.array(G_rint[i])/G_rint_max
                 , '.-', label='$R_{int}=$'+str(radia_int[i]))
    #
    plt.xlabel('$R_{ext}$')
    plt.ylabel('Normalized Sensitivity')
    plt.legend()
    plt.grid()
    plt.show()

    y_c = 0.5
    z_c = 1.5
    radius_int = 1.0
    radius_ext = 1.5
    heights = np.arange(.1, 1.6, .1)

    G_height = np.array([G_coil(y_c, z_c, radius_int, radius_ext, height) for height in heights])

    plt.figure(4)
    plt.clf()
    plt.title('Sensitivity as funciton of coil height')
    #
    plot(heights, G_height/max(G_height), '.-')
    #
    plt.xlabel('coil height')
    plt.ylabel('Normalized Sensitivity')
    plt.grid()
    plt.show()
#
if __name__ == '__main__':
    main()
