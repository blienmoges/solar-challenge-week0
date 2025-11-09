from src.data_loader import load_data
from src.cleaning import handle_missing, remove_outliers
from src.eda import plot_time_series, plot_correlation

df = load_data('data/benin.csv')

numeric_cols = ['GHI','DNI','DHI','ModA','ModB','WS','WSgust']
df = handle_missing(df, numeric_cols)
df = remove_outliers(df, numeric_cols)

plot_time_series(df, 'Timestamp', 'GHI', 'GHI Over Time')
plot_correlation(df, numeric_cols)
