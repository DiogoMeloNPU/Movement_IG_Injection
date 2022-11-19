import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#CHANGE THIS CODE TO CHECK THE LIKELIHOOD DISTRIBUTIONS DURING THE SESSION!!!! (by checking the velocity.pkl files)

#check the likelihood distribution of the catheter and the tailbase likelihood for each session
for sessionVelMagnitude in FilesDF['Organized_DLC_predictions.pkl']:
    if isinstance(DLCpath, str):
        df = pd.read_pickle(DLCpath)
        tailbase_likelihoods = np.array(df['catheter (likelihood)'])
        catheter_likelihoods = np.array(df['tailbase (likelihood)'])
        plt.subplot(1,2,1)
        plt.hist(catheter_likelihoods, bins=100)
        plt.xlabel('Likelihood')
        plt.ylabel('Count')
        plt.title('Catheter')
        plt.ylim(0, 15000)
        plt.subplot(1,2,2)
        plt.hist(tailbase_likelihoods, bins=100, color='lightskyblue')
        plt.xlabel('Likelihood')
        plt.title('Tail base')
        plt.ylim(0, 15000)
        plt.suptitle('_'.join(DLCpath.split('\\')[-1].split('_')[1:5]))
    plt.show()

#check the distribution of the fraction of the session in which the likelihood of the predictions is > 0.9

#ignore SMOF VTA

#establish a criteria based on the likelihood distribution during the session


#create a bool variable that indicates which videos can be used based on the criteria defined based on the distributions