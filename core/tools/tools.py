#!/usr/bin/env python
# -*- coding: utf-8 -*-"
#labdaOrbit - by lambdaCard
from PIL import Image,ImageOps
import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpi
import datetime
def noaaResample(name:str,pathwav="",directoryimg=""):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform,resampled is better cuality, sometimes audio not was resample
    """
    fs, data = wav.read(pathwav+name)  
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
    plt.imsave(directoryimg+filename,image)
    return filename,image
def noaa(name:str,pathwav="",directoryimg=""):
    """
    noaaResample(name:str)->imagefilename 
    with a wav file obteined of noaas satelite generate a png file using hilbert transform
    """
    imgpix=[]
    fs, data = wav.read(pathwav+name)  
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
    image = image.resize((w, h))
    #print(imgpix)
    image=ImageOps.grayscale(image)
    plt.imshow(image)
    filename=name.replace(".wav",".png")
    plt.imsave(directoryimg+filename,image)
    return filename,image
def imgload(file):
    datos = mpi.imread(file)
    return datos
def grayScale(imagen):
    height = imagen.shape[0]
    width = imagen.shape[1]
    img = np.zeros((height,width,3),dtype=int)
    for i in range(height):
        for j in range(width):
            elemento1 = imagen[i][j][0]
            elemento2 = imagen[i][j][1]
            elemento3 = imagen[i][j][2]
            prom = elemento1+elemento2+elemento3/imagen.shape[2]
            for k in range(3):
                img[i][j][k] = prom*100
    return img
def save(path,image):
    #print(type(path),type(image),path,image)
    img=Image.fromarray(image)
    img.save(path)
    #plt.savefig(path,image)
def genMap():
    import folium
    m = folium.Map(location=[6.256405968932449, -75.59835591123756])
    folium.Marker([6.176375,-75.5600386], popup="<i>Node 0</i>", tooltip="Node 0").add_to(m)
    m.save("index.html")
