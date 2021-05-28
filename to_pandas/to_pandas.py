import pandas as pd
import time
def to_pandas(var):
    ''''
    Convert scraped data to dataframe and save as csv
    var = list of scraped data
    '''
    dataframe = pd.DataFrame()
    for dim in var:
        df_dic = pd.DataFrame.from_records(dim)
        dataframe.append(df_dic, ignore_index=True)

    return dataframe

def to_csv(loc, dataframe):
    '''
    Export to csv based on time exporting
    '''
    path = 'C:\Users\Rahadian\PycharmProjects\AirBnB\exported_dataset'
    return dataframe.to_csv(path=exported_dataset)