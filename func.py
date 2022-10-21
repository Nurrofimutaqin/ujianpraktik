import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout, LeakyReLU
# from keras.regularizers import l2
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import cv2
import random
import os

from tensorflow.keras.layers import Input, Dense, Flatten, GlobalAveragePooling2D
from tensorflow.keras.models import Sequential

def make_model():
    xception = tf.keras.applications.Xception(input_shape=(100 , 100, 3),
                                           include_top=False,
                                           weights='imagenet')

    model = Sequential()
    model.add(xception)
    model.add(GlobalAveragePooling2D())
    model.add(Flatten())
    model.add(Dense(2048, activation="relu"))
    model.add(Dense(1024, activation="relu"))
    model.add(Dense(512, activation="relu"))
    model.add(Dense(10, activation="softmax" , name="classification"))


    return model