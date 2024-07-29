import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

def load_model(model_path):
    return joblib.load(model_path)

def preprocess(df):
    EPS = 1e-7

    df = df[df['fare_amount'] > 0].reset_index(drop=True)
    df['tip_fraction'] = df['tip_amount'] / df['fare_amount']
    df['high_tip'] = df['tip_fraction'] > 0.2
    df['pickup_weekday'] = df['tpep_pickup_datetime'].dt.weekday
    df['pickup_hour'] = df['tpep_pickup_datetime'].dt.hour
    df['pickup_minute'] = df['tpep_pickup_datetime'].dt.minute
    df['work_hours'] = (df['pickup_weekday'] >= 0) & (df['pickup_weekday'] <= 4) & (df['pickup_hour'] >= 8) & (df['pickup_hour'] <= 18)
    df['trip_time'] = (df['tpep_dropoff_datetime'] - df['tpep_pickup_datetime']).dt.total_seconds() / 60
    df['trip_speed'] = df['trip_distance'] / (df['trip_time'] / 60 + EPS)
    return df

def predict(model, df):
    features = [
        "pickup_weekday", "pickup_hour", 'work_hours', "pickup_minute",
        "passenger_count", 'trip_distance', 'trip_time', 'trip_speed',
        "PULocationID", "DOLocationID", "RatecodeID"
    ]
    X = df[features]
    predictions = model.predict(X)
    return predictions

if __name__ == '__main__':
    model_path = 'models/random_forest_model.pkl'
    data_path = 'data/raw/yellow_tripdata_2020-03.csv'  # Example path to new data

    model = load_model(model_path)
    df = pd.read_csv(data_path)
    df = preprocess(df)
    predictions = predict(model, df)

    # Save predictions to a CSV file
    df['predictions'] = predictions
    df.to_csv('data/predictions/predictions_2020-03.csv', index=False)
