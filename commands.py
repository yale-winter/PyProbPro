# -*- coding: utf-8 -*-
"""
@author: yale-winter
"""
import glob
import os
import time
import pandas as pd
from . problemset import provide_problem
from . loader import df, set_problem
def details():
    '''
    Show problem set details
    '''
    print('* * * * * * * * * Problem Set Details * * * * * * * * * * *\n')
    df2 = df.sort_values(by=['Time', 'Problem Description'], ascending = False)
    df2 = df2.loc[df2['Time'] > 0, ['Problem Description', 'Time']]
    print(df2)
    print('\nAverage best time:', int(100*sum(df2['Time'])/len(df2['Time']))/100,'min',
          '\nTotal time:', sum(df2['Time']),'min','\nProblems:', len(df2['Time']))
def hard():
    '''
    Produce a 'hard' problem
    '''
    start(True)
def start(hard_mode= False):
    '''
    Use this function in console to start problem solving
    '''
    if isinstance(df, pd.DataFrame):
        set_problem(provide_problem(df, -1, hard_mode))
def problem(j):
    '''
    Use this function to answer a specific ID question
    '''
    if isinstance(df, pd.DataFrame):
        set_problem(provide_problem(df, j))
def show():
    '''
    Show current problem
    '''
    list_of_files = glob.glob('*.txt')
    latest_file = max(list_of_files, key=os.path.getctime)
    with open(latest_file, "r", encoding="utf-8") as file1:
        file_list = file1.readlines()
        for i in enumerate(len(file_list)):
            print(file_list[i])
def done():
    '''
    Use this function in console when done
    '''
    list_of_files = glob.glob('*.txt')
    latest_file = max(list_of_files, key=os.path.getctime)
    with open(latest_file, "r", encoding="utf-8") as file1:
        file_list = file1.readlines()
    last_time = int(file_list[-1])
    end_time = int(((time.time() - float(file_list[1]))/60))
    print('minutes taken', end_time)
    result_string = ''
    if end_time < last_time:
        result_string = ('New fastest time: ' + str(end_time)
        + ' minutes. Congratulations, this was ' + str(last_time - end_time)
        + ' minutes faster')
    else:
        result_string = ('New time: ' + str(end_time) + ' minutes. This was '
        + str(end_time - last_time) + ' minutes slower than your best')
    print(result_string)
    with open(latest_file, "a", encoding="utf-8") as file1:
        file1.write(result_string +'\n')
        file1.write(str(end_time) +'\n')
