import matplotlib.pyplot as plt
import numpy as np

'''signal1_VTA = np.random.randint(4000, 5000, 100)
signal2_VTA = np.random.randint(3000, 3500, 100)
signal3_VTA = np.random.randint(7000, 7800, 100)
signal4_VTA = np.random.randint(1500, 2500, 100)
signal1_SN = np.random.randint(4000, 5000, 100)
signal2_SN = np.random.randint(3000, 3500, 100)
signal3_SN = np.random.randint(7000, 7800, 100)
signal4_SN = np.random.randint(1500, 2500, 100)'''

fig, ((ax_VTA, ax_SN)) = plt.subplots(1, 2, constrained_layout=False)

# set the spacing between subplots
fig.subplots_adjust(left=0.1,
                    bottom=0.1,
                    right=0.9,
                    top=0.9,
                    wspace=0.25,
                    hspace=0.4)

ratio = 0.7

ax_VTA.set_ylim([0, 10000])
ax_VTA.set_title('Ventral Tegmental Area (VTA)', pad=20)
ax_VTA.set_ylabel('Movement\n(Pixel change)')
ax_VTA.set_xlabel('Time (s)')
ax_VTA.plot(np.linspace(-300, 600, 135),
            binned_data_median[8:8+135], label='Intragastric Sucrose', linewidth=0.9, color='r')
'''ax_VTA.plot(np.linspace(-300, 600, 100), signal1_VTA, label = 'Intragastric Sucrose', color = 'r', linewidth = 0.9)
ax_VTA.fill_between(np.linspace(-300, 600, 100), 
                 signal1_VTA - 200,
                 signal1_VTA + 200, alpha = 0.2, color = 'r')'''
ax_VTA.plot(np.linspace(-300, 600, 100), signal2_VTA,
            label='Intragastric Sucralose', color='black', linewidth=0.9)
ax_VTA.fill_between(np.linspace(-300, 600, 100),
                    signal2_VTA - 200,
                    signal2_VTA + 200, alpha=0.2, color='black')
ax_VTA.plot(np.linspace(-300, 600, 100), signal3_VTA,
            label='Intragastric Corn Oil', color='blue', linewidth=0.9)
ax_VTA.fill_between(np.linspace(-300, 600, 100),
                    signal3_VTA - 200,
                    signal3_VTA + 200, alpha=0.2, color='blue')
ax_VTA.plot(np.linspace(-300, 600, 100), signal4_VTA,
            label='Intragastric SMOF lipid', color='green', linewidth=0.9)
ax_VTA.fill_between(np.linspace(-300, 600, 100),
                    signal4_VTA - 200,
                    signal4_VTA + 200, alpha=0.2, color='green')
ax_VTA.spines['top'].set_visible(False)
ax_VTA.spines['right'].set_visible(False)
x_left, x_right = ax_VTA.get_xlim()
y_low, y_high = ax_VTA.get_ylim()
ax_VTA.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
ax_VTA.axvspan(0, 90, facecolor='r', alpha=0.2)
ax_VTA.set_xticks(np.arange(-300, 700, 100))
#leg_VTA = ax_VTA.legend(fontsize=8, frameon=False)

ax_SN.set_ylim([0, 10000])
ax_SN.set_title('Substancia Nigra (SN)', pad=20)
ax_SN.set_xlabel('Time (s)')
ax_SN.plot(np.linspace(-300, 600, 100), signal1_SN,
           label='Intragastric Sucrose', color='red', linewidth=0.9)
ax_SN.fill_between(np.linspace(-300, 600, 100),
                   signal1_SN - 200,
                   signal1_SN + 200, alpha=0.2, color='red')
ax_SN.plot(np.linspace(-300, 600, 100), signal2_SN,
           label='Intragastric Sucralose', color='black', linewidth=0.9)
ax_SN.fill_between(np.linspace(-300, 600, 100),
                   signal2_SN - 200,
                   signal2_SN + 200, alpha=0.2, color='black')
ax_SN.plot(np.linspace(-300, 600, 100), signal3_SN,
           label='Intragastric Corn Oil', color='blue', linewidth=0.9)
ax_SN.fill_between(np.linspace(-300, 600, 100),
                   signal3_SN - 200,
                   signal3_SN + 200, alpha=0.2, color='blue')
ax_SN.plot(np.linspace(-300, 600, 100), signal4_SN,
           label='Intragastric SMOF lipid', color='green', linewidth=0.9)
ax_SN.fill_between(np.linspace(-300, 600, 100),
                   signal4_SN - 200,
                   signal4_SN + 200, alpha=0.2, color='green')
ax_SN.spines['top'].set_visible(False)
ax_SN.spines['right'].set_visible(False)
x_left, x_right = ax_SN.get_xlim()
y_low, y_high = ax_SN.get_ylim()
ax_SN.set_aspect(abs((x_right-x_left)/(y_low-y_high))*ratio)
ax_SN.axvspan(0, 90, facecolor='r', alpha=0.2)
ax_SN.set_xticks(np.arange(-300, 700, 100))
leg_SN = ax_SN.legend(fontsize=8, frameon=False)
