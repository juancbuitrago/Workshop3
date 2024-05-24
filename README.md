# Workshop3
## Structure ##
<div style="background-color: #000000;font-size: 14px ;color: #FFFFFF; padding: 10px; border: 1px solid #ccc">
    <pre>
        .
        ├── .gitignore
        ├── config.json
        ├── consumer.py
        ├── db.py
        ├── docker-compose.yml
        ├── functions.py
        ├── Metrics.ipynb
        ├── producer.py
        ├── README.md
        ├── data
        │   ├── 2015.csv
        │   ├── 2016.csv
        │   ├── 2017.csv
        │   ├── 2018.csv
        │   ├── 2019.csv
        │   ├── X_test.csv
        │   └── y_test.csv
        ├── docs
        │   └── documentation.pdf
        ├── models
        │   └── randomForest.pkl
        └── notebooks
            └── EDA_001.ipynb

</div>

## Overview ##
_.This workshop is an exercise on how to train a model to predict the happiness of people depending on different variables using datasets from different years and with different structures, so we will have to make different transformations to finally make a merge between these datasets having in all the normalized information._
_Besides we will need to dig into the variables of this one to try to get the best possible R^2._
_Finally, we will stream the data through Kafka to a postgresql database._

_Also, *[Detailed Documentation](https://github.com/juancbuitrago/Workshop3/blob/main/docs/documentation.pdf)* is available that covers everything from data selection to the final visualizations_

## Table of Contents ##
- [Requirements](#requirements)
- [Setup](#setup)
- [Data Transformation](#data-transformation)
- [Data Analysis](#exploratory-data-analysis)

## Requirements <a name="requirements"></a> ##
- Create a folder and clone this github repository
- Python 3.9
- Kafka
- Docker
- PostgreSQL
In this section you need to create a database called happiness_predictions (or you can renamed it but you should change the name of the database in the rest of the code.)
- Jupyter Notebook
- JSON credentials file ("config_EDA.json") with this format:
 
```
{
    "user": your user,
    "password": your password,
    "host": "localhost",
    "dbname": your db name,
    "port": your port
}

``` 

- Libraries that we install with the requirements.txt (You need to go to the terminal and run: 'pip install -r requirements.txt'):
    - pandas
    - matplotlib
    - numpy
    - SQLalchemy
    - psycopg2-binary
    - seaborn
    - kafka-python
    - scikit-learn
    - joblib

## Setup <a name="setup"></a> ##
_First of all, 
ensure you have the following programs installed with which the entire project procedure is carried out:_

   - **[Python](https://www.python.org)**
   - **[PostgreSQL](https://www.postgresql.org/download/)**
   - **[PowerBI](https://powerbi.microsoft.com/es-es/downloads/)**
   - **[VS Code](https://code.visualstudio.com/download)** or **[Jupyter](https://jupyter.org/install)**
   - **[Docker Desktop](https://www.docker.com/products/docker-desktop/)**

If you already have all the requirements, you only need to run Docker Desktop and then:
1. Run all the notebook called EDA_001
2. Go to the root of the repository
3. Run `docker-compose up`
4. Run producer.py
5. Run consumer.py
6. Go to the database and refresh to see how the data is streaming
7. (Optional) Run the Metrics notebook.

## General EDA <a name="data-transformation"></a> ##

 _This process was carried out in **[EDA_001](https://github.com/juancbuitrago/Workshop3/blob/main/notebooks/EDA_001.ipynb)** where the following procedures are being carried out:_

- Identification of the data frames structure
- Identification of columns names
- Identification of data types
- Identification of null data
- Identification of unnecesary columns
- Identification of problems in the data
- Transformations
- Exploratory Data Analysis
- Merge
- Model a features selection
- Some graphics
- Transformations for the model and get better R^2
 

 # _[Clone me](https://github.com/juancbuitrago/Workshop3.git) and see how powerful the data can be!_

