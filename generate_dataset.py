import os
import cv2

input_dir = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/train/'
out_dir = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/withoutAP/'

# 将视频转换成每帧图片
def video2img(input_dir, out_dir):
    video_num = out_dir[-5:-1]
    print(video_num)
    vc = cv2.VideoCapture(input_dir + 'train_%s.mp4' % video_num)  # 读入视频文件

    # if vc.isOpened():  # 判断是否正常打开
    #     rval, frame = vc.read()
    # else:
    #     rval = False

    timeF = 1  # 视频帧计数间隔频率

    num = 0
    while True:  # 循环读取视频帧
        rval, frame = vc.read()
        if not rval:
            break
        # if (n % timeF == 0):  # 每隔timeF帧进行存储操作
        num += 1
        frame = cv2.resize(frame, (64, 64), interpolation=cv2.INTER_AREA) # resize
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(out_dir + '{}.png'.format(num), frame)  # 存储为图像
    vc.release()

if not os.path.exists(out_dir):
        os.mkdir(out_dir)
data_list = os.listdir(input_dir)
folder_name = 0
for file in data_list:
    folder_name += 1
    opt_dir = out_dir + '%04d/' % folder_name
    if not os.path.exists(opt_dir):
        os.mkdir(opt_dir)
    video2img(input_dir, opt_dir)
    print('video clip %d is processed.' % folder_name)

####test1####
# os.system('python scripts/demo_inference.py '
#           '--cfg C:/Users/Abali/Projects/AlphaPose_n/AP/configs/coco/resnet/256x192_res50_lr1e-3_2x.yaml '
#           '--checkpoint C:/Users/Abali/Projects/AlphaPose_n/AP/pretrained_models/fast_res50_256x192.pth '
#           '--video %strain_0035.mp4 '
#           '--outdir test/val/ '
#           '--save_video '
#           %input_dir
#           )
# if not os.path.exists():
#     os.mkdir('')
# for file in data_list:
#     file = input_dir + file
#     os.system('python scripts/demo_inference.py '
#               '--cfg C:/Users/Abali/Projects/AlphaPose_n/AP/configs/coco/resnet/256x192_res50_lr1e-3_2x.yaml '
#               '--checkpoint C:/Users/Abali/Projects/AlphaPose_n/AP/pretrained_models/fast_res50_256x192.pth '
#               '--video %s '
#               '--outdir test/val/ '
#               '--save_video '
#               %file
#               )

###test2###
# os.system('ffmpeg -i {}'.format(input_dir) + 'train_0004.mp4 -r 30 -s 64,64 {}'.format(out_dir) + '%03d.png')
