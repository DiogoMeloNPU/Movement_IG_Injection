#this module is designed to bin the data from the velocity dataframes
#the resulting files (.npy's containing the binned velocities) will be used for the final plot

import numpy as np
import pandas as pd

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#create a file pattern for each type of new file (catheter and tailbase.npy)
file_pattern_catheter = 'BinnedCatheterVel_csv_'
file_pattern_tailbase = 'BinnedTailbaseVel_csv_'
file_type = '.csv'

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
        catheterVel, tailbaseVel = np.array(df_velMag['VelMagnitude_catheter']), np.array(
            df_velMag['VelMagnitude_tailbase'])
        #bin the data accoddingly (notice that 15 Hz and 10 Hz videos will have a different number of data points per bin)
        #...for this I will reshape the array in smaller arrays (the same ammount as numBins) and take only the average of the smaller arrays
        #...as the value to assign to the bin
        reshaped_CatheterVel = np.reshape(
            catheterVel, (int(numBins), int(len(catheterVel)/numBins)))
        reshaped_TailbaseVel = np.reshape(
            tailbaseVel, (int(numBins), int(len(tailbaseVel)/numBins)))
        binnedCatheterVel = [round(np.mean(reshaped_CatheterVel[row, :]), 2)
                             for row in range(reshaped_CatheterVel.shape[0])]
        binnedTailbaseVel = [round(np.mean(reshaped_TailbaseVel[row, :]), 2)
                             for row in range(reshaped_TailbaseVel.shape[0])]
        #create the paths to save the new files as .npy
        temp_path_catheter = FilesDF['FilteredDLCPath'].iloc[i].split('\\')[
            :-1]
        temp_path_tailbase = FilesDF['FilteredDLCPath'].iloc[i].split('\\')[
            :-1]
        temp_path_catheter.append(
            file_pattern_catheter+path.split('\\')[-1][26:-4]+file_type)
        temp_path_tailbase.append(
            file_pattern_tailbase+path.split('\\')[-1][26:-4]+file_type)
        path2save_binnedCatheterVel = '\\'.join(temp_path_catheter)
        path2save_binnedTailbaseVel = '\\'.join(temp_path_tailbase)
        #save the .npy files containing the binned velocity signals in the respective paths
        print('CSV - The binned velocity of the CATHETER in the current session was saved in: {}'.format(
            path2save_binnedCatheterVel))
        #np.save(path2save_binnedCatheterVel, binnedCatheterVel)
        df_cat = pd.DataFrame(binnedCatheterVel)
        df_cat.to_csv(path2save_binnedCatheterVel, index=False) #new line
        BinnedCatheterVelPaths.append(path2save_binnedCatheterVel)
        print('CSV - The binned velocity of the TAILBASE in the current session was saved in: {}'.format(
            path2save_binnedTailbaseVel))
        #np.save(path2save_binnedTailbaseVel, binnedTailbaseVel)
        df_tb = pd.DataFrame(binnedTailbaseVel)
        df_tb.to_csv(path2save_binnedTailbaseVel, index=False)
        BinnedTailbaseVelPaths.append(path2save_binnedTailbaseVel)
        print('\n')
    else:
        BinnedCatheterVelPaths.append(-1)
        BinnedTailbaseVelPaths.append(-1)
