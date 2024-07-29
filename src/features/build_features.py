import pandas as pd

def preprocess(df, target_col):
    EPS = 1e-7

    df = df[df['fare_amount'] > 0].reset_index(drop=True)
    df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
    df[target_col] = df['tip_fraction'] > 0.2
    df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_minute'] = df['tpep_pickup_datetime'].dt.minute
    df['work_hours'] = (df['pickup_weekday'] >= 0) & (df['pickup_weekday'] <= 4) & (df['pickup_hour'] >= 8) & (df['pickup_hour'] <= 18)
    df['trip_time'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
    df['trip_speed'] = df['trip_distance'] / (df['trip_time'] / 60 + EPS)
    return df

if __name__ == '__main__':
    df = pd.read_csv('data/raw/yellow_tripdata_2020-01.csv')
    df = preprocess(df, 'high_tip')
    df.to_csv('data/interim/preprocessed_data_jan.csv', index=False)

    df = pd.read_csv('data/raw/yellow_tripdata_2020-02.csv')
    df = preprocess(df, 'high_tip')
    df.to_csv('data/interim/preprocessed_data_feb.csv', index=False)
