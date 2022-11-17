#After running FilesDF.py...

#OpenCV - search a video frame by frame and press a specific key when you find the session 
# onset (which is marked by the moment in which the light is switched on)

#all videos were recorded at 15 Hz

import pandas as pd
import numpy as np
import cv2

#open the pkl file containing the video paths
FilesDF_path = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDF_path)

#create a function to rewind one second
def rewind_key_action():
    #gets the current frame number
    frame_counter = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
    #gets the frame rate
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    #makes sure it goes back to the first frame when less than 1 second has passed
    frame_counter = max(0, int(frame_counter - (video_fps)))
    #resets the current frame to one second earlier
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_counter)

#ask for user input to check if the numFrameSessionOnset.npy file already exists
file_exists = input("Does the file numFrameSessionOnset (1 (for YES) OR 0 (for NO)): ")

#create a path to save the array where all the frame numbers corresponding to the session onset are stored
path2saveNPY = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\numFrameSessionOnset.npy"

#if the file already exists, you can skip the already assessed videos and check those that were not
if file_exists:
    sessionOnsets = np.load(path2saveNPY).tolist()
else:
    #create an array to save all the frame numbers corresponding to the session onset
    sessionOnsets = []

for i, video_path in enumerate(FilesDF['VideoPath']):
    if i >= len(sessionOnsets):
        #create a variable to check if a frame of session onset was identified for the current video (in each iteration)
        onset_added = False
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            #read video capture
            ret, frame = cap.read()
            #display each frame
            cv2.putText(frame, video_path.split('\\')[-1], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
            cv2.imshow("video", frame)
            #show one frame at a time
            key = cv2.waitKey(0)
            while key not in [ord('q'), ord('k'), ord('s'), ord('b')]:
                key = cv2.waitKey(0)
            #go back in the video 
            if key == ord('b'):
                rewind_key_action()
            #save the number
            if key == ord('s'):
                numFrameSessionOnset = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
                sessionOnsets.append(numFrameSessionOnset)
                print(numFrameSessionOnset)
                np.save(path2saveNPY, sessionOnsets)
                onset_added = True
                break
            #quit when 'q' is pressed
            if key == ord('q'):
                if onset_added == False:
                    sessionOnsets.append(-1)
                    print(-1)
                    np.save(path2saveNPY, sessionOnsets)
                break

#If you reached this part of the code you have an array with the number of the frames corresponding to the beggining of each session
#So, it is time to place those values in the proper column of FilesDF and store the file again as pkl
FilesDF['FrameSessionOnset'] = sessionOnsets

#show the df
print(FilesDF)

#save the updated file as pkl
if -1 not in sessionOnsets:
    FilesDF.to_pickle(FilesDF_path)