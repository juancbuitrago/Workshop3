import pandas as pd

def select_features(df):
    df = df.drop(columns=['country', 'lower_confidence_interval', 'upper_confidence_interval', 'happiness_rank'], axis=1)
    return df

def continent_dummies(df):
    df = pd.get_dummies(df, columns=['continent'], drop_first=False)
    df.columns = df.columns.str.replace(r'[^A-Za-z0-9]+', '_', regex=True).str.lower()
    df['continent_africa'] = df['continent_africa'].astype(int)
    df['continent_asia'] = df['continent_asia'].astype(int)
    df['continent_europe'] = df['continent_europe'].astype(int)
    df['continent_north_america'] = df['continent_north_america'].astype(int)
    df['continent_oceania'] = df['continent_oceania'].astype(int)
    df['continent_south_america'] = df['continent_south_america'].astype(int)
    return df
