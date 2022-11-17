#this module reads each organizedDLC dataframe and creates a new dataframe with the total velocities
#of each bodypart
#the unit of velocity magnitude is PX/FRAME and needs no normalization since all videos have the same resolution

import pandas as pd
import numpy as np

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#create a variable to define the session duration in minutes
session_duration_min = 15

def convert_min2frames(videofps, min):
    #This function converts the session duration from minutes to frames
    seconds = min*60
    session_duration_frames = video_fps*seconds

    return session_duration_frames

def calculateBodyPartVel(df_predictions, loc, FrameSessionOnset):
    ''' 
    This function calculates the magnitude of the velocity of a bodypart given the DLC predictions 
    ...DF, as well as the location of the likelihood column.
    It also receives the number of the frame of session onset which allows me to obtain only the velocities I want to plot...
    ...(which should correspond to a 15 min recording from the frame number given as input).
    With that info I can extrapolate the location of the x and y coordinates across the recording and compute the 
    ...magnitude of the body part velocity.
    '''
    #create a variable to define the session duration in frames
    session_duration_frames = convert_min2frames(FilesDF['VideoAqRate'][loc], session_duration_min)
    #obtain an array containing all the v_xy values - square root of the sum of the velocity components squared
    velMagnitude = np.sqrt(df_predictions[df_predictions.columns[loc-2]]**2 + df_predictions[df_predictions.columns[loc-1]]**2)
    #convert to numpy array
    velMagnitude = np.array(velMagnitude)
    #get only the first 15 minutes hint:[FrameSessionOnset:FrameSessionOnset+session_duration_frames]
    velMagnitude = velMagnitude[FrameSessionOnset:FrameSessionOnset+session_duration_frames]

    return velMagnitude

for i, path in enumerate(FilesDF['Organized_DLC_predictions.pkl']):
    #read the current file containing organizedDLCpredictions
    df_predictions = pd.read_pickle(path)
    #create a new df for the velocities
    df_velMagnitude = pd.DataFrame()
    #calculate the difference between the x and y coordinates of consecutive frames
    for column in df_predictions.columns:
        if ('likelihood') not in column:
            df_predictions[column] = np.abs(df_predictions[column].diff())
    #change the name of the columns
    column_names = []
    for col in df_predictions.columns:
        if 'likelihood' not in col:
            column_names.append('Vel - ' + col)
    df_predictions.columns = column_names
    #for each body part (x and y columns) create a column in a new dataframe containing the total velocity
    for col in df_predictions:
        #for each body part
        if 'likelihood' in col:
            loc = df_predictions.columns.get_loc(col)
            #create the arrays 
            velMagnitude = calculateBodyPartVel(df_predictions, loc, FilesDF['FrameSessionOnset'][i])
            #for example: you start with 'right_ear (likelihood)' and get 'VelMagnitude_right_ear'
            name_column = 'VelMagnitude_' + df_predictions.columns[loc].split(" ")[0]
            df_velMagnitude[name_column] = velMagnitude
    #delete
    print(df_velMagnitude)
    #create the path to save the new dataframe as pickle
    #save the new dataframe containing the velocities in the indicated path