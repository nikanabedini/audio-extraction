import librosa as librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
%matplotlib inline
import librosa.display
from IPython.display import Audio
import pandas as pd
import os
from sklearn.model_selection import train_test_split
import skimage.io

y, sr = librosa.load("/content/daily_download_20210730_128.mp3", sr=32000)
librosa.display.waveshow(y,max_points=11025 , x_axis='s')