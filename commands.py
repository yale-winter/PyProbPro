# -*- coding: utf-8 -*-
"""
@author: yale-winter
"""
import pandas as pd
from . problemset import provide_problem
import glob
import os
from . loader import df, set_problem
import time

def details():
    print('* * * * * * * * * Problem Set Details * * * * * * * * * * *\n')
    df2 = df.sort_values(by=['Time', 'Problem Description'], ascending = False)
    df2 = df2.loc[df2['Time'] > 0, ['Problem Description', 'Time']]
    print(df2)
    print('\nAverage best time:', int(100*sum(df2['Time'])/len(df2['Time']))/100,'min','\nTotal time:', sum(df2['Time']),'min','\nProblems:', len(df2['Time']))


def hard():
    start(True)

def start(hard= False):
    '''
    Use this function in console to start problem solving
    '''
    if type(df) == pd.DataFrame:
        set_problem(provide_problem(df, -1, hard))


def problem(x):
    '''
    Use this function to answer a specific ID question
    '''
    if type(df) == pd.DataFrame:
        set_problem(provide_problem(df, x))


def show():
    list_of_files = glob.glob('*.txt')
    latest_file = max(list_of_files, key=os.path.getctime)
    
    with open(latest_file, "r") as file1:
        fileList = file1.readlines()
        for i in range(len(fileList)):
            print(fileList[i])

def done():
    '''
    Use this function in console when done
    '''

    list_of_files = glob.glob('*.txt')
    latest_file = max(list_of_files, key=os.path.getctime)
    
    with open(latest_file, "r") as file1:
        fileList = file1.readlines()
        
    last_time = int(fileList[-1])
    end_time = int(((time.time() - float(fileList[1]))/60))
    print('minutes taken', end_time)
    
    result_string = ''
    if end_time < last_time:
        result_string = 'New fastest time: ' + str(end_time) + ' minutes. Congratulations, this was ' + str(last_time - end_time) + ' minutes faster'
    else: 
        result_string = 'New time: ' + str(end_time) + ' minutes. This was ' + str(end_time - last_time) + ' minutes slower than your best'
    print(result_string)
    with open(latest_file, "a") as file1:
        file1.write(result_string +'\n')
        file1.write(str(end_time) +'\n')