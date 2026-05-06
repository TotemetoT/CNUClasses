import matplotlib.pyplot as plt
import numpy as np
import os

class Params:
    def __init__(self, A=0, a=0, b=0, color="blue"):
        self.A = A
        self.a = a
        self.b = b
        self.color = color
    def set_parameters(self, A=None, a=None, b=None, color=None):
        if A is not None: self.A = A
        if a is not None: self.a = a
        if b is not None: self.b = b
        if color is not None: self.color = color

class ButterflyCurve(Params):
    def __init__(self, A=0, a=0, b=0, color="blue"):
        super().__init__(A, a, b, color)
        self.t = np.linspace(0, 8 * np.pi, 1000)
    def plot_curve(self):
        t = self.t
        x = np.sin(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)
        y = np.cos(t) * (np.exp(np.cos(t)) - 2 * np.cos(4 * t) - np.sin(t / 12) ** 5)

        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)

        ax.plot(x, y, self.color, label=f'a={self.a}, b={self.b}')
        ax.set_xlabel("x-Axis")
        ax.set_ylabel("y-Axis")
        ax.set_title("Butterfly Curve - Ryan.Schatzberg.24")
        ax.grid(True)
        ax.set_aspect('equal')
        ax.legend(title="Ryan.Schatzberg.24")

        path = os.path.join("data", "Butterfly.png")
        fig.savefig(path)
        # Showing
        plt.show()


class VivianiCurve(Params):
    def __init__(self, A=0, a=0, b=0, color="blue"):
        super().__init__(A, a, b, color)
        self.t = np.linspace(0, 8 * np.pi, 1000)
    def plot_curve(self):
        t = self.t
        x = self.a * (1 + np.cos(t))
        y = self.a * np.sin(t)
        z = 2*self.a * np.sin(t/2)

        fig = plt.figure()
        ax = fig.add_subplot(projection='3d')

        ax.plot(x, y, z, self.color, label=f'a={self.a}, b={self.b}')
        ax.set_xlabel("x-Axis")
        ax.set_ylabel("y-Axis")
        ax.set_zlabel("z-Axis")
        ax.set_title("Viviani's Curve - Ryan.Schatzberg.24")
        ax.grid(True)
        ax.set_aspect('equal')
        ax.legend()

        path = os.path.join("data", "Viviani.png")
        fig.savefig(path)
        # Showing
        plt.show()


curve = VivianiCurve(A=2, a=1, b=1, color="purple")
curve.plot_curve()

