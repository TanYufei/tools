# 小工具（tools）

标签（空格分隔）： tools

---

## 1. wer(Word Error Rate)

- wer/asr_wer.py  
- wer/score_it.py
 
![wer](http://img.blog.csdn.net/20170224105020653?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvcXVoZURpZWdvb28=/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

## 2. 文本转换

- atc.py  将输入文本转为全中文文本

```python
    text = '-今天-112.5天4-6气.123.45'
    #2种数字转化方式
    print(text2allchinese(text))     #今天负一百一十二点五天四负六气一百二十三点四五
    print(text2allchinese(text, 2))  #今天负一一二点五天四负六气一二三点四五
```
## 3. 数字（带逗号，）转中文

- num2zh.py

```python
print num2zh('$10.12356888')               #十点一二三五六八八八
print num2zh('2,000,000,000,000,200.12')   #二千兆零二百点一二
print num2zh('2,001.1')                    #二千零一点一
```

## 4. 音频分割

- split_audio.py

```python
    import pydub
    from pydub.silence import split_on_silence
    song1 = pydub.AudioSegment.from_wav('/home/tyf/gits/tongdunwav/corpus1.wav')
    segments = split_on_silence(song1, min_silence_len=500, silence_thresh=-45)
```

