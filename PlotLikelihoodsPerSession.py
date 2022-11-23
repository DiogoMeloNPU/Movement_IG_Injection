import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

fig, ((ax_SN, ax_VTA)) = plt.subplots(1, 2, constrained_layout=False)

# set the spacing between subplots
fig.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.25,
                    hspace=0.4)

ratio = 0.7

upper_y_lim = 1.05
ax_SN.set_ylim([0, upper_y_lim])
ax_SN.set_title('Substancia Nigra (SN)', pad=20)
ax_SN.set_ylabel('Movement\n(px/fr)')
ax_SN.set_xlabel('Time (s)')
ax_SN.spines['top'].set_visible(False)
ax_SN.spines['right'].set_visible(False)

ax_VTA.set_ylim([0, upper_y_lim])
ax_VTA.set_title('Ventral Tegmental Area (VTA)', pad=20)
ax_VTA.set_xlabel('Time (s)')
ax_VTA.spines['top'].set_visible(False)
ax_VTA.spines['right'].set_visible(False)

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#find all possible combinations of 'Imaging area' and 'Reinforcer'
sessions = np.array(np.meshgrid(np.array(FilesDF['Imaging'].unique()), np.array(
    FilesDF['Reinforcer'].unique()[1:]))).T.reshape(-1, 2)
#sessions = ['_'.join(sessions[row,:]) for row in range(len(sessions))]
#print(sessions)
'''[['SN' 'CORNOIL']
 ['SN' 'SUCROSE']
 ['SN' 'SUCRALOSE']
 ['SN' 'SMOF']
 ['VTA' 'CORNOIL']
 ['VTA' 'SUCROSE']
 ['VTA' 'SUCRALOSE']
 ['VTA' 'SMOF']]'''  # result of 'print(sessions)'

num_bins = 90  # this value should come from another module

#establish the x limits of the plot
begg_second = -300
end_second = 600

#define a color for each reinforcer
color = ['r', 'black', 'blue', 'green']

for sessionType in sessions[:-1]:  # do not consider VTA/SMOF
    print('_'.join(sessionType))
    sessionTypeSignal = np.zeros((num_bins,))
    num_sessions = 0
    for i, binnedCatheterVel in enumerate(FilesDF['binnedCatheterLikelihood.npy']):
        if FilesDF['Imaging'][i] == sessionType[0] and FilesDF['Reinforcer'][i] == sessionType[1]:
            currentSession = np.load(binnedCatheterVel)
            if np.nan not in currentSession:
                num_sessions += 1
                sessionTypeSignal = np.concatenate(
                    (sessionTypeSignal, currentSession), axis=0)
            else:
                print('This session will not be considered, since it is only composed of nan values {}'.format(
                    currentSession))
    sessionTypeSignal = np.reshape(
        sessionTypeSignal, (num_sessions+1, num_bins))
    # starts in one to eliminate the first array which is a np.zeros()
    print(sessionTypeSignal[1:])
    Signal = np.round(np.mean(sessionTypeSignal[1:], axis=0), 2)
    print('Signal: {}'.format(Signal))
    StdError = np.round(
        (np.std(sessionTypeSignal[1:], axis=0)/np.sqrt(num_sessions)), 2)
    print('Standard Error: {}'.format(StdError))
    print(num_sessions)
    print('\n')
    if sessionType[0] == 'SN':
        ax_SN.plot(np.linspace(begg_second, end_second, len(Signal)), Signal,
                   label='Intragastric {} Sessions (n={})'.format(sessionType[1], num_sessions), linewidth=0.9)
        ax_SN.fill_between(np.linspace(begg_second, end_second, len(StdError)),
                           Signal - StdError,
                           Signal + StdError, alpha=0.2)
    else:  # VTA
        ax_VTA.plot(np.linspace(begg_second, end_second, len(Signal)), Signal,
                    label='Intragastric {} Sessions (n={})'.format(sessionType[1], num_sessions), linewidth=0.9)
        ax_VTA.fill_between(np.linspace(begg_second, end_second, len(StdError)),
                            Signal - StdError,
                            Signal + StdError, alpha=0.2)

x_left, x_right = ax_SN.get_xlim()
y_low, y_high = ax_SN.get_ylim()
ax_SN.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
ax_SN.axvspan(0, 90, facecolor='r', alpha=0.2)
ax_SN.set_xticks(np.arange(-300, 700, 100))
leg_SN = ax_SN.legend(fontsize=8, frameon=False)

x_left, x_right = ax_VTA.get_xlim()
y_low, y_high = ax_VTA.get_ylim()
ax_VTA.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
ax_VTA.axvspan(0, 90, facecolor='r', alpha=0.2)
ax_VTA.set_xticks(np.arange(-300, 700, 100))
leg_VTA = ax_VTA.legend(fontsize=8, frameon=False)

#show the figure
plt.show()
