#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#labdaOrbit - by lambdaCard
def noaaResample(name:str,directory=""):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform,resampled is better cuality, sometimes audio not was resample
    """
    import scipy.io.wavfile as wav
    import scipy.signal as signal
    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt
    import datetime
    fs, data = wav.read(name)  
    data_crop = data[20*fs:21*fs]
    analytical_signal = signal.hilbert(data)
    data_am = np.abs(analytical_signal)
    frame_width = int(0.5*fs)
    w, h = frame_width, data_am.shape[0]//frame_width
    image = Image.new('RGB', (w, h))
    px, py = 0, 0
    for p in range(data_am.shape[0]):
        lum = int(data_am[p]//32 - 32)
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py), (0, lum, 0))
        px += 1
        if px >= w:
            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, 4*h))
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.savefig(directory+filename)
    return filename
def noaa(name:str,directory=""):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform
    """
    import scipy.io.wavfile as wav
    import scipy.signal as signal
    import numpy as np
    from PIL import Image
    import matplotlib.pyplot as plt
    import datetime
    imgpix=[]
    fs, data = wav.read(name)  
    data_crop = data[20*fs:21*fs]
    resample = 4
    data = data[::resample]
    fs = fs//resample
    analytical_signal = signal.hilbert(data)
    data_am = np.abs(analytical_signal)
    frame_width = int(0.5*fs)
    w, h = frame_width, data_am.shape[0]//frame_width
    image = Image.new('RGB', (w, h))
    px, py = 0, 0
    for p in range(data_am.shape[0]):
        lum = int(data_am[p]//32 - 32)
        if lum < 0: lum = 0
        if lum > 255: lum = 255
        image.putpixel((px, py), (0, lum, 0))
        px += 1
        if px >= w:
            px = 0
            py += 1
            if py >= h:
                break
    image = image.resize((w, 4*h))

    #print(imgpix)
    #image=ImageOps.grayscale(image)
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.savefig(directory+filename)
    return filename
