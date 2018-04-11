# -*- coding: utf-8 -*-
from __future__ import division

import sys
import pandas as pd
import numpy as np


def isMatch(res):
    # return [v for v in res if v > 50]
    return res.values > 50


def main():
    df = pd.read_csv('./res.csv')
    print 'total count :', len(df)
    print df

    math = df[['name', 'math']]
    # print math

    print
    test = df[(df['physics'] > 50) & (df['english'] > 80)]
    print test

    print
    res = df[isMatch(df['physics'])]
    print res


    print '--------------'
    for index, row in df.iterrows():
        print row['name'], row['physics']

if __name__ == '__main__':
    main()
