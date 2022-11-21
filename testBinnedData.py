import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#create SN sucrose signal
#create empty arry
sucroseSN_sessions = np.zeros((90,))
num_sessions = 0
for i, binnedCatheterVel in enumerate(FilesDF['binnedCatheterVel.npy']):
    if FilesDF['Reinforcer'][i] == 'SUCROSE' and FilesDF['Imaging'][i] == 'SN':
        num_sessions += 1
        currentSession = np.load(binnedCatheterVel)
        sucroseSN_sessions = np.sum([sucroseSN_sessions, currentSession], axis=0)
sucroseSN_sessions = sucroseSN_sessions/num_sessions
print(num_sessions)

#create SN sucralose signal
#create empty arry
sucraloseSN_sessions = np.zeros((90,))
num_sessions = 0
for i, binnedCatheterVel in enumerate(FilesDF['binnedCatheterVel.npy']):
    if FilesDF['Reinforcer'][i] == 'SUCROSE' and FilesDF['Imaging'][i] == 'VTA':
        num_sessions += 1
        currentSession = np.load(binnedCatheterVel)
        sucraloseSN_sessions = np.sum(
            [sucraloseSN_sessions, currentSession], axis=0)
sucraloseSN_sessions = sucraloseSN_sessions/num_sessions
print(num_sessions)


plt.plot(sucroseSN_sessions)
plt.plot(sucraloseSN_sessions)
plt.ylim([0,10])
plt.show()
