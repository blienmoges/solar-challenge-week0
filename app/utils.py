import pandas as pd


def load_data():
    benin = pd.read_csv('../data/benin-malanville.csv')
    sierraleone = pd.read_csv('../data/sierraleone-bumbuna.csv')
    togo = pd.read_csv('../data/togo-dapaong_qc.csv')
    
    benin['Country'] = 'Benin'
    sierraleone['Country'] = 'Sierra Leone'
    togo['Country'] = 'Togo'
    
    df_all = pd.concat([benin, sierraleone, togo], ignore_index=True)
    return df_all

def filter_countries(df, selected_countries):
    return df[df['Country'].isin(selected_countries)]


def top_regions(df, n=5):
    if 'site' in df.columns:
        return df.groupby(['Country','site'])['GHI'].mean().sort_values(ascending=False).head(n)
    return df.groupby('Country')['GHI'].mean().sort_values(ascending=False).head(n)
