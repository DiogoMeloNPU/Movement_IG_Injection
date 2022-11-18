#this module creates the signals that will be plotted in PlotResults.py

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

'''for i, path in enumerate(FilesDF['velMagnitude.pkl']):
    if isinstance(path, str):
        if int(FilesDF['VideoAqRate'][i][0:2]) == 15 and FilesDF['Reinforcer'][i] == 'SUCROSE':
            velMagnitudeDF = pd.read_pickle(path)
            plt.plot(np.array(velMagnitudeDF['VelMagnitude_tailbase']), linewidth=0.8)
            #sns.kdeplot(np.array(velMagnitudeDF['VelMagnitude_tailbase'])+1, log_scale = True, linewidth=0.8)
            plt.axhline(y=20, color='black', linestyle='-')
            plt.show()

path = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\VTA\\Sucrose\\VTA_M45856_SUCROSE_DAY13_1602022_2022-02-16-163154.mp4"
index = FilesDF.index[FilesDF['VideoPath'] == path].tolist()
velDF = np.array(FilesDF[''])
plt.plot(, linewidth=0.8, color='lightskyblue')
plt.show()'''