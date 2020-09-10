#3245
import sys
sys.path.insert(1,'dsp-modulo')

from thinkdsp import SinSignal
from thinkdsp import decorate

from thinkdsp import read_wave
from thinkdsp import play_wave

import matplotlib.pyplot as plt


frecuencia697 = SinSignal(freq=697, amp=1, offset=0)
frecuencia1477 = SinSignal(freq=1477, amp=1, offset=0)
frecuencia1336 = SinSignal(freq=1336, amp=1, offset=0)
frecuencia1209 = SinSignal(freq=1209, amp=1, offset=0)
frecuencia770 = SinSignal(freq=770, amp=1, offset=0)

wave_697_3 = frecuencia697.make_wave(duration=0.5, start=0, framerate=44100)
wave_1477_3 = frecuencia1477.make_wave(duration=0.5, start=0, framerate=44100)

wave_697_2 = frecuencia697.make_wave(duration=0.5, start=0.5, framerate=44100)
wave_1336_2 = frecuencia1336.make_wave(duration=0.5, start=0.5, framerate=44100)

wave_770_4 = frecuencia770.make_wave(duration=0.5, start=1, framerate=44100)
wave_1209_4 = frecuencia1209.make_wave(duration=0.5, start=1, framerate=44100)

wave_770_5 = frecuencia770.make_wave(duration=0.5, start=1.5, framerate=44100)
wave_1336_5 = frecuencia1336.make_wave(duration=0.5, start=1.5, framerate=44100)

wave_sonido_3 = wave_697_3 + wave_1477_3
wave_sonido_2 = wave_697_2 + wave_1336_2
wave_sonido_4 = wave_770_4 + wave_1209_4
wave_sonido_5 = wave_770_5 + wave_1336_5

wave_numero = wave_sonido_3 + wave_sonido_2 + wave_sonido_4 + wave_sonido_5

decorate(xlabel="Tiempo(s)")
decorate(ylabel="amplitud")

wave_numero.plot()
wave_numero.write("3245.wav")
plt.show()