import pandas as pd
from sqlalchemy import create_engine, inspect
import json

# Load database configuration from the config file
def load_config():
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except Exception as e:
        print(f"Failed to load config: {e}")
        return {}

config = load_config()

# Assemble the DATABASE_URI from the config details
user = config.get('user')
password = config.get('password')
host = config.get('host')
dbname = config.get('dbname')
port = config.get('port')
DATABASE_URI = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"

# Create the database engine
engine = create_engine(DATABASE_URI)

# Function to create the table if it doesn't exist
def create_table(table_name):
    inspector = inspect(engine)
    if not inspector.has_table(table_name):
        df = pd.DataFrame({
            'economy_gdp_per_capita_': pd.Series(dtype='float'),
            'social_support': pd.Series(dtype='float'),
            'health_life_expectancy_': pd.Series(dtype='float'),
            'freedom': pd.Series(dtype='float'),
            'trust_government_corruption_': pd.Series(dtype='float'),
            'generosity': pd.Series(dtype='float'),
            'year': pd.Series(dtype='float'),
            'continent_africa': pd.Series(dtype='integer'),
            'continent_asia': pd.Series(dtype='integer'),
            'continent_europe': pd.Series(dtype='integer'),
            'continent_north_america': pd.Series(dtype='integer'),
            'continent_oceania': pd.Series(dtype='integer'),
            'continent_south_america': pd.Series(dtype='integer'),
            'happiness_score': pd.Series(dtype='float'),
            'prediction': pd.Series(dtype='float')
        })
        df.to_sql(table_name, engine, if_exists='replace', index=False)
    else:
        print(f"Table '{table_name}' already exists.")

# Function to load data into the table
def load_data(df, table_name):
    df.to_sql(table_name, con=engine, if_exists='append', index=False)
