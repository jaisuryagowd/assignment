#Task 4
import cProfile
import pandas as pd
def dst():
    df = pd.read_csv('detailTemp.csv', parse_dates = ["Realtime"], index_col = "Realtime")
    df = df.resample('T').mean()

def dsv():
    df = pd.read_csv('detailVol.csv', parse_dates = ["Realtime"], index_col = "Realtime")
    df = df.resample('T').mean()

def ds():
    df = pd.read_csv('detail.csv', parse_dates = ["Absolute Time"], index_col = "Absolute Time")
    df = df.resample('T').mean()

#Applying cProfile for down sampling method defined above
cProfile.run('dsv()')
cProfile.run('dst()')
cProfile.run('ds()')


