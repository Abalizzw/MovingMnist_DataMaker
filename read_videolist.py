import shutil

input_dir = 'D:/M1/JAAD_DATA/JAAD_clips/'
target_dir = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/clips/'

# with open('D:/M1/JAAD_DATA/JAAD_clips/优选视频/list.txt', 'r') as f:
#     my_data = f.readlines() #txt中所有字符串读入data，得到的是一个list
#     # 对list中的数据做分隔和类型转换
#     for line in my_data:
#         file_name = input_dir + 'video_' + line.strip() + '.mp4'
#         target_file = target_dir + 'train_' + line.strip() + '.mp4'
#         shutil.copy2(file_name, target_file)
#
# print('Copy Done.')

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import cv2

def get_source_info_opencv(source_name):
    return_value = 0
    try:
        cap = cv2.VideoCapture(source_name)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        fps = cap.get(cv2.CAP_PROP_FPS)
        num_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)
        print("width:{} \nheight:{} \nfps:{} \nnum_frames:{}".format(width, height, fps, num_frames))
    except (OSError, TypeError, ValueError, KeyError, SyntaxError) as e:
        print("init_source:{} error. {}\n".format(source_name, str(e)))
        return_value = -1
    return return_value

def main():
    source_name = 'C:/Users/Abalizzw/Projects/AlphaPose_n/AP/test/val/train_0004.mp4'
    get_source_info_opencv(source_name)

if __name__ == "__main__":
    main()
