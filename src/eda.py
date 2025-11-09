import matplotlib.pyplot as plt
import seaborn as sns

def plot_time_series(df, x_col, y_col, title=''):
    plt.figure(figsize=(12,5))
    sns.lineplot(data=df, x=x_col, y=y_col)
    plt.title(title)
    plt.show()

def plot_correlation(df, cols):
    plt.figure(figsize=(10,6))
    sns.heatmap(df[cols].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.show()
