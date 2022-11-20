import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#open the FilesDF.pkl that was created in FilesDF.py
FilesDFpath = "E:\\.shortcut-targets-by-id\\1un_-G2CqE1eg6sx5KdpwrQRyPBJ1REFA\\All_video_data_baseline\\MovementIGInjectionFilesDF.pkl"
FilesDF = pd.read_pickle(FilesDFpath)

#ask the user if he wants to plot the prediction likelihood histograms
see_plots = input('Do you want to plot the prediction likelihood histograms? (1 for YES, 0 for NO)')

if see_plots == str(1):
    #check the likelihood distribution of the catheter and the tailbase likelihood for each session
    for sessionVelMagnitude in FilesDF['velMagnitude.pkl']:
        if isinstance(sessionVelMagnitude, str):
            df = pd.read_pickle(sessionVelMagnitude)
            catheter_likelihoods = np.array(df['catheter_likelihood'])
            tailbase_likelihoods = np.array(df['tailbase_likelihood'])
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
            plt.suptitle('_'.join(sessionVelMagnitude.split('\\')[-1].split('_')[1:5]))
        plt.show()

#check the distribution of the fraction of the session in which the likelihood of the predictions is > 0.9
see_fractions_hist = input('Do you want to check the distribution of the fractions of the session in which the likelihood o the predictions is > 0.9? (1 for YES, 0 for NO)')

#establish a criteria based on the likelihood distribution during the session
# I will start by setting the session inclusion criteria to be at leat 80% of the video with > 0.9 prediction likelihood
sessionFraction = 0.6
predictionLikelihood = 0.95

if see_fractions_hist == str(1):
    #create vectors to save the fractions of the sessions in which prediction likelihood > 0.9
    catheterFractionsAboveCutoff = []
    tailbaseFractionsAboveCutoff = []
    #create an array of 1/0s to identify which sessions will be used for analysis
    includeInAnalysis = []
    for sessionVelMagnitude in FilesDF['velMagnitude.pkl']:
        if isinstance(sessionVelMagnitude, str):
            print(sessionVelMagnitude)
            #open the dataframe
            df = pd.read_pickle(sessionVelMagnitude)
            #save likelihoods in separate numpy arrays
            catheter_likelihoods = np.array(df['catheter_likelihood'])
            tailbase_likelihoods = np.array(df['tailbase_likelihood'])
            #count the occurences of likelihood > 0.9
            num_catheterCorrectLabel = np.count_nonzero(catheter_likelihoods>=predictionLikelihood)
            num_tailbaseCorrectLabel = np.count_nonzero(tailbase_likelihoods>=predictionLikelihood)
            #save the fractions of the current session in separate arrays (need to divide by the dataframe length)
            catheterFractionsAboveCutoff.append(num_catheterCorrectLabel/len(df))
            tailbaseFractionsAboveCutoff.append(num_tailbaseCorrectLabel/len(df))
            #decide if the session will be in the analysis (based on the catheter predictions)
            if num_catheterCorrectLabel/len(df) >= sessionFraction:
                includeInAnalysis.append(1)
            else:
                includeInAnalysis.append(0)
    plt.subplot(1,2,1)
    plt.hist(catheterFractionsAboveCutoff, bins=20)
    #sns.kdeplot(catheterFractionsAboveCutoff)
    plt.xlabel('Fraction of session above 0.95 likelihood')
    plt.ylabel('Count')
    plt.title('Catheter')
    plt.ylim(0, len(catheterFractionsAboveCutoff))
    plt.subplot(1,2,2)
    plt.hist(tailbaseFractionsAboveCutoff, bins=20)
    #sns.kdeplot(tailbaseFractionsAboveCutoff)
    plt.xlabel('Fraction of session above 0.95 likelihood')
    plt.title('Tailbase')
    plt.ylim(0, len(tailbaseFractionsAboveCutoff))
    plt.show()

#show the df
print(FilesDF)

#create a bool variable that indicates which videos can be used based on the criteria defined based on the distributions
FilesDF['IncludeInAnalysis'] = includeInAnalysis
FilesDF.to_pickle(FilesDFpath)