#this module returns the paths of the videos whose DLC predictions were not filtered
#this videos correspond to those whose path is present in the videoPathsAndFPS.npy file, but whose filtered DLC coordinate predictions csv file was not produced

import numpy as np
import os

#indicate the path of the .npy file containing the video paths
videos2analyzepath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\videoPathsAndFPS.npy"

#load the .npy file
videoPathsandFPS = np.load(videos2analyzepath)

#create a variable to save the paths of the videos whose DLC predictions were not filtered
missingFiltering = []
#iterate through the file to search only the column in the 2D array corresponfing to the video paths
for i, path in enumerate(videoPathsandFPS[0]):
    videoName = path[:-4]
    filePatternDLC = 'DLC_resnet50_DLC_postingestiveReinforcersNov4shuffle1_500000_filtered.csv'
    file2search4 = videoName+filePatternDLC
    #if the file doesn't exist print its name and append the video path
    if not os.path.exists(file2search4):
        print('This file does not exist: {}'.format(file2search4))
        missingFiltering.append(path)

#print the number of videos that were not analyzed
if len(missingFiltering) == 0:
    print('All predictions were filtered!')
elif len(missingFiltering) == 1:
    print('Only one DLC file missing filtering.')
else:
    print('!!A total of {} prediction files were not filtered!!'.format(
        len(missingFiltering)))

#print the array
print(missingFiltering)

#convert to np.array and save the variable as a .npy
missingFiltering = np.array(missingFiltering)
save_here = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\missingFiltering.npy"
np.save(save_here, missingFiltering, allow_pickle=True)
