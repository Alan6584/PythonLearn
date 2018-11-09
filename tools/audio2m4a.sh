#!/bin/sh
find $1 -name "*.ogg" > list

for file in `cat list`; do
    echo $file
    wav_name=`echo $file|cut -d'.' -f1`;
    echo $wav_name.m4a

    # ffmpeg -i $file  "$wav_name.m4a"
done

rm -f list