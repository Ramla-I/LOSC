import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

fn = Path('~/Desktop/mm_eval.svg').expanduser()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, sharey=True)
# fig.suptitle('Time to Map, Remap and Unmap a 4 KiB Page')
# plt.xlabel('Total Mappings')
# plt.ylabel('Time (ns)')
fig.subplots_adjust(bottom = 0.201, top = 0.812)
fig.text(0.51, 0.01, 'Total Mappings', ha='center')

df_map = pd.DataFrame({
    'total mappings': ['10^2', '10^3', '10^4', '10^5'],
    'Theseus': [474.21, 492.45, 525.88, 590.74],
    'Verified Theseus': [484.75, 494.55, 530.04, 594.95]
})

yerr_map = [[15.22,2.08,14.40,19.77], [9.93,6.27,12.41,7.15]]

df_remap = pd.DataFrame({
    'total mappings': ['10^2', '10^3', '10^4', '10^5'],
    'Theseus': [8611.71, 8621.28, 8542.41, 8632.16],
    'Verified Theseus': [8536.25, 8539.45, 8456.37, 8473.11]
})
yerr_remap = [[71.56, 30.96, 13.74, 105.15], [69.58, 35.76, 16.88, 58.60]]

df_unmap = pd.DataFrame({
    'total mappings': ['10^2', '10^3', '10^4', '10^5'],
    'Theseus': [7957.62, 8063.04, 8086.53, 8195.73],
    'Verified Theseus': [7819.33, 8020.60, 7971.50, 8057.61]
})
yerr_unmap = [[60.16, 30.95, 22.03, 41.35], [86.94, 10.05, 30.12, 222.97]]


df_map.plot(x='total mappings', y=['Theseus', 'Verified Theseus'], kind='bar', ax=ax1,
        yerr=yerr_map, capsize=2, legend=False, xlabel='(a) Map', ylabel='Time (ns)')
# df_map.plot.barh(df_map['Theseus'], height=0.3, width = 0.2, hatch='/')
bars = ax1.patches
bars[0].set_hatch('//')
bars[1].set_hatch('//')
bars[2].set_hatch('//')
bars[3].set_hatch('//')

df_remap.plot(x='total mappings', y=['Theseus', 'Verified Theseus'], kind='bar', ax=ax2,
        yerr=yerr_remap, capsize=2, legend=False, xlabel='(b) Remap')
bars = ax2.patches
bars[0].set_hatch('//')
bars[1].set_hatch('//')
bars[2].set_hatch('//')
bars[3].set_hatch('//')


df_unmap.plot(x='total mappings', y=['Theseus', 'Verified Theseus'], kind='bar', ax=ax3,
        yerr=yerr_unmap, capsize=2, legend=False, xlabel='(c) Unmap')
bars = ax3.patches
bars[0].set_hatch('//')
bars[1].set_hatch('//')
bars[2].set_hatch('//')
bars[3].set_hatch('//')

plt.legend(loc='center', bbox_to_anchor=(-0.7, 1.1), ncol=2)
plt.rcParams['figure.dpi']=500
plt.rcParams['pdf.fonttype']=42
plt.rcParams['ps.fonttype']=42
plt.show()

fig.savefig('mm_eval.eps', format='eps')