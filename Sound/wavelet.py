import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

class FourierMorlet:
    """En Morlet-wavelet evaluert i frekvensdomenet."""

    def __init__(self, k):
        self.k = k

    def __call__(self, omega, omegaa):
        return 2 * (np.exp(-np.power(self.k * (omega - omegaa) / omegaa, 2)) -
                    np.exp(-np.power(self.k, 2)) *
                    np.exp(-np.power(self.k * omega / omegaa, 2)))


def wavelet_transform(t, signal, omega_range, wavelet=FourierMorlet(6)):
    fft_signal = np.fft.fft(signal)
    fft_omegas = np.fft.fftfreq(len(signal), t[1] - t[0]) * 2 * np.pi
    transformed_signals = []
    for omega in omega_range:
        transformed_signals.append(
            np.fft.ifft(wavelet(fft_omegas, omega) * fft_signal))
    return np.asarray(transformed_signals)




if __name__ == "__main__":
    N = 8192  # nr of time-points.
    n = 50  # nr of frequencies.
    Fs = 10e3
    T = N / Fs
    f1 = 1000
    f2 = 1600
    c1 = 1.0
    c2 = 1.7
    t = np.linspace(0, T, N)
    dt = t[1] - t[0]
    t1 = 0.15
    t2 = 0.5
    sigma1 = 0.01
    sigma2 = 0.05
    y = c1 * np.sin(2 * np.pi * f1 * t) * \
        np.exp(-np.power((t - t1) / sigma1, 2)) + \
        c2 * np.sin(2 * np.pi * f2 * t) * \
        np.exp(-np.power((t - t2) / sigma2, 2))
    y = y + np.random.uniform(0, 3, N)

    omegas = np.logspace(np.log10(800), np.log10(2000), n) * 2 * np.pi
    wavelet = np.abs(wavelet_transform(t, y, omegas, FourierMorlet(24)))
    # plt.pcolormesh(t, omegas / 2.0 / np.pi, np.absolute(waveletDiagram))
    # plt.colorbar()
    # plt.tight_layout()
    # plt.show()

    data = np.zeros((n, N))
    def update_data(current_index, time_index_span):
        data[:, current_index:current_index+time_index_span] = wavelet[:, current_index:current_index+time_index_span]


    fig,ax = plt.subplots()
    time_index_span = 1000
    time_index_interval = 100
    def animate(i):
        current_index = i*time_index_interval
        update_data(current_index, time_index_span)
        ax.clear()
        ax.pcolormesh(data[:,current_index:current_index+time_index_span])
        ax.set_title('%03d'%(i))
        return ax

    frames = (N - time_index_span)//time_index_interval
    print(frames)
    interval = 1
    ani = animation.FuncAnimation(fig,animate,frames,interval=interval,blit=False)

    plt.show()