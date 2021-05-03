def main():
    import pandas as pd
    import numpy as np
    df = pd.read_csv("detail.csv")
    df['Absolute Time'] = pd.to_datetime(df['Absolute Time'])
    df1 = df.set_index('Absolute Time').resample('T').agg(
        {'Record Index': np.size, 'Status': np.size, 'JumpTo': np.mean, 'Cycle': np.mean, 'Step': np.mean,
         'Cur(mA)': np.mean, 'Voltage(V)': np.mean, 'CapaCity(mAh)': np.mean, 'Energy(mWh)': np.mean})
    df1.head(10)
    df1.to_csv('detailDownsampled.csv')
    print("Downsampled csv file : 'detailDownsampled.csv' created!!")
    df = pd.read_csv("detailvol.csv")
    df['Realtime'] = pd.to_datetime(df['Realtime'])
    df1 = df.set_index('Realtime').resample('T').agg(
        {'Record ID': np.size, 'Step Name': np.size, 'Auxiliary channel TU1 U(V)': np.mean, 'Gap of Voltage': np.mean})
    df1.head(10)
    df1.to_csv('detailVolDownsampled.csv')
    print("Downsampled csv file : 'detailVolDownsampled.csv' created!!")
    df = pd.read_csv("detailtemp.csv")
    df['Realtime'] = pd.to_datetime(df['Realtime'])
    df1 = df.set_index('Realtime').resample('T').agg(
        {'Record ID': np.size, 'Step Name': np.size, 'Auxiliary channel TU1 T(°C)': np.mean,
         'Gap of Temperature': np.mean})
    df1.head(10)
    df1.to_csv('detailTempDownsampled.csv')
    print("Downsampled csv file : 'detailTempDownsampled.csv' created!!")

    
if __name__ == '__main__':
    import cProfile
    cProfile.run('main()')

