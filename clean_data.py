import pandas as pd
import numpy as np
import re

total = pd.read_csv('poeltl_data/poeltl_data.csv')

BOS = pd.read_csv('poeltl_data/EA/BOS.csv')
PHI = pd.read_csv('poeltl_data/EA/PHI.csv')
BRK = pd.read_csv('poeltl_data/EA/BRK.csv')
NYK = pd.read_csv('poeltl_data/EA/NYK.csv')
TOR = pd.read_csv('poeltl_data/EA/TOR.csv')
MIL = pd.read_csv('poeltl_data/EC/MIL.csv')
DET = pd.read_csv('poeltl_data/EC/DET.csv')
CLE = pd.read_csv('poeltl_data/EC/CLE.csv')
IND = pd.read_csv('poeltl_data/EC/IND.csv')
CHI = pd.read_csv('poeltl_data/EC/CHI.csv')
MIA = pd.read_csv('poeltl_data/ESE/MIA.csv')
ATL = pd.read_csv('poeltl_data/ESE/ATL.csv')
WAS = pd.read_csv('poeltl_data/ESE/WAS.csv')
ORL = pd.read_csv('poeltl_data/ESE/ORL.csv')
CHO = pd.read_csv('poeltl_data/ESE/CHO.csv')
DEN = pd.read_csv('poeltl_data/WNW/DEN.csv')
UTA = pd.read_csv('poeltl_data/WNW/UTA.csv')
MIN = pd.read_csv('poeltl_data/WNW/MIN.csv')
OKC = pd.read_csv('poeltl_data/WNW/OKC.csv')
POR = pd.read_csv('poeltl_data/WNW/POR.csv')
SAC = pd.read_csv('poeltl_data/WP/SAC.csv')
GSW = pd.read_csv('poeltl_data/WP/GSW.csv')
LAC = pd.read_csv('poeltl_data/WP/LAC.csv')
PHO = pd.read_csv('poeltl_data/WP/PHO.csv')
LAL = pd.read_csv('poeltl_data/WP/LAL.csv')
MEM = pd.read_csv('poeltl_data/WSW/MEM.csv')
NOP = pd.read_csv('poeltl_data/WSW/NOP.csv')
DAL = pd.read_csv('poeltl_data/WSW/DAL.csv')
SAS = pd.read_csv('poeltl_data/WSW/SAS.csv')
HOU = pd.read_csv('poeltl_data/WSW/HOU.csv')

total.drop(labels='Player-additional', axis=1, inplace=True)

sum_lis = [BOS, PHI, BRK, NYK, TOR, MIL, DET, CLE, IND, CHI, MIA, ORL, ATL, CHO, WAS,
          DEN, MIN, UTA, POR, OKC, SAC, GSW, LAC, PHO, LAL, MEM, NOP, DAL, SAS, HOU]

tot_team = pd.concat(sum_lis)

new_tot = pd.merge(total, tot_team, on='Player', how='left')

new_tot = new_tot.dropna()


def add_conf_div(new_tot):
    Div = []
    Conf = []

    for row in new_tot['Tm']:
        if row == 'TOR':
            Div.append('Atl.')
            Conf.append('East')
        elif row == 'BRK':
            Div.append('Atl.')
            Conf.append('East')
        elif row == 'NYK':
            Div.append('Atl.')
            Conf.append('East')
        elif row == 'PHI':
            Div.append('Atl.')
            Conf.append('East')
        elif row == 'BOS':
            Div.append('Atl.')
            Conf.append('East')
        elif row == 'DET':
            Div.append('Cen.')
            Conf.append('East')
        elif row == 'MIL':
            Div.append('Cen.')
            Conf.append('East')
        elif row == 'CLE':
            Div.append('Cen.')
            Conf.append('East')
        elif row == 'IND':
            Div.append('Cen.')
            Conf.append('East')
        elif row == 'CHI':
            Div.append('Cen.')
            Conf.append('East')
        elif row == 'MIA':
            Div.append('SE')
            Conf.append('East')
        elif row == 'ATL':
            Div.append('SE')
            Conf.append('East')
        elif row == 'WAS':
            Div.append('SE')
            Conf.append('East')
        elif row == 'ORL':
            Div.append('SE')
            Conf.append('East')
        elif row == 'CHO':
            Div.append('SE')
            Conf.append('East')
        elif row == 'POR':
            Div.append('NW')
            Conf.append('West')
        elif row == 'MIN':
            Div.append('NW')
            Conf.append('West')
        elif row == 'OKC':
            Div.append('NW')
            Conf.append('West')
        elif row == 'UTA':
            Div.append('NW')
            Conf.append('West')
        elif row == 'DEN':
            Div.append('NW')
            Conf.append('West')
        elif row == 'LAC':
            Div.append('Pac.')
            Conf.append('West')
        elif row == 'LAL':
            Div.append('Pac.')
            Conf.append('West')
        elif row == 'PHO':
            Div.append('Pac.')
            Conf.append('West')
        elif row == 'SAC':
            Div.append('Pac.')
            Conf.append('West')
        elif row == 'GSW':
            Div.append('Pac.')
            Conf.append('West')
        elif row == 'HOU':
            Div.append('SW')
            Conf.append('West')
        elif row == 'SAS':
            Div.append('SW')
            Conf.append('West')
        elif row == 'MEM':
            Div.append('SW')
            Conf.append('West')
        elif row == 'NOP':
            Div.append('SW')
            Conf.append('West')
        elif row == 'DAL':
            Div.append('SW')
            Conf.append('West')
        else:
            Div.append(np.NaN)
            Conf.append(np.NaN)


    new_tot['Div'] = Div
    new_tot['Conf'] = Conf

    return new_tot

def convert_feet(str_h):
    m = re.match(r'^(\d+)\-(\d+)$', str_h)
    if m:
        return float(m.group(1)) + (float(m.group(2))/12)
    else:
        return None


new_tot = add_conf_div(new_tot)

new_tot['Ht'] = new_tot['Ht'].apply(convert_feet)

print(new_tot[new_tot['Player']=='Anthony Davis'])
print(new_tot[new_tot['Player']=='Darius Bazley'])

new_tot.to_csv('poeltl_data/clean_tot.csv', index_label=False)
