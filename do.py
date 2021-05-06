import os
import ffmpeg
input_dir = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/clips/'
# input_file = 'D:/M1/JAAD_DATA/JAAD_clips/video_0011.mp4'
# input_file = 'C:/Users/Abali/Projects/AlphaPose_n/AP/examples/res/datasets/test/out.mp4'
save_path = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/train/'


# os.system('ffmpeg -h')

def crop(stream):
    stream = ffmpeg.crop(stream, x=640, y=320, width=640, height=640)

    return stream


def trim(stream, duration, length=2.0):
    start = float(duration) // 2
    end = start + length
    stream = ffmpeg.trim(stream, start=start, end=end)

    return stream


video_list = os.listdir(input_dir)
i = 0
for file in video_list:
    i += 1
    file = input_dir + file
    duration = ffmpeg.probe(file)['format'].get('duration')

    stream = ffmpeg.input(file)
    stream = crop(stream)
    stream = trim(stream, duration)
    stream.output(save_path + 'train_%0.4d.mp4' % i).run()
