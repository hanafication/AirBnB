import pandas as pd
import os
import time
import datetime

def to_pandas(var):
    ''''
    Convert scraped data to dataframe and save as csv
    var = list of scraped data
    '''
    dataframe = pd.DataFrame()
    for dim in var:
        df_dic = pd.DataFrame.from_records(dim)
        print(df_dic)
        dataframe = dataframe.append(df_dic, ignore_index=True)
    dataframe = dataframe.drop_duplicates()
    return dataframe

def to_csv(loc, dataframe):
    '''
    Export to csv based on time exporting
    '''
    path = 'C:/Users/Rahadian/PycharmProjects/AirBnB/exported_dataset'
    #path_ubuntu = '/home/expiatio/PycharmProjects/AirBnB/exported_dataset'
    ts = time.time()
    timenow = datetime.datetime.fromtimestamp(ts).strftime('%Y%m%d%H%M%S_%f')

    return dataframe.to_csv(os.path.join(path, timenow+'-'+loc+'.csv'),
                            index=False, sep=';')