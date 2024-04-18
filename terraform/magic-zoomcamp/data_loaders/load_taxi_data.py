import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Load data from API for the final quarter of 2020 (months 10, 11, 12)
    """
    base_url = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download'
    urls = [
        f'{base_url}/green/green_tripdata_2020-{month:02d}.csv.gz'
        for month in range(10, 13)
    ]
    
    # Define data types
    taxi_dtypes = {
        'VendorID': 'Int64',
        'store_and_fwd_flag': 'str',
        'RatecodeID': 'Int64',
        'PULocationID': 'Int64',
        'DOLocationID': 'Int64',
        'passenger_count': 'Int64',
        'trip_distance': 'float64',
        'fare_amount': 'float64',
        'extra': 'float64',
        'mta_tax': 'float64',
        'tip_amount': 'float64',
        'tolls_amount': 'float64',
        'ehail_fee': 'float64',
        'improvement_surcharge': 'float64',
        'total_amount': 'float64',
        'payment_type': 'float64',
        'trip_type': 'float64',
        'congestion_surcharge': 'float64'
    }
    
    # Define parse dates
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    
    # Load data for each month and concatenate
    data = []
    for url in urls:
        df = pd.read_csv(url, sep=',', compression='gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
        # df.drop(columns=['__index_level_0__'], inplace=True) 
        data.append(df)
    if len(data) == 0:
        raise ValueError("No data loaded.") 
    
    return data
    return pd.concat(data, ignore_index=True)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'