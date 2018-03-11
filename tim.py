import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns
from datetime import datetime

pd.set_option('max_columns', None)
# %matplotlib inline
# %config InlineBackend.figure_format = 'retina'
rcParams['figure.figsize'] = 12, 10


class CrimeAnalysis:
    def __init__(self):
        self.fn = 'crime.txt'
        self.df = self.build_df()

    def build_df(self):
        df = pd.read_csv(self.fn)
        df.columns = ['agency', 'crime', 'time', 'addr', 'zip', 'community']
        df['crime'] = df['crime'].astype(str)
        return df

    @staticmethod
    def time_fix(row):
        t = str(row['time'])
        return datetime.strptime(t, "%m/%d/%Y %H:%M:%S")

    @staticmethod
    def add_doy(row):
        d = row['time_fix']
        return d.timetuple().tm_yday

    @staticmethod
    def add_month(row):
        m = row['time_fix']
        return m.month

    @staticmethod
    def add_hour(row):
        h = row['time_fix']
        return h.hour

    @staticmethod
    def type_find(row):
        t = str(row['crime']).lower()
        if 'firearm' in t or 'ammunition' in t or 'shoot' in t:
            return 'gun'
        if 'controlled' in t or 'contr' in t or 'drug' in t or 'paraphernalia' in t or 'cntl' in t:
            return 'drug'
        if 'theft' in t or 'burglary' in t or 'robbery' in t or 'obtain money' in t:
            return 'theft'
        if 'drunk' in t or 'liquor' in t or 'open container' in t or 'alcohol' in t or 'alc' in t:
            return 'alcohol'
        if 'marijuana' in t or 'cannabis' in t or 'weed' in t:
            return 'weed'
        if 'weapon' in t or 'metal knuckles' in t or 'leaded cane' in t or 'shuriken' in t or 'knife' in t or 'dagger' in t:
            return 'weapons'
        if 'sex' in t or 'rape' in t or 'intimate' in t or 'indecent exposure' in t or 'obscene' in t or 'prostitution' in t:
            return 'sexual'
        if 'assault' in t or 'battery' in t:
            return 'assault'
        if 'resist' in t:
            return 'resisting'
        if 'shoplifting' in t:
            return 'shoplifting'
        if 'fraud' in t or 'defraud' in t or 'personate' in t:
            return 'fraud'
        if 'vandalism' in t:
            return 'vandalism'
        if 'elder' in t:
            return 'elder abuse'
        if 'get credit' in t or 'personal identific' in t:
            return 'identity theft'
        if 'terrorize' in t or 'terrorist' in t:
            return 'terrorism'
        if 'animal' in t:
            return 'animal'
        if 'child' in t or 'minor' in t:
            return 'child'
        if 'tamper' in t or 'carjacking' in t:
            return 'vehicle tampering'
        if 'arson' in t:
            return 'arson'
        else:
            return 'none'

    def fix_df(self):
        df = self.df
        df['time_fix'] = df.apply(self.time_fix, axis=1)
        df['doy'] = df.apply(self.add_doy, axis=1)
        df['month'] = df.apply(self.add_month, axis=1)
        df['hour'] = df.apply(self.add_hour, axis=1)
        df['type'] = df.apply(self.type_find, axis=1)
        return df


if __name__ == '__main__':
    ca = CrimeAnalysis
    ca.fix_df()
