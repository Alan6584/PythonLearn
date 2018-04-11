# -*- coding: utf-8 -*-
from __future__ import division

import sys
import pandas as pd
import numpy as np


def isMatch(res):
    # return [v for v in res if v > 50]
    return res.values > 50


def groupby_01(df):
    verdf = df[['version']]
    verdf = verdf.groupby(by=['version']).size()

    print type(verdf)

    verdf = verdf.reset_index(name='times')
    print verdf

    sort = verdf.sort_values(by='version', ascending=False)  
    print sort

    version = sort['version']

    for ver in version:
        print ver

def get_version_list(df):
    # verdf = df.groupby(by=['version']).apply(lambda x: x.sort_values(by='version', ascending=False))
    verdf = df.groupby(by=['version']).size().reset_index().sort_values(by='version', ascending=False).head(2)
    version = verdf['version']
    return version


def analysic_by_version(version):
    print 'current version is : ', version

def main():
    df = pd.read_csv('./res_version.csv')
    print 'total count :', len(df)
    print df

    # groupby_01(df)
    ver_list = get_version_list(df)
    for ver in ver_list:
        analysic_by_version(ver)


if __name__ == '__main__':
    main()
