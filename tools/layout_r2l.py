# -*- coding: utf-8 -*-
# @Time    : 2018-05-02 10:28
# @Author  : jianjun.wang
# @FileName: layout_r2l.py
import os
import sys
import re

files_cnt = 0
handled_lines_cnt = 0

convertfiletypes = [
  ".xml"
] 

convert_contents = [
    "layout_alignParentLeft",  "layout_alignParentStart", 
    "layout_alignParentRight", "layout_alignParentEnd", 
    "layout_marginLeft",       "layout_marginStart",
    "layout_marginRight",      "layout_marginEnd",
    "drawableLeft",            "drawableStart",
    "drawableRight",           "drawableEnd",
    "layout_toLeftOf",         "layout_toStartOf",
    "layout_toRightOf",        "layout_toEndOf",
    "paddingLeft",             "paddingStart",
    "paddingRight",            "paddingEnd" 
]

def check_need_convert(filename):
    for filetype in convertfiletypes:
        if filename.lower().endswith(filetype):
            return True
    return False

def other_handle(line):
    global handled_lines_cnt
    if "gravity=" in line:
        line = re.sub('left', 'start', line)
        line = re.sub('right', 'end', line)
        handled_lines_cnt+=1
    return line

def convert_line_r2l(line):
    global handled_lines_cnt
    for i in range(0, len(convert_contents), 2):
        if convert_contents[i] in line:
            handled_lines_cnt+=1
            line = re.sub(convert_contents[i], convert_contents[(i + 1)], line)
            return line
    return other_handle(line)

def convert_layout_file(file_path):
    global files_cnt,handled_lines_cnt
    print file_path

    if not os.path.isfile(file_path):
        return

    files_cnt+=1
    handled_lines_cnt = 0

    fr = open(file_path, 'r')
    all_lines = fr.readlines()

    temp_lines = []
    for line in all_lines:
        temp_lines.append(convert_line_r2l(line))
    fr.close()

    fp = open(file_path, 'w')
    for new_line in temp_lines:
        fp.write(new_line)
    fp.close()    

    print "the file matched lines cnt:",handled_lines_cnt

def convert_dir(root_dir):
    if os.path.exists(root_dir) == False:
        print "[error] dir:",root_dir,"do not exit"
        return
    if os.path.isfile(root_dir):
        convert_layout_file(root_dir)
    else:
        print "work in",convertdir
        for root, dirs, files in os.walk(root_dir):
            for f in files:
                if check_need_convert(f):
                    filename = os.path.join(root, f)
                    try:
                        convert_layout_file(filename)
                    except Exception, e:
                        print "Exception",filename,e
    print "finish files_cnt:",files_cnt

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
