import numpy as np
def transform_data(data):
    '''transforming data by creating new feature or modify exsiting one'''
    print("transforming data...")

    # convert bytes to megabyets
    if 'size_in_bytes' in data.columns:
        data['size_in_mb']=data['size_in_bytes'] / (1024 * 1024)

        #log transformation (creat new column)
    if 'value_column' in data.columns:
        data['log_value']=np.loglp(data['value_column'])

        print("data transformation completed")
        return data

