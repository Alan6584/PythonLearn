#!/bin/sh
find $1 -name "*.pcm" >list

for file in `cat list`; do
    echo $file
    wav_name=`echo $file|cut -d'.' -f1`;
    echo $wav_name.wav

    ffmpeg  -f s16le -y -ar 44100 -ac 1 -i $file  "$wav_name.wav"
done

rm -f list