#!/bin/bash

#如果中途发生错误就退出
set -e

#这个是指定NDK的路径，需要进行配置
#NDK=$HOME/Library/android/sdk/ndk-bundle
#NDK=$HOME/Desktop/ffmpeg/sdk/android-ndk-r14b/ndk-bundle
NDK=$HOME/Desktop/ffmpeg/sdk/android-ndk-r10e
#指定系统编译的路径
PLATFORMS=$NDK/platforms/android-16/arch-

#进行config的函数
function build_one
{
./configure \
    --prefix=$PREFIX \
    --disable-shared \
    --enable-static \
    --enable-small \
    --enable-gpl \
    --disable-stripping \
    --disable-debug \
    --disable-ffmpeg \
    --disable-ffplay \
    --disable-ffprobe \
    --disable-ffserver \
    --disable-avdevice \
    --disable-devices \
    --disable-symver \
    --disable-doc \
    --disable-decoders \
    --disable-encoders \
    --disable-parsers \
    --disable-protocols \
    --disable-hwaccels \
    --enable-protocol=file \
    --enable-parser=aac \
    --enable-parser=mpegaudio \
    --disable-devices \
    --enable-decoder=aac \
    --enable-decoder=pcm_s16le \
    --enable-decoder=pcm_f32le \
    --enable-encoder=aac \
    --enable-encoder=pcm_s16le \
    --enable-encoder=pcm_f32le \
    --disable-bsfs \
    --enable-bsf=aac_adtstoasc \
    --enable-bsf=hevc_mp4toannexb \
    --enable-bsf=mpeg4_unpack_bframes \
    --disable-muxers \
    --enable-muxer=mp4 \
    --enable-muxer=wav \
    --enable-muxer=ipod \
    --enable-muxer=flv  \
    --enable-muxer=avi  \
    --enable-muxer=mov  \
    --enable-muxer=matroska \
    --disable-demuxers \
    --enable-demuxer=h264 \
    --enable-demuxer=mov \
    --enable-demuxer=aac \
    --enable-demuxer=wav \
    --enable-demuxer=flv \
    --enable-demuxer=avi \
    --enable-demuxer=mov \
    --enable-demuxer=matroska \
    --disable-filters \
    --enable-filter=aresample \
    --enable-filter=transpose \
    --enable-filter=crop \
    --enable-filter=vflip \
    --enable-filter=hflip \
    --enable-runtime-cpudetect \
    --cross-prefix=$CROSS_PREFIX \
    --target-os=linux \
    --cpu=$CPU \
    --arch=$ARCH \
    --enable-cross-compile \
    --sysroot=$SYSROOT \
    --extra-cflags="-O3 -ffast-math -fPIC $ADDI_CFLAGS" \
    --extra-cxxflags="-O3 -ffast-math -fPIC $ADDI_CXXFLAGS"\
    --extra-ldflags="$ADDI_LDFLAGS" \
    $ADDITIONAL_CONFIGURE_FLAG

make clean
make
make install
}

#如果即 --enable-share 又 --enable-static 会出现 ff_log2_tab 重复定义的问题
function all_static_to_share
{
${CROSS_PREFIX}ld \
    -rpath-link=$SYSROOT/usr/lib \
    -L$SYSROOT/usr/lib \
    -soname libffmpeg.so \
    -shared -nostdlib  \
    -Bsymbolic \
    --whole-archive --no-undefined \
    -o $PREFIX/libffmpeg.so \
    libavcodec/libavcodec.a \
    libavfilter/libavfilter.a \
    libswresample/libswresample.a \
    libavformat/libavformat.a \
    libavutil/libavutil.a \
    libswscale/libswscale.a \
    libpostproc/libpostproc.a \
    -lc -lm -lz -ldl -llog \
    $CROSS_LIB/4.9/libgcc.a
#$CROSS_LIB/4.9.x/libgcc.a
}

function build_ffmpeg_exe
{
${CROSS_PREFIX}gcc-4.9 -I $(pwd) --sysroot=$SYSROOT \
    -pie -fPIE \
    ffmpeg.c ffmpeg_filter.c cmdutils.c ffmpeg_opt.c -o ${PREFIX}/ffmpeg \
    libavformat/libavformat.a \
    libavcodec/libavcodec.a \
    libavfilter/libavfilter.a \
    libpostproc/libpostproc.a \
    libswresample/libswresample.a \
    libswscale/libswscale.a \
    libavutil/libavutil.a \
    -lm -lz
}

if true; then
###########################
# x86平台的编译
###########################
CPU=x86
ARCH=x86
#最后的安装路径
PREFIX=$(pwd)/build_android/x86
SYSROOT=$PLATFORMS$ARCH
TOOLCHAIN=$NDK/toolchains/x86-4.9/prebuilt/darwin-x86_64
CROSS_PREFIX=$TOOLCHAIN/bin/i686-linux-android-
CROSS_LIB=$TOOLCHAIN/lib/gcc/i686-linux-android
ADDI_CFLAGS="-march=atom -msse3 -mfpmath=sse"
ADDI_CXXFLAGS="-march=atom -msse3 -mfpmath=sse"
ADDI_LDFLAGS=""
ADDITIONAL_CONFIGURE_FLAG="--arch=x86 --disable-amd3dnow --disable-avx"
echo "start build static"
echo ${CROSS_PREFIX}
echo ${SYSROOT}
echo ${PREFIX}
echo ${CROSS_LIB}
build_one
echo "start all_static_to_share"
all_static_to_share
echo "start build_ffmpeg_exe"
build_ffmpeg_exe
fi

if true; then
###########################
# armv7平台的编译
###########################
CPU=cortex-a8
ARCH=arm
#最后的安装路径
PREFIX=$(pwd)/android/armv7-a
SYSROOT=$PLATFORMS$ARCH
TOOLCHAIN=$NDK/toolchains/arm-linux-androideabi-4.9/prebuilt/darwin-x86_64
CROSS_PREFIX=$TOOLCHAIN/bin/arm-linux-androideabi-
CROSS_LIB=$TOOLCHAIN/lib/gcc/arm-linux-androideabi
ADDI_CFLAGS="-march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -mcpu=cortex-a8"
ADDI_CXXFLAGS="-march=armv7-a -mfloat-abi=softfp -mfpu=vfpv3-d16 -mcpu=cortex-a8"
ADDI_LDFLAGS="-Wl,--fix-cortex-a8"
ADDITIONAL_CONFIGURE_FLAG="--arch=arm --enable-neon --enable-asm --enable-inline-asm"
build_one
all_static_to_share
build_ffmpeg_exe
fi
