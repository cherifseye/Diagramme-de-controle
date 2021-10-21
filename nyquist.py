import numpy as np
import matplotlib.pyplot as plt
from sympy import *


def transfer(num, den, w):
    
    if isinstance(num, int) and isinstance(den, int):
        num = num
        den = den
    if isinstance(num, int) and isinstance(den, list):
        s = symbols('s')
        den_ = 0

        for i, j in enumerate(reversed(den)):
            den_ += j * s ** i

            den = den_
        num = num
    if isinstance(num, list) and isinstance(den, list):
        s = symbols('s')
        den_ = 0
        num_ = 0
        for i, j in enumerate(reversed(den)):
            den_ += j * s ** i

            den = den_

        for k, l in enumerate(reversed(num)):
            num_ += l * s ** k

            num = num_

    if isinstance(num, list) and isinstance(den, int):
        s = symbols('s')
        num_ = 0

        for i, j in enumerate(reversed(num)):
            num_ += j * s ** i

            num = num_
        den = den

    G = simplify(num / den)
    tf = lambdify(s, G, 'numpy')
    jw = 1j * np.arange(0, 30)
    tf_ = tf(jw)
    print(tf_)
    real = [r.real for r in tf_]
    imag = [i.imag for i in tf_]
    plt.plot(real, imag)
    plt.gca().spines['top'].set_color('none')
    # plt.gca().spines['bottom'].set_position('zero')
    plt.gca().spines['right'].set_color('none')
    # plt.gca().spines['left'].set_position('zero')

    plt.text(max(real) + .05, min(imag) - 0.02, r'Real', fontsize=10)
    plt.text(0, max(imag) + 0.03, r'Imaginary', fontsize=10)

    tf_w = lambdify(s, G)
    tf__ = tf_w(w * 1j)
    rw = [tf__.real]
    iw = [tf__.imag]
    plt.text(tf__.real, tf__.imag + 0.02, r'w', fontsize=10)
    plt.scatter(rw, iw)

    plt.show()


if __name__ == '__main__':
    print(transfer(5, 5, 10))
