#this module organizes every file containing the DLC predictions for easier manipulation of the data as a pandas dataframe
#it also stores each new file in the respective folder containing all other files (neuron.mat, simpler_neuron.mat, AccelData.csv,
# FrameDiff.csv, VideoProcessed.csv)
#finally it updates the MovementIGInjectionFilesDF.pkl with a new column with the paths for the files created here

from os import walk
import pandas as pd
import numpy as np
import os

def buildDLCpredictionsDF(path_predictions_DLC, path_acceldata):
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
FilesDFpath = 
FilesDF = pd.read_pickle(FilesDFpath)

#create an array to save the paths of the new OrganizedDLC files
OrganizedDLCpaths = []
#create a file pattern to name the new files
file_pattern = 'OrganizedDLC_'
#create a new file with an organized dataframe of DLC predictions for all prediction files
for row, (DLCpredictionFile, AccelDataFile) in enumerate(zip(dystoniaFilesDF['DLC_coordinate_prediction.csv'], dystoniaFilesDF['AccelData.csv'])):
    #if the two files are present...
    if isinstance(DLCpredictionFile, str) and isinstance(AccelDataFile, str):
        #print('\n\n----Organize the following file and display the new dataframe----: {}'.format(DLCpredictionFile))
        organized_DLC_predictionsDF = buildDLCpredictionsDF(
            DLCpredictionFile, AccelDataFile)
        print(organized_DLC_predictionsDF)
        print(DLCpredictionFile, AccelDataFile)
        print('\n'*5)
        #create the path of the new file
        #temp_path = dystoniaFilesDF['neuron.mat'].iloc[row].split('\\')[:-1]
        #file_type = 'pkl'
        #temp_path.append(file_pattern+DLCpredictionFile.split('\\')[-1][:-3]+file_type)
        #same path as the other files, not the path of the original DLC file (which was in a separate folder)
        #path2save_organizedDLC_DF = '\\'.join(temp_path)
        #print('A new file was created in the following folder: {}'.format(path2save_organizedDLC_DF))
        #organized_DLC_predictionsDF.to_pickle(path2save_organizedDLC_DF)
        #OrganizedDLCpaths.append(path2save_organizedDLC_DF)
    else:
        OrganizedDLCpaths.append(np.nan)
