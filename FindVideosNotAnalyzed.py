#this module returns the paths of the videos that were not analyzed by the DLC networks
#this videos correspond to those whose path is present in the videoPathsAndFPS.npy file, but whose DLC coordinate predictions csv file was not produced
#the need for this arose due to the fact that the DLC analyzes was stopped due to errors (not identified yet) which led to it not running completely

import numpy as np
import os

#indicate the path of the .npy file containing the video paths
videos2analyzepath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\videoPathsAndFPS.npy"

#load the .npy file
videoPathsandFPS = np.load(videos2analyzepath) 

#create a variable to save the paths of the videos that were not analyzed
missingDLCanalysis = []
#iterate through the file to search only the column in the 2D array corresponfing to the video paths
for i, path in enumerate(videoPathsandFPS[0]):
    videoName = path[:-4]
    filePatternDLC = 'DLC_resnet50_DLC_postingestiveReinforcersNov4shuffle1_500000.csv'
    file2search4 = videoName+filePatternDLC
    #if the file doesn't exist print its name and append the video path 
    if not os.path.exists(file2search4):
        print('This file does not exist: {}'.format(file2search4))
        missingDLCanalysis.append(path)

#print the number of videos that were not analyzed
if len(missingDLCanalysis) == 0:
    print('All videos were analyzed!')
elif len(missingDLCanalysis) == 1:
    print('Only one video missing the DLC analysis.')
else:
    print('!!A total of {} videos were not analyzed!!'.format(len(missingDLCanalysis)))

#convert to np.array and save the variable as a .npy
missingDLCanalysis = np.array(missingDLCanalysis)
save_here = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\missingDLCanalysis.npy"
np.save(save_here, missingDLCanalysis, allow_pickle=True)