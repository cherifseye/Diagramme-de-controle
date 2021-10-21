import magnitude as magnitude
import numpy as np
import matplotlib.pyplot as plt
from sympy import *


class Diagram():

    def __init__(self, fonction_transfert, frequence=np.logspace(-2, 3, 1000)):
        self.tf = fonction_transfert
        self.w = frequence

    def magnitude(self):
        return 20 * np.log(np.absolute(self.tf))

    def phase(self):
        return np.angle(self.tf, 'deg')

    def Nyquist(self, num, den, w):
        if isinstance(num, int) and isinstance(den, int):
            numerator = num
            denominator = den
        if isinstance(num, int) and isinstance(den, list):
            s = symbols('s')
            den_ = 0

            for i, j in enumerate(reversed(den)):
                den_ += j * s ** i

                denominator = den_
            numerator = num
        if isinstance(num, list) and isinstance(den, list):
            s = symbols('s')
            den_ = 0
            num_ = 0
            for i, j in enumerate(reversed(den)):
                den_ += j * s ** i

                denominator = den_

            for k, l in enumerate(reversed(num)):
                num_ += l * s ** k

                numerator = num_

        if isinstance(num, list) and isinstance(den, int):
            s = symbols('s')
            num_ = 0

            for i, j in enumerate(reversed(num)):
                num_ += j * s ** i

                numerator = num_
            denominator = den

        G = simplify(numerator / denominator)
        s = symbols('s')
        transfer_value = lambdify(s, G, 'numpy')
        jw = 1j * np.linspace(0, 30, 300)
        transfer_values = transfer_value(jw)
        # print(transfer_values)
        reals = [r.real for r in transfer_values]
        imag = [i.imag for i in transfer_values]
        plt.plot(reals, imag)
        plt.gca().spines['top'].set_color('none')
        # plt.gca().spines['bottom'].set_position('zero')
        plt.gca().spines['right'].set_color('none')
        # plt.gca().spines['left'].set_position('zero')

        plt.text(max(reals) + .05, min(imag) - 0.02, r'Real', fontsize=10)
        plt.text(min(reals) - 0.02, max(imag) + 0.03, r'Imaginary', fontsize=10)

        tf_w = lambdify(s, G)
        tf__ = tf_w(w * 1j)
        rw = [tf__.real]
        iw = [tf__.imag]
        plt.text(tf__.real, tf__.imag + 0.02, r'w', fontsize=10)
        plt.scatter(rw, iw)

        plt.show()

    def bode(self):
        if isinstance(self.tf, int):
            if self.tf < 0: 
                fig, (ax1, ax2) = plt.subplots(2, 1)
                ax1.hlines(self.magnitude(), 1, 1000)
                ax1.set_xscale('log')
                ax2.hlines(-np.pi, 1, 1000)
                ax2.set_xscale('log')
                plt.xlabel('Frequency[Hz]')
                ax1.set(ylabel='Amplitude[dB]')
                ax2.set(ylabel='Phase[deg]')
                ax1.grid(True)
                ax2.grid(True)
                plt.show()
                

            else:
                fig, (ax1, ax2) = plt.subplots(2, 1)
            
                ax1.hlines(self.magnitude(), 1, 1000)
                ax1.set_xscale('log')
                ax2.hlines(0, 1, 1000)
                ax2.set_xscale('log')
                plt.xlabel('Frequency[Hz]')
                ax1.set(ylabel='Amplitude[dB]')
                ax2.set(ylabel='Phase[deg]')
                ax1.grid(True)
                ax2.grid(True)
                plt.show()
                
            
        else:
            fig, (ax1, ax2) = plt.subplots(2, 1)
            ax1.semilogx(self.w, self.magnitude())
            ax2.semilogx(self.w, self.phase())
            # ax2.set_ylim(-90, 10)
            ax2.grid(True)
            # ax1.set_ylim(-70, -20)
            ax1.set(ylabel='Amplitude[dB]')
            ax2.set(ylabel='Phase[deg]')
            ax1.grid(True)
            ax2.grid(True)
            plt.xlabel('Frequency[Hz]')

            plt.show()

    def black(self):
        plt.gca().spines['top'].set_color('none')
        plt.gca().spines['top'].set_position
        # plt.gca().spines['bottom'].set_position('zero')
        # plt.gca().spines['left'].set_position('zero')
        plt.gca().spines['right'].set_color('none')
        plt.plot(self.phase(), self.magnitude())
        plt.xlim(-100, 10)
        plt.ylim(-70, -10)
        plt.xlabel('Phase[]')
        plt.ylabel(' Amplitude[dB]')
        plt.show()