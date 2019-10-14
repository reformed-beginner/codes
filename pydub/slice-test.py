# pip install pydub
# install ffmpeg (https://ffmpeg.zeranoe.com/builds/)
# Reference link: https://blog.csdn.net/u014633966/article/details/85244347

#%%
from pydub import AudioSegment
import os

def extract_from_file(filename):
    file_split = filename.split('_')
    chapter = file_split[3]
    volume = file_split[4]
    print(volume)
    print(chapter)
    return (volume, chapter)

def slice_file(base, file, verse_start, verse_end, time_start, time_end):
    audio = AudioSegment.from_mp3(os.path.join(base, file))
    volume,chapter = extract_from_file(file)
    new_file = volume+"_" + chapter + "_" + str(verse_start) + "-" + str(verse_end) + "_" + str(time_start) + "-" + str(time_end) + ".mp3"
    print(new_file)
    audio[time_start*1000:time_end*1000].export("F:/Workspace/Python/pydub-test/mp3_new/" + new_file, format="mp3")


if __name__ == '__main__':
    base = "F:/Workspace/Python/pydub-test/mp3"
    file = 'B01___27_Matthew_____ENGESVN2DA.mp3'
    verse_start = 65
    verse_end = 66
    time_start = 529
    time_end = 542
    #for each in os.listdir(base):
    #print(each)
    slice_file(base, file, verse_start, verse_end, time_start, time_end)


#%%
