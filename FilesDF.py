import pandas as pd
import numpy as np
import os

#Create a dataframe containing the paths for the session videos and DLC files

#define the column labels
columns = ['Imaging', 'MiceID', 'Reinforcer', 'SessionDay', 'VideoPath', 'FilteredDLCPath', 'FrameSessionOnset']

#create the df
FilesDF = pd.DataFrame(columns = columns)

#folder containing all files used for training the DLC network
path_files = "C:\\Users\\user\\Desktop\\DLC_postingestiveReinforcers-Diogo-Melo-2022-11-04\\videos"

#Now, fill the dataframe using the files stored in path_files
for path, subdirs, files in os.walk(path_files):
    for name in files:
        if (name.endswith('.mp4') or name.endswith('.avi')) and 'labeled' not in name:
            #use the video name to fill the first columns of the dataframe
            currentRowValues = {'Imaging':name.split('_')[0], 'MiceID':name.split('_')[1], 'Reinforcer':name.split('_')[2], 'SessionDay':name.split('_')[3][3:], 
            'VideoPath':os.path.join(path, name), 'FilteredDLCPath':np.nan, 'FrameSessionOnset':np.nan}
            FilesDF = FilesDF.append(currentRowValues, ignore_index=True)

#Match the path of the filtered DLC predictions to the respective row in the df
for path, subdirs, files in os.walk(path_files):
    for name in files:
        if name.endswith('500000_filtered.csv'):
            #list containing the imaging region (0), the miceID (1), the Reinforcer (2), and the session day (3)
            currentDLCFile = [name.split('_')[0], name.split('_')[1], name.split('_')[2], name.split('_')[3][3:]]
            match = FilesDF.loc[(FilesDF['Imaging'] == currentDLCFile[0]) & (FilesDF['MiceID'] == currentDLCFile[1]) & (FilesDF['Reinforcer'] == currentDLCFile[2]) & (FilesDF['SessionDay'] == currentDLCFile[3])]
            if len(match) == 1:
                FilesDF['FilteredDLCPath'][match.index[0]] = os.path.join(path, name)

#show the df
print(FilesDF)

#save the df in google drive as pkl
path2saveFilesDF = "E:\\My Drive\\MovementIGInjectionFilesDF.pkl"
FilesDF.to_pickle(path2saveFilesDF)

#if you want, you an also save it in other formats (such as csv for easier direct search - not recommended)
#save the df in google drive as csv
#path2saveFilesDF = "E:\\My Drive\\MovementIGInjectionFilesDF.csv"
#FilesDF.to_csv(path2saveFilesDF)
