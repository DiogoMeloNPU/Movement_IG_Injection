#this module will be for getting the file paths to provide as input for DLC analysis (obtaining the .h5 and .csv files to store at)

import pandas as pd
import numpy as np
import os
import cv2

drive_files_path_SNc = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\SNc"
drive_files_path_VTA = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\VTA"
drive_files_path_total = [drive_files_path_SNc, drive_files_path_VTA]

#create an array to save the video file paths
paths2inputDLCanalysis = []
#store the files in an array
for imaging_region in drive_files_path_total:
    for path, subdirs, files in os.walk(imaging_region):
        for name in files:
            if (name.endswith('.mp4') or name.endswith('.avi')) and 'labeled' not in name and '(1)' not in name:
                temp_path = os.path.join(path, name)
                temp_path = temp_path.split('\\')
                currentpath = '\\'.join(temp_path)
                paths2inputDLCanalysis.append(currentpath)
#show the complete array
print(paths2inputDLCanalysis)