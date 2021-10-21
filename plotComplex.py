import matplotlib.pyplot as plt
import math
import cmath


def plotComplex(z, xmin, xmax, ymin, ymax):

    x = [0.0, 0.0]
    y = [z.real, z.imag]
    #set the axes
    plt.gca().spines['top'].set_color('none')
    plt.gca().spines['bottom'].set_position('zero')
    plt.gca().spines['left'].set_position('zero')
    plt.gca().spines['right'].set_color('none')
    dx = y[0] - x[0] # x coordinate
    dy = y[1] - x[1] # y coordinate
    head_length = 0.2 #length of the arrow
    mag = math.sqrt(dx**2 + dy**2) # the magnitude of Z
    dx = dx / mag
    dy = dy / mag
    mag = mag - head_length
    arg = cmath.phase(z)
    arg = round(arg, 2)
    arg = str(arg)
    plt.arrow(x[0], x[1], dx*mag, dy*mag, head_width=head_length,
              head_length=head_length, fc='black', ec='black')
    plt.text(y[0]+0.3, y[1], r'Z', fontsize=10)
    plt.text(xmax+.5, 0, r'Real', fontsize=10)
    plt.text(0, ymax+0.5, r'Imaginary', fontsize=10)
    plt.xlim(xmin, xmax)
    plt.ylim(ymin, ymax)
    plt.grid(True, linestyle='--')
    plt.text(0.9, 0.2, r'$\theta$ = ' + arg)
    plt.show()


if __name__ == '__main__':
    plotComplex(2+2*1j, -5, 5, -5, 5)

