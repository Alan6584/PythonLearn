# -*- coding: utf-8 -*-
# @Time    : 2018-04-11 09：58
# @Author  : jianjun.wang
# @FileName: devices.py

import sys
import getopt
import pandas as pd

     

def analysic(flie_name, manufacturer):
    
    file = flie_name;
    df = pd.read_csv(file)
    print 'total count :', len(df)

    print 'df :', df
    sorted_df = df.sort_values(by='user_count', ascending=False)
    print '=============================='
    print 'sorted_df :', sorted_df

    user_sum = sorted_df['user_count'].sum()
    print 'user_sum :', user_sum

    target_df = sorted_df[sorted_df['devices'].str.contains('samsung', case=False)]
    print 'target_df :', target_df
    

def main(argv):

    file=''
    manufacturer=''

    try:
        opts, args = getopt.getopt(argv, "hf:m:")
    except getopt.GetoptError:
        print('Error: devices.py -f <file_name> -m <manufacturer>')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h"):
            print('devices.py -f <file_name> -m <manufacturer>')    
            sys.exit()
        elif opt in ("-f"):
            file = arg
            print 'file :', file
        elif opt in ("-m"):
            manufacturer = arg
            print 'manufacturer :', manufacturer

    analysic(file, manufacturer)

if __name__ == '__main__':
    main(sys.argv[1:])
