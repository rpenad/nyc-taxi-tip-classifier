import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_feature_importances(importances, features, month_name):
    feature_importances_df = pd.DataFrame({
        'Feature': features,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Importance', y='Feature', data=feature_importances_df)
    plt.title(f'Importancia de las Características - {month_name}')
    plt.show()

if __name__ == '__main__':
    features = [
        "pickup_weekday", "pickup_hour", 'work_hours', "pickup_minute",
        "passenger_count", 'trip_distance', 'trip_time', 'trip_speed',
        "PULocationID", "DOLocationID", "RatecodeID"
    ]

    jan_importances = [0.1, 0.15, 0.05, 0.2, 0.1, 0.2, 0.1, 0.1, 0.05, 0.05, 0.05]
    feb_importances = [0.12, 0.13, 0.05, 0.18, 0.1, 0.22, 0.08, 0.07, 0.03, 0.02, 0.05]

    plot_feature_importances(jan_importances, features, 'Enero')
    plot_feature_importances(feb_importances, features, 'Febrero')
