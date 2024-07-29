import pandas as pd

def download_data():
    url_jan = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-01.parquet'
    url_feb = 'https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2020-02.parquet'
    
    df_jan = pd.read_parquet(url_jan)
    df_feb = pd.read_parquet(url_feb)
    
    df_jan.to_csv('data/raw/yellow_tripdata_2020-01.csv', index=False)
    df_feb.to_csv('data/raw/yellow_tripdata_2020-02.csv', index=False)

if __name__ == '__main__':
    download_data()
