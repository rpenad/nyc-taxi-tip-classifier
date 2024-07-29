import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
import joblib

def train_and_evaluate(train_file, test_file):
    train_df = pd.read_csv(train_file)
    test_df = pd.read_csv(test_file)
    
    features = [
        "pickup_weekday", "pickup_hour", 'work_hours', "pickup_minute",
        "passenger_count", 'trip_distance', 'trip_time', 'trip_speed',
        "PULocationID", "DOLocationID", "RatecodeID"
    ]

    X_train = train_df[features]
    y_train = train_df['high_tip']
    X_test = test_df[features]
    y_test = test_df['high_tip']
    
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    score = f1_score(y_test, y_pred)
    print(f'F1-score: {score:.4f}')
    
    joblib.dump(model, 'models/random_forest_model.pkl')

    feature_importances = model.feature_importances_
    return feature_importances

if __name__ == '__main__':
    jan_importances = train_and_evaluate('data/interim/preprocessed_data_jan.csv', 'data/interim/preprocessed_data_feb.csv')
    feb_importances = train_and_evaluate('data/interim/preprocessed_data_feb.csv', 'data/interim/preprocessed_data_jan.csv')

    print("Feature Importances for January Model:", jan_importances)
    print("Feature Importances for February Model:", feb_importances)
