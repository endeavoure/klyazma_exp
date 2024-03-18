from scipy.io import loadmat
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.fft import ifft, fft, fftfreq, fftshift, ifft2, fft2
from scipy import signal
from scipy.signal import spectrogram
from scipy.io import loadmat, wavfile
from scipy.interpolate import interp2d
from scipy.interpolate import RectBivariateSpline
import pickle
from Klyazma2024 import get_audio, spec_plot, full_process, build_spec, t_plot

NFFT = 5000
upper_edge = 5000
pathx = 'TASCAM_Files/TASCAM_0035S1.wav'
pathy = 'TASCAM_Files/TASCAM_0035S2.wav'
pathz = 'TASCAM_Files/TASCAM_0035S3.wav'
T_beg = [931.75, 960.9, 988.6, 1019.3, 1049.7, 1079.9, 1110.1, 1140.8]
T_end = [932.3, 961.4, 989.3, 1020.0, 1050.3, 1080.5, 1110.7, 1141.5]

data = {'freq': [], 't': [], 'sxx': []}
f, t, sxx = full_process(pathx, T_beg[0], T_end[0], NFFT)
data['freq'] = f

for i in range(len(T_beg)):
    print(f'Удар {i+1} по каналу X')
    f, t, sxx = full_process(pathx, T_beg[i], T_end[i], NFFT)
    data['t'].append(t)
    data['sxx'].append(sxx)

for i in range(len(T_beg)):
    print(f'Удар {i+1} по каналу Y')
    f, t, sxx = full_process(pathy, T_beg[i], T_end[i], NFFT)
    data['t'].append(t)
    data['sxx'].append(sxx)

for i in range(len(T_beg)):
    print(f'Удар {i+1} по каналу Z')
    f, t, sxx = full_process(pathz, T_beg[i], T_end[i], NFFT)
    data['t'].append(t)
    data['sxx'].append(sxx)

with open('saved_dictionary.pkl', 'wb') as f:
    pickle.dump(data, f)