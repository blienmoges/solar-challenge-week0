from src.data_loader import load_data
from src.cleaning import handle_missing, remove_outliers
from src.eda import plot_time_series, plot_correlation

# Load Sierra Leone dataset
df = load_data('data/sierra_leone.csv')

# Define numeric columns
numeric_cols = ['GHI','DNI','DHI','ModA','ModB','WS','WSgust']

# Clean data
df = handle_missing(df, numeric_cols)
df = remove_outliers(df, numeric_cols)


plot_time_series(df, 'Timestamp', 'GHI', 'GHI Over Time - Sierra Leone')
plot_correlation(df, numeric_cols)
