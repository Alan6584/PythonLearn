# -*- coding: utf-8 -*-
# @Time    : 2018-08-10 16:45
# @Author  : jianjun.wang
# @FileName: layout_r2l.py
import os
import sys
import re
import wave
import numpy as np
import pylab as plt



def read_wav_data(filename):
  '''
  读取一个wav文件，返回声音信号的时域谱矩阵和播放时间
  '''
  wav = wave.open(filename,"rb") # 打开一个wav格式的声音文件流
  num_frame = wav.getnframes() # 获取帧数
  num_channel=wav.getnchannels() # 获取声道数
  framerate=wav.getframerate() # 获取帧速率
  num_sample_width=wav.getsampwidth() # 获取实例的比特宽度，即每一帧的字节数
  str_data = wav.readframes(num_frame) # 读取全部的帧
  wav.close() # 关闭流
  wave_data = np.fromstring(str_data, dtype = np.short) # 将声音文件数据转换为数组矩阵形式
  wave_data.shape = -1, num_channel # 按照声道数将数组整形，单声道时候是一列数组，双声道时候是两列的矩阵
  wave_data = wave_data.T # 将矩阵转置
  wave_data = wave_data 
  return wave_data, framerate 

   
def wav_show(wave_data, fs): # 显示出来声音波形
  time = np.arange(0, len(wave_data)) * (1.0/fs)  # 计算声音的播放时间，单位为秒
  # 画声音波形
  plt.plot(time, wave_data)  
  plt.show()  


if __name__ == '__main__':
    '''
        使用说明：目前只针对.xml 对 convert_contents 中匹配的内容做修改
        运行环境：Python 2.7
        执行：python layout_r2l.py <要转换的目录>
    '''
    if len(sys.argv) == 1:
        raw_input("[error] need root dir")
        sys.exit(-1)
    wav_path = sys.argv[1]
    print "wav_path = ", wav_path

    wave_data, fs = read_wav_data(wav_path)  
    wav_show(wave_data[0],fs)
    wav_show(wave_data[1],fs)  # 如果是双声道则保留这一行，否则删掉这一行
