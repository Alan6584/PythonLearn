# -*- coding: utf-8 -*-
from __future__ import division

import sys
import pandas as pd
import numpy as np



def main():
    df = pd.read_csv('/Users/wangjianjun/Alan/me/audio/data/story_list_new.csv')
    # df = pd.read_csv('/Users/wangjianjun/Alan/me/audio/data/story.csv')
    

    # new_df = df.drop_duplicates(['story_link'], keep='first', inplace=False)
    new_df = df.drop_duplicates()

    new_df.to_csv("/Users/wangjianjun/Alan/me/audio/data/story_list_no_repeat_new.csv")

    print "finish!!"

if __name__ == '__main__':
    main()
