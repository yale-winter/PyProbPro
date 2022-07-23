# -*- coding: utf-8 -*-
"""
@author: yale-winter
"""
import os
import pandas as pd
def import_data_table(file_name, read_rows):
    '''
    import timeline from .csv file
    '''
    df = None
    try:
        print('  *        *    *  *** pyprobpro ***  *    *        *      ')
        print('* * * * * * * * * Python Problem Provider * * * * * * * * *')
        __location__ = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__)))
        sheet_url = os.path.join(__location__, file_name)
        df = pd.read_csv(sheet_url,nrows=read_rows, on_bad_lines='skip')
        df.dropna()
    except:
        print('Error loading data from local .csv')
    return df
def set_up():
    '''
    set up the dataframe
    '''
    df = import_data_table('Problems.csv', 1000)
    return df
df = set_up()
def __main__():
    '''
    describe to the problem solver how to use basic commands
    '''
    if isinstance(df, pd.DataFrame):
        print('pyprobpro successfully loaded - Use pyprobpro.commands.start()',
              '\npyprobpro.commands.hard(), or pyprobpro.commands.problem(x)',
              'for a new problem.')
        print('Or pyprobpro.commands.details() to show problem set and best average time.')
