import pyarrow as pa
import pyarrow.parquet as pq
import os
from datetime import datetime as dt


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

# MANUALLY DEFINE THE CREDENTIALS
# Set the environment variable to the location of the mounted key. json
# This will tell pyarrow where our credentials are
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/home/src/mage-project-74715-3584748e4a25.json"

# Define the bucket, project, and table  
bucket_name = 'mage-zoomcamp-ndu'
project_id = 'mage-project-74715'
table_name = 'nyc_taxi_data'          

root_path = f'{bucket_name}/{table_name}'

@data_exporter
def export_data(data, *args, **kwargs):
    # Check if the data is a list
    if isinstance(data, list):
        # If data is a list, assume it contains pandas DataFrames
        if len(data) == 0:
            raise ValueError("Input 'data' list is empty.")
        
        # Loop through the list and add the 'lpep_pickup_date' to each DataFrame
        for i, df in enumerate(data):
            df['lpep_pickup_date'] = pd.to_datetime(df['lpep_pickup_datetime']).dt.date
            data[i] = df
        
        # Concatenate the DataFrames within the list
        data = pd.concat(data, ignore_index=True)
        
    # Check if the data is a pandas DataFrame
    elif not isinstance(data, pd.DataFrame):
        raise ValueError("Input 'data' must be a pandas DataFrame.")

    # Convert the 'lpep_pickup_datetime' column to the correct format
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime']).dt.date

    # Define the pyarrow table and read the DataFrame into it
    table = pa.Table.from_pandas(data)

    # Define file system - the Google Cloud object that is going to authorize using the environmental variable automatically
    gcs = pa.fs.GcsFileSystem()

    # Write to the dataset using a parquet function, with partitioning
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],  # Needs to be a list
        filesystem=gcs
    )
