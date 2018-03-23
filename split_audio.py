# -*- coding: utf-8 -*-
# @Time    : 11/24/17 1:42 PM
# @Author  : tyf_aicyber
# @Site    : 
# @File    : split_audio.py
# @Software: PyCharm

import pydub
from pydub.silence import split_on_silence
from tqdm import tqdm

song1 = pydub.AudioSegment.from_wav('/home/tyf/gits/tongdunwav/corpus1.wav')

segments = split_on_silence(song1, min_silence_len=500, silence_thresh=-45)

for i, segment in tqdm(enumerate(segments)):
    segment.export('/home/tyf/gits/tongdunwav/a/%04d.wav'%i, format='wav')
    # words[0].export('text.wav',format='wav')
# b = song1[1000]

print song1.channels
print len(segments)
