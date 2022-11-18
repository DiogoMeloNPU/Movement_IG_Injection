#this module is designed to bin the data from the velocity dataframes
#the resulting files (.npy's containing the binned velocities) will be used for the final plot

import numpy as np
import pandas as pd

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#create a file pattern for each type of new file (catheter and tailbase.npy)
file_pattern_catheter = 'BinnedCatheterVel_'
file_pattern_tailbase = 'BinnedTailbaseVel_'
file_type = '.npy'

#create two arrays, to save the paths of the binned data files
BinnedCatheterVelPaths = []
BinnedTailbaseVelPaths = []

#session duration in seconds
session_duration_plot = 900
#number of data points to plot
numBins = session_duration_plot/10

for i, path in enumerate(FilesDF['velMagnitude.pkl']):
    if isinstance(path, str):
        #read the current file containing the velocities and the prediction likelihoods of one session
        df_velMag = pd.read_pickle(path)
        catheterVel, tailbaseVel = df_velMag['VelMagnitude_catheter'], df_velMag['VelMagnitude_tailbase']
        #bin the data accoddingly (notice that 15 Hz and 10 Hz videos will have a different number of data points per bin)
        #...for this I will reshape the 
        binnedCatheterVel = 
        binnedTailbaseVel = 
        #create the paths to save the new files as .npy
        temp_path = FilesDF['DLC_predictions.csv'].iloc[i].split('\\')[:-1]
        temp_path_catheter.append(file_pattern_catheter+path.split('\\')[-1][:-4]+file_type)
        temp_path_tailbase.append(file_pattern_tailbase+path.split('\\')[-1][:-4]+file_type)
        path2save_binnedCatheterVel = '\\'.join(temp_path_catheter)
        path2save_binnedTailbaseVel = '\\'.join(temp_path_tailbase)
        #save the .npy files containing the binned velocity signals in the respective paths
        np.save(path2save_binnedCatheterVel, binnedCatheterVel)
        np.save(path2save_binnedTailbaseVel, binnedTailbaseVel)