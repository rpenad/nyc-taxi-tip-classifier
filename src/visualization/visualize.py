import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_feature_importances(importances, features, month_name):
    feature_importances_df = pd.DataFrame({
        'Feature': features,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x
