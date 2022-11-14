#After running FilesDF.py...

#OpenCV - search a video frame by frame and press a specific key when you find the session 
# onset (which is marked by the moment in which the light is switched on)

#all videos were recorded at 15 Hz

import pandas as pd
import cv2

#open the pkl file containing the video paths
FilesDF_path = "E:\\My Drive\\MovementIGInjectionFilesDF.pkl"
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

#create an array to save all the frame numbers corresponding to the session onset
sessionOnsets = []
for video_path in FilesDF['VideoPath']:
    cap = cv2.VideoCapture(video_path)
    while cap.isOpened():
        # Read video capture
        ret, frame = cap.read()
        # Display each frame
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
            break
        # Quit when 'q' is pressed
        if key == ord('q'):
            break

#If you reached this part of the code you have an array with the number of the frames corresponding to the beggining of each session
#So, it is time to place those values in the proper column of FilesDF and store the file again as pkl
FilesDF['FrameSessionOnset'] = sessionOnsets

#show the df
print(FilesDF)

#save the updated file as pkl
#FilesDF.to_pickle(FilesDF_path)