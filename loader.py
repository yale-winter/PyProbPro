# -*- coding: utf-8 -*-
"""
@author: yale-winter
"""
import pandas as pd
import os

def set_problem(x):
    pass


def import_data_table(file_name, read_rows, col_names):
    '''
    Import timeline from .csv file
    '''
    df = None
    try:
        print('  *        *    *  *** PyProbPro ***  *    *        *      ')
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
    col_names = ['Problem Description', 'Test Cases', 'Time']
    df = import_data_table('Problems.csv', 1000, col_names)
    return df

startT = 0
prob_choice = -1
df = set_up()
if type(df) == pd.DataFrame:
    print('PyProbPro successfully loaded - Use start(), hard(), or problem(x) for a new problem.')
    print('Or details() to show problem set and best average time.')