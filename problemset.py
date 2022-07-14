# -*- coding: utf-8 -*-
"""
@author: yale-winter
"""
import random as rnd
from datetime import datetime
import time


def provide_problem(df, x, hard=False):
    '''
    displays the problem information
    '''
    print('df', df)
    print('x', x)
    print('df.shape[0]', df.shape[0])
    startT = time.time()
    prob_choice2 = rnd.randint(0,len(df)-1)
    the_mean = df['Time'].mean()
    speed_desc = ''
    if hard == True:
        while int(df.loc[prob_choice2]['Time']) < the_mean:
            prob_choice2 = rnd.randint(0,df.shape[0]-1)
            
    #if using problem(x) set problem manually
    if x != -1:
        prob_choice2 = x -1 
        
    print('trying to access problem num', prob_choice2)    
    
    try:
        print('\nProblem', prob_choice2+1)
        print('\n- - - - - - - - - - - - - - - - - -\n')
        print(df.loc[prob_choice2]['Problem Description'])
        print('\n',df.loc[prob_choice2]['Test Cases'])
        speed_desc = '\nBest time for this problem: ' + str(df.loc[prob_choice2]['Time']) + ' min\n\nAverage best time for all problems: ' + str(the_mean) +' min\n'
        print(speed_desc)
        print("Run done() when finished to compare times, Show() to show problem again")
        print('\nDate stamp', datetime.now())
        print('\n- - - - - - - - - - - - - - - - - -\n')
    except:
        print('Problem reading problem data')
        return 'none'
        
    # Write line to file
    fName = str(datetime.now()) + '-Problem-' + str(prob_choice2 + 1) 
    fName = fName.replace('.', '_')
    fName = fName.replace(' ', '_')
    fName = fName.replace(':', '_')
    fName += '.txt'

    with open(fName, 'w') as writefile:
        writefile.write('Problem ' + str(prob_choice2+1)+'\n')
        writefile.write(str(startT) + '\n')
        writefile.write(str(datetime.now()) + '\n')
        writefile.write(str(df.loc[prob_choice2]['Problem Description']) + '\n')
        writefile.write(str(df.loc[prob_choice2]['Test Cases']) + '\n')
        writefile.write(speed_desc)
        writefile.write(str(df.loc[prob_choice2]['Time']) + '\n')

    return prob_choice2