import pandas as pd
import numpy as np
import os
import cv2

#Create a dataframe containing the paths for the session videos and DLC files

#define the column labels
columns = ['Imaging', 'MiceID', 'Reinforcer', 'SessionDay',
           'VideoPath', 'VideoAqRate', 'FrameSessionOnset', 'FilteredDLCPath']

#create the df
FilesDF = pd.DataFrame(columns = columns)

#load the video paths to create the dataframe
videoPathsAndFPS_path = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\videoPathsAndFPS.npy"
videoPathsAndFPS = np.load(videoPathsAndFPS_path)

#The following loop hasn't been tested for possible bugs. Be mindful that the multiple if statements to correct for files that were badly labeled may need to be updated for future use.
#Now, fill the dataframe using the info present in each video file name
for i in range(videoPathsAndFPS.shape[1]):
    file_name = videoPathsAndFPS[0, i].split('\\')[-1]
    #get the imaging region (either SN or VTA)
    imaging_region = file_name.split('_')[0]
    #get the MiceID
    MiceID = file_name.split('_')[1]
    #get the session day
    sessionDay = file_name.split('_')[3][3:]
    #correct the cases in which the file name doesn't start with the region being imaged
    if not file_name.startswith('SN') and not file_name.startswith('VTA'):
        prefix = videoPathsAndFPS[0, i].split('\\')[4]
        if prefix == 'SNc':
            imaging_region = 'SN'
        elif prefix == 'VTA':
            imaging_region = 'VTA'
        MiceID = file_name.split('_')[0]
        sessionDay = -1 #meaning I can't get that information from the file name
    #get the Reinforcer that was injected IG
    reinforcer = file_name.split('_')[2]
    #correct 'COIL'/'CORNOIL'
    if reinforcer == 'COIL':
        reinforcer = 'CORNOIL'
    #correct cases in which a date was incorporated in the name AND the beggining of the file name corresponds to the imaging region
    if reinforcer.isdigit():
        reinforcer = file_name.split('_')[3]
        sessionDay = file_name.split('_')[4][3:]
    #correct for specific error in building the file name 'M46682SUCROSE' (miceID and reinforcer are merged)
    if len(MiceID) > 6:
        sessionDay = reinforcer[3:]
        MiceID = MiceID[:6]
        reinforcer = file_name.split('_')[1][6:]
    #correct the sessionday in the case of a baseline session
    if reinforcer == 'BASELINE':
        sessionDay = 0
    #account for the names that may display a different pattern 
    if file_name:
        #fill the dataframe with the exception of the path of the filtered DLC coordinate predictions
        currentRowValues = {'Imaging': imaging_region, 'MiceID': MiceID, 'Reinforcer': reinforcer, 'SessionDay': sessionDay,
                            'VideoPath': videoPathsAndFPS[0, i], 'VideoAqRate': videoPathsAndFPS[1, i], 'FrameSessionOnset': np.nan, 'FilteredDLCPath': np.nan}
    #add the new row to the dataframe
    FilesDF = FilesDF.append(currentRowValues, ignore_index=True)

#delete if unnecessary
'''#folder containing all the files for the analysis
drive_files_path_SNc = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\SNc"
drive_files_path_VTA = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\VTA"
drive_files_path_total = [drive_files_path_SNc, drive_files_path_VTA]'''

#run this after the DLC analysis is complete
'''#Match the path of the filtered DLC predictions to the respective row in the df
for path, subdirs, files in os.walk(path_files):
    for name in files:
        if name.endswith('500000_filtered.csv'):
            #list containing the imaging region (0), the miceID (1), the Reinforcer (2), and the session day (3)
            currentDLCFile = [name.split('_')[0], name.split('_')[1], name.split('_')[2], name.split('_')[3][3:]]
            match = FilesDF.loc[(FilesDF['Imaging'] == currentDLCFile[0]) & (FilesDF['MiceID'] == currentDLCFile[1]) & (FilesDF['Reinforcer'] == currentDLCFile[2]) & (FilesDF['SessionDay'] == currentDLCFile[3])]
            if len(match) == 1:
                FilesDF['FilteredDLCPath'][match.index[0]] = os.path.join(path, name)'''

#show the df
print(FilesDF)

#save the df in google drive as pkl
path2saveFilesDF = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF.to_pickle(path2saveFilesDF)

#if you want, you an also save it in other formats (such as csv for easier direct search - not recommended)
#save the df in google drive as csv
#path2saveFilesDF = "E:\\My Drive\\MovementIGInjectionFilesDF.csv"
#FilesDF.to_csv(path2saveFilesDF)