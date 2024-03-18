from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
from scipy.fft import ifft, fft, fftfreq, fftshift, ifft2, fft2
from scipy import signal
from scipy.signal import spectrogram
from scipy.io import loadmat, wavfile
from scipy.interpolate import interp2d
from scipy.interpolate import RectBivariateSpline


def get_audio(path, T_beg, T_end):

    sample_rate, audio_data = wavfile.read(path)

    t = np.arange(len(audio_data))/sample_rate

    nt = (t > T_beg) & (t < T_end)
    t1 = t[nt]
    t1 = t1 - T_beg
    t2 = np.zeros(len(t))
    audio_data1 = audio_data[nt]

    return audio_data1, sample_rate


def spec_plot(audio_data, sample_rate, NFFT):
    f, t, sxx = spectrogram(audio_data, fs=sample_rate, nfft=NFFT, nperseg=int(NFFT//16))
    return f, t, sxx

def full_process(path, T_beg, T_end, NFFT):

    audio_data, sample_rate = get_audio(path, T_beg, T_end)
    f, t, sxx = spec_plot(audio_data, sample_rate, NFFT)
    
    plt.figure(figsize=(15,8))
    plt.colormaps["plasma"]
    plt.pcolormesh(t, f, sxx, shading='auto', vmax = 1)
    plt.ylabel('Frequency [Hz]')
    plt.xlabel('Time [sec]')
    plt.ylim([0, 3000])
    plt.show()
    
    return f, t, sxx
