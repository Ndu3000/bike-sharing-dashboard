if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

import pandas as pd

@transformer
def transform(data, *args, **kwargs):
    # Remove rows where passenger count is 0 and trip distance is 0
    data = data[(data['passenger_count'] > 0) & (data['trip_distance'] > 0)]

    # Create new column lpep_pickup_date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    # Rename columns from CamelCase to snake_case
    data.rename(columns={
        'VendorID': 'vendor_id',
        'store_and_fwd_flag': 'store_and_fwd_flag',
        'RatecodeID': 'ratecode_id',
        'PULocationID': 'pu_location_id',
        'DOLocationID': 'do_location_id',
        'passenger_count': 'passenger_count',
        'trip_distance': 'trip_distance',
        'fare_amount': 'fare_amount',
        'extra': 'extra',
        'mta_tax': 'mta_tax',
        'tip_amount': 'tip_amount',
        'tolls_amount': 'tolls_amount',
        'ehail_fee': 'ehail_fee',
        'improvement_surcharge': 'improvement_surcharge',
        'total_amount': 'total_amount',
        'payment_type': 'payment_type',
        'trip_type': 'trip_type',
        'congestion_surcharge': 'congestion_surcharge',
        'lpep_pickup_datetime': 'lpep_pickup_datetime',
        'lpep_dropoff_datetime': 'lpep_dropoff_datetime'
    }, inplace=True)

    return data

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    # Assert that vendor_id is one of the existing values
    assert output['vendor_id'].isin(output['vendor_id'].unique()).all(), 'vendor_id contains invalid values'

    # Assert that passenger_count is greater than 0
    assert (output['passenger_count'] > 0).all(), 'passenger_count is not greater than 0'

    # Assert that trip_distance is greater than 0
    assert (output['trip_distance'] > 0).all(), 'trip_distance is not greater than 0'