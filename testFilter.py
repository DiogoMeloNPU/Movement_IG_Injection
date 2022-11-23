#this module is meant for displaying, for all sessions, the effects of the filter applied on the signals

path = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\SNc\\Corn_oil\\M43802_14092021_COIL_14092021DLC_resnet50_DLC_postingestiveReinforcersNov4shuffle1_500000.csv"
path_filtered = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\SNc\\Corn_oil\\M43802_14092021_COIL_14092021DLC_resnet50_DLC_postingestiveReinforcersNov4shuffle1_500000_filtered.csv"

import pandas as pd
import numpy as np
from organizeDF_DLCcoordinates import buildDLCpredictionsDF
import matplotlib.pyplot as plt

organized_DLC = buildDLCpredictionsDF(path)
organized_filteredDLC = buildDLCpredictionsDF(path_filtered)


#IMPLEMENT LOOP TO CHECK THE EFFECT OF THE FILTER IN ALL THE SESSIONS
#REBUILD THIS NOT TO REPEAT THE PROCESS OF PRODUCING ORGANIZED DLC DATAFRAMES
plt.subplot(1,2,1)
plt.plot(organized_DLC['tailbase (x)'])
plt.plot(organized_filteredDLC['tailbase (x)'])
plt.title('tailbase (x)')
plt.subplot(1,2,2)
plt.plot(organized_DLC['tailbase (y)'])
plt.plot(organized_filteredDLC['tailbase (y)'])
plt.title('tailbase (y)')
plt.show()