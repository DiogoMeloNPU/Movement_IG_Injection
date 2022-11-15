#this module will be for getting the file paths to provide as input for DLC analysis (obtaining the .h5 and .csv files to store at)

import pandas as pd
import numpy as np
import os
import cv2

drive_files_path_SNc = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\SNc"
drive_files_path_VTA = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\VTA"
drive_files_path_total = [drive_files_path_SNc, drive_files_path_VTA]

#create a function that computes the duration of a video in minutes given the video path
def video_duration_min(video_path):
    cap = cv2.VideoCapture(video_path)
    videofps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    if frame_count == 0:
        duration_min = -1
    else:
        duration_sec = frame_count/videofps
        duration_min = int(duration_sec/60)

    return duration_min, videofps

#create an array to save the video file paths
paths2inputDLCanalysis = []
#create an array to save the video aq rate
currentAqRate = []
#store the files in an array
for imaging_region in drive_files_path_total:
    for path, subdirs, files in os.walk(imaging_region):
        for name in files:
            if (name.endswith('.mp4') or name.endswith('.avi')) and 'labeled' not in name and '(1)' not in name:
                temp_path = os.path.join(path, name)
                temp_path = temp_path.split('\\')
                currentpath = '\\'.join(temp_path)
                #get the duration of the video in minutes
                duration_min, videofps = video_duration_min(currentpath)
                if duration_min > 20:
                    paths2inputDLCanalysis.append(currentpath)
                    currentAqRate.append(videofps)
                    print('The following video will be analyzed with DLC: {}'.format(currentpath))
                else:
                    print('The current video is 0 frames long and should be discarded: {}'.format(currentpath))

#create a 2D array to save the video aq rate and the video files paths
videoPathsAndFPS = [paths2inputDLCanalysis, currentAqRate]

#show the 2D array
print(videoPathsAndFPS)

#convert to np.array and save the variable as a .npy
videoPathsAndFPS = np.array(videoPathsAndFPS)
save_here = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\videoPathsAndFPS.npy"
np.save(save_here, videoPathsAndFPS, allow_pickle=True)

#how many videos will be analyzed
print('A total of {} videos will be analyzed.'.format(len(paths2inputDLCanalysis)))