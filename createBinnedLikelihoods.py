#this module is temporary and should be implemented as part of the createBinnedData.py to avoid code repetition
#this module is designed to bin the data from the velocity dataframes

#the resulting files (.npy's containing the binned likelihoods) will be used for the final plot

import numpy as np
import pandas as pd

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#create a file pattern for each type of new file (catheter.npy)
file_pattern_catheter = 'BinnedCatheterLikelihood_'
file_type = '.npy'

#create two arrays, to save the paths of the binned data files
BinnedCatheterLikelihoodPaths = []

#session duration in seconds
session_duration_plot = 900
#number of data points to plot
numBins = session_duration_plot/10

for i, path in enumerate(FilesDF['velMagnitude.pkl']):
    if isinstance(path, str):
        #read the current file containing the velocities and the prediction likelihoods of one session
        df_velMag = pd.read_pickle(path)
        CatheterLikelihood = np.array(df_velMag['catheter_likelihood'])
        #bin the data accoddingly (notice that 15 Hz and 10 Hz videos will have a different number of data points per bin)
        #...for this I will reshape the array in smaller arrays (the same ammount as numBins) and take only the average of the smaller arrays
        #...as the value to assign to the bin
        reshaped_CatheterLikelihood = np.reshape(
            CatheterLikelihood, (int(numBins), int(len(CatheterLikelihood)/numBins)))
        BinnedCatheterLikelihood = [round(np.mean(reshaped_CatheterLikelihood[row, :]), 2)
                             for row in range(reshaped_CatheterLikelihood.shape[0])]
        #create the paths to save the new files as .npy
        temp_path_catheter = FilesDF['FilteredDLCPath'].iloc[i].split('\\')[
            :-1]
        temp_path_catheter.append(
            file_pattern_catheter+path.split('\\')[-1][26:-4]+file_type)
        path2save_binnedCatheterLikelihood = '\\'.join(temp_path_catheter)
        #save the .npy files containing the binned likelihoods in the respective paths
        print('The binned likelihood of the CATHETER in the current session was saved in: {}'.format(
            path2save_binnedCatheterLikelihood))
        np.save(path2save_binnedCatheterLikelihood, BinnedCatheterLikelihood)
        BinnedCatheterLikelihoodPaths.append(path2save_binnedCatheterLikelihood)
        print('\n')
    else:
        BinnedCatheterLikelihoodPaths.append(-1)

#create a new column in FilesDF to save the paths of the binned catheter likelihoods
FilesDF['binnedCatheterLikelihood.npy'] = BinnedCatheterLikelihoodPaths

#show the df
print(FilesDF)

#save the df as a pkl file in google drive - this will overwrite the MovementIGInjectionFilesDF.pkl file
path2saveDF = FilesDFpath
FilesDF.to_pickle(path2saveDF)
print('\n\nThe MovementIGinjectionFilesDF.pkl file was updated.')
