from mysignal import Signal

x = Signal('skip.wav')
noise = Signal('noise.wav')
x.noise_removal(noise)
x.write('denoise.wav')
x.truncate_silence(100)
x.write('trunc.wav')