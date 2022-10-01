#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#labdaOrbit - by lambdaCard
def noaaResample(name:str):
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
    plt.savefig(filename)
    return filename
def noaa(name:str):
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
    for i in range(1, w):
        for j in range(1, 4*h):
            pixVal = image.getpixel((i, j))
            if pixVal != (255, 255, 255):
               imgpix.append([i, j])
    print(imgpix)
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.savefig(filename)
    return filename
def img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]):
    """
    img2asciiart(img,size = 15,intensity = 255,replaceItem = 0,items = ["@"," "]) ,return a  matrix img as str
    """
    import cv2
    from numpy import asarray 
    dataFile = cv2.imread(img,cv2.IMREAD_GRAYSCALE)
    imgresized  = dataFile #cv2.resize(dataFile , (size, size))
    imgstr = ""
    #imgstr = asarray(imgresized , dtype= str)
    for count in range(len(imgresized)):
        for cont in range(len(imgresized[count]))  :
                if imgresized[count,cont]//intensity == replaceItem:
                    #imgstr[count,cont]= items[0]
                    imgstr += items[0]
                else:
                    #imgstr[count,cont] = items[1]
                    imgstr += items[1]
        imgstr += "\n"
    outfig = [imgresized,imgstr]
    np.set_printoptions(threshold=sys.maxsize)
    print(imgresized)
    return outfig 
def main():
    img2asciiart("1.png",size = 500,intensity = 255,replaceItem = 0,items = ["@"," "])
main()