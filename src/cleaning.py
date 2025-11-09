import numpy as np
from scipy import stats

def handle_missing(df, cols):
    for col in cols:
        df[col].fillna(df[col].median(), inplace=True)
    return df

def remove_outliers(df, cols):
    z_scores = np.abs(stats.zscore(df[cols], nan_policy='omit'))
    mask = (z_scores <= 3).all(axis=1)
    return df[mask]
