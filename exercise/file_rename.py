# -*- coding: utf-8 -*-
# @Time    : 2018-05-02 10:28
# @Author  : jianjun.wang
# @FileName: layout_r2l.py
import os
import sys
import re

def check_need_convert(file):
    return True

def convert_file(file):
    print file
    # s = r'\d{1, 14}'
    # print re.search(s, "a_1213.png").span()
    index = file.rindex('_')
    subStr = file[0:index]
    final_file = subStr + '.png'
    print final_file

    os.rename(file, final_file)


def convert_dir(root_dir):
    if os.path.exists(root_dir) == False:
        print "[error] dir:",root_dir,"do not exit"
        return
    if os.path.isfile(root_dir):
        convert_file(root_dir)
    else:
        print "work in",convertdir
        for root, dirs, files in os.walk(root_dir):
            for f in files:
                if check_need_convert(f):
                    filename = os.path.join(root, f)
                    try:
                        convert_file(filename)
                    except Exception, e:
                        print "Exception",filename,e

if __name__ == '__main__':
    '''
        使用说明：目前只针对.xml 对 convert_contents 中匹配的内容做修改
        运行环境：Python 2.7
        执行：python layout_r2l.py <要转换的目录>
    '''
    if len(sys.argv) == 1:
        raw_input("[error] need root dir")
        sys.exit(-1)
    convertdir = sys.argv[1]
    convert_dir(convertdir)
