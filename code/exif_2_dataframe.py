#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
import cv2
import os
from PIL import Image as Pil_Img
from PIL.ExifTags import TAGS
from IPython.display import Image

def get_exif(fn):
    '''
    Extracts EXIF data from image
    
    Args:
        fn: image filename
        
    Returns:
        ret: EXIF data
    '''
    
    ret = {}
    i = Pil_Img.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return(ret)
    

def EXIF_2df(file_path):
    '''
    Creates dataframe of EXIF data from image directory and saves in csv format
    
    Args:
        file_path: path to image directory
    
    Returns:
        df: dataframe of selected EXIF data from images
    '''
    
    path = file_path
    exif_pics = dict()
    
    # list of exif attributes for dataframe:
    exif_list = ['Make', 'Model', 'DateTime', 'Flash', 'LightSource']
    
    # initialize counter:
    no_exif = 0
    
    for idx, photo in enumerate(os.listdir(path)):
        fname = path + photo
        try:
            pic = get_exif(fname)
            exif_pics[idx] = {k: pic[k] for k in exif_list if k in pic}
        except:
            no_exif += 1
            
    # build dataframe:
    df = pd.DataFrame(exif_pics)
    df = df.T
    df = df.reset_index(drop = True)
    df = df.dropna(subset = ['DateTime'])
    df.to_csv(path_or_buf = './df_exif.csv')
    return(df)

    