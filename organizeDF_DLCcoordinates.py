#this module organizes every file containing the DLC predictions for easier manipulation of the data as a pandas dataframe
#it also stores each new file in the respective folder containing all other files (neuron.mat, simpler_neuron.mat, AccelData.csv,
# FrameDiff.csv, VideoProcessed.csv)
#finally it updates the MovementIGInjectionFilesDF.pkl with a new column with the paths for the files created here

from os import walk
import pandas as pd
import numpy as np
import os

def buildDLCpredictionsDF(path_predictions_DLC):
    '''
    This function organizes the csv file contanining the DLC predictions for bodypart coordinates 
    (as well as label likelihood) into a more structured and easier to manipulate dataframe.
    '''
    df_DLC = pd.read_csv(path_predictions_DLC)
    df_DLC = df_DLC.drop(columns='scorer')
    df_DLC.iloc[0] + ' ' + '(' + df_DLC.iloc[1] + ')'
    df_DLC.iloc[0] = df_DLC.iloc[0] + ' ' + '(' + df_DLC.iloc[1] + ')'
    df_DLC.drop(index=1)
    df_DLC.columns = df_DLC.iloc[0]
    df_DLC = df_DLC.drop(index=0)
    df_DLC = df_DLC.drop(index=1)
    df_DLC.reset_index(inplace=True, drop=True)
    df_DLC.rename_axis('Index', axis='columns', inplace=True)
    for column in df_DLC.columns:
        df_DLC[column] = pd.to_numeric(df_DLC[column])

    return df_DLC  # dataframe with the DLC predictions

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#create an array to store the file paths of the DLC predictions files
DLCpredictionsPaths = []
#check which DLC analysis files exist and store the file paths in a separate column in FilesDF
for i, path in enumerate(FilesDF['VideoPath']):
    videoName = path[:-4]
    #change this file pattern to use the filtered predictions
    filePatternDLC = 'DLC_resnet50_DLC_postingestiveReinforcersNov4shuffle1_500000_filtered.csv'
    file2search4 = videoName+filePatternDLC
    if os.path.exists(file2search4):
        DLCpredictionsPaths.append(file2search4)
    else:
        #append -1 which is easier to search for and indicates a missingfile
        DLCpredictionsPaths.append(-1)

print(DLCpredictionsPaths, len(DLCpredictionsPaths))

#use the DLCpredictionsPath to fill a new df column
FilesDF['DLC_predictions.csv'] = DLCpredictionsPaths

print(FilesDF)

#create an array to save the paths of the new OrganizedDLC files
OrganizedDLCpaths = []
#create a file pattern to name the new files
file_pattern = 'OrganizedDLC_'
#create a new file with an organized dataframe of DLC predictions for all prediction files
for row, DLCpredictionFile in enumerate(FilesDF['DLC_predictions.csv']):
    if isinstance(DLCpredictionFile, str):
        print('\n\n----Organize the following file and display the new dataframe----: {}'.format(DLCpredictionFile))
        organized_DLC_predictionsDF = buildDLCpredictionsDF(DLCpredictionFile)
        #create the path of the new file
        temp_path = FilesDF['DLC_predictions.csv'].iloc[row].split('\\')[:-1]
        file_type = '.pkl'
        temp_path.append(file_pattern+DLCpredictionFile.split('\\')[-1][:-4]+file_type)
        #same path as the other files, not the path of the original DLC file (which was in a separate folder)
        path2save_organizedDLC_DF = '\\'.join(temp_path)
        print('A new file was created in the following folder: {}'.format(path2save_organizedDLC_DF))
        organized_DLC_predictionsDF.to_pickle(path2save_organizedDLC_DF)
        OrganizedDLCpaths.append(path2save_organizedDLC_DF)
    else:
        OrganizedDLCpaths.append(-1)

#create a new column in FilesDF to save the paths of the new organized files
FilesDF['Organized_DLC_predictions.pkl'] = OrganizedDLCpaths

#save the df as a pkl file in google drive - this will overwrite the MovementIGInjectionFilesDF.pkl file
path2saveDF = FilesDFpath
FilesDF.to_pickle(path2saveDF)
print('\n\nThe MovementIGinjectionFilesDF.pkl file was updated.')