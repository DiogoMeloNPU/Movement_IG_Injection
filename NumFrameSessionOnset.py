#After running FilesDF.py...

#OpenCV - search a video frame by frame and press a specific key when you find the session 
# onset (which is marked by the moment in which the light is switched on)

#all videos were recorded at 15 Hz

import pandas as pd
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

#implement a way to save the current state of the sessionOnsets array as .npy and restart where I left (so that if something wrong happens during identification of session
# onset frames, I don't lose the info on the videos I had already checked)

#the implementation of the onset_added variable only works if the videos are all closed with the specified 'character'. Otherwise, if the loop doesn't run until the end, 
#...the size of the array will not match the number of videos

#create an array to save all the frame numbers corresponding to the session onset
sessionOnsets = []
for video_path in FilesDF['VideoPath']:
    #create a variable to check if a frame of session onset was identified for the current video (in each iteration)
    onset_added = False
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        # Read video capture
        ret, frame = cap.read()
        # Display each frame
        cv2.putText(frame, video_path.split('\\')[-1], (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow("video", frame)
        # show one frame at a time
        key = cv2.waitKey(0)
        while key not in [ord('q'), ord('k'), ord('s'), ord('b')]:
            key = cv2.waitKey(0)
        #go back in the video one frame at a time
        if key == ord('b'):
            rewind_key_action()
        #save the number
        if key == ord('s'):
            numFrameSessionOnset = int(cap.get(cv2.CAP_PROP_POS_FRAMES))
            sessionOnsets.append(numFrameSessionOnset)
            onset_added = True
            break
        # Quit when 'q' is pressed
        if key == ord('q'):
            if onset_added == False:
                sessionOnsets.append(-1)
            break

#correct the array for the cases in which the user just closes the loop before it running completely
videos_not_assessed = -1*np.ones(len(FilesDF)-len(sessionOnsets))
print(videos_not_assessed)
sessionOnsets = np.concatenate(sessionOnsets, videos_not_assessed)

#print the values that will be stored as .npy
print(sessionOnsets)

#before saving, complete the array (until its length equals the number of videos used) with -1, to signal for 'num of onset frame not obtained yet'
#save as .npy and filll the 'unfilled' with -1
sessionOnsets = np.array(sessionOnsets)
path2saveNPY = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\numFrameSessionOnset.npy"
np.save(path2saveNPY, sessionOnsets)

#If you reached this part of the code you have an array with the number of the frames corresponding to the beggining of each session
#So, it is time to place those values in the proper column of FilesDF and store the file again as pkl
FilesDF['FrameSessionOnset'] = sessionOnsets

#show the df
print(FilesDF)

#save the updated file as pkl
if -1 not in sessionOnsets:
    FilesDF.to_pickle(FilesDF_path)