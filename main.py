import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.signal import convolve

plt.style.use('dark_background')

class GameOfLife:
    def __init__(self, seed = None, size = 100):
        self.size = size
        self.I = seed if seed else np.round(np.random.random((self.size, self.size)))
        self.kernel = np.array([
                [1, 1, 1],
                [1, 0, 1],
                [1, 1, 1]
            ])
        self.fig = plt.figure()
        self.fig.tight_layout()

    def plt_init(self):
        self.im_obj = plt.imshow(self.I, cmap='gray')
        plt.axis('off')
        return self.im_obj, 

    def plt_update(self, _):
        t = convolve(self.I, self.kernel, mode='same') + 16 * self.I - 8
        self.I = np.where((t == -5)|(t == 10)|(t == 11), 1, 0).reshape(self.I.shape)
        self.im_obj.set_data(self.I)
        plt.draw()
        return self.im_obj, 
    
    def animate(self):
        self.ani = animation.FuncAnimation(self.fig, self.plt_update, init_func=self.plt_init, interval = 10, blit=True)
        plt.show()

if __name__ == '__main__':
    obj = GameOfLife()
    obj.animate()