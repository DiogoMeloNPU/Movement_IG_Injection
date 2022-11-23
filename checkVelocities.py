#this module allows you to check the velocities that were obtained using DLC filtered coordinates during a complete session (not binned)

import numpy as np
import pandas as pd
import scipy.stats as st
import matplotlib.pyplot as plt
import seaborn as sns

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#check catheter velocities
for session in FilesDF['velMagnitude.pkl']:
    if isinstance(session, str):
        df = pd.read_pickle(session)
        if not df.isnull().values.any():
            #sns.kdeplot(df['catheter_likelihood'], log_scale = True)
            plt.plot(df['catheter_likelihood'])
            #plt.suptitle('_'.join(session.split('\\')[-1].split('_')[1:5]))
    plt.show()