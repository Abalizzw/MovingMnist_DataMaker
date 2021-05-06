import cv2
import os
import numpy as np

npy_save_path = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/mydata_npy/'
valid_dir = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/withoutAP/val/'
train_dir = 'C:/Users/Abali/Projects/AlphaPose_n/AP/test/withoutAP/train/'
frame_size = 64
mode = 'valid'


def countFile(dir):
    tmp = 0
    for item in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, item)):
            tmp += 1
        else:
            tmp += countFile(os.path.join(dir, item))
    return tmp


train_frame_nums = countFile(train_dir)
val_frame_nums = countFile(valid_dir)

# length = 64
# pixel = data[100][0]
# cv2.imshow('npy', pixel)
# print(pixel.shape)
# print(type(pixel))
# print(type(pixel[0][0]))
# cv2.waitKey(0)
# # for i in range(length):
# #     #for j in range(length):
# #     print(pixel[i])


def gen_npz_data(path):
    data_list = os.listdir(path)
    print('reading data...')
    for file in data_list:
        if file[0] == 'c':
            clips = np.load(path + 'clips.npy')
        if file[0] == 'd':
            dims = np.load(path + 'dims.npy')
        if file[0] == 'i':
            input_raw_data = np.load(path + file)

    le = len(clips[0])
    if le == train_frame_nums // 20:
        np.savez(path + 'mydata_train.npz', clips=clips, dims=dims, input_raw_data=input_raw_data)
        print('{}, {}, {} have been saved in {}'.format('clips.npy', 'dims.npy',
                                                        'input_raw_data.npy', 'mydata_train.npz'))
    elif le == val_frame_nums // 20:
        np.savez(path + 'mydata_valid.npz', clips=clips, dims=dims, input_raw_data=input_raw_data)
        print('{}, {}, {} have been saved in {}'.format('clips.npy', 'dims.npy',
                                                        'input_raw_data.npy', 'mydata_valid.npz'))





def gen_npy_clips(frame_nums, save_path):
    dim2 = frame_nums // 20
    clips = np.ndarray(shape=(2, dim2, 2), dtype=np.int32)
    for i in range(clips.shape[0]):
        x = 0 if i == 0 else 10
        for j in range(clips.shape[1]):
            clips[i][j][0] = x
            clips[i][j][1] = 10
            x += 20
    np.save(save_path + 'clips.npy', clips)
    print('clips.npy is saved in path:%s' % save_path)
    print('shape:', clips.shape)
    print('type:', type(clips[0][0][0]))


def gen_npy_dims(frame_size, save_path):
    dims = np.array([[1, frame_size, frame_size]], dtype=np.int32)
    np.save(save_path + 'dims.npy', dims)
    print('dims.npy is saved in path:%s' % save_path)
    print('shape:', dims.shape)
    print('type:', type(dims[0][0]))


def gen_raw_data(img_path, img_size, save_path):
    size = img_size
    nums = countFile(img_path)
    data = np.ndarray(shape=(nums, 1, size, size), dtype=np.float32)

    folder_list = os.listdir(img_path)
    itr = 0
    for folders in folder_list:
        img_list = os.listdir(img_path + folders)
        contents = []
        for numbers in img_list:  # 遍历图片文件名
            contents.append(int(numbers[:-4]))  # 保存图片文件编号
        start = min(contents)  # 记录起始文件编号
        for i in range(start, len(img_list) + start):  # 起始编号为start的图片开始向后操作图片数量个循环
            img = cv2.imread(img_path + folders + '/%d.png' % i)
            img = cv2.resize(img, (size, size), interpolation=cv2.INTER_AREA)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            img = np.float32(img)
            dst = np.zeros(img.shape, dtype=np.float32)
            img = cv2.normalize(img, dst, alpha=0, beta=1.0, norm_type=cv2.NORM_MINMAX)
            data[itr] = img
            itr += 1
        print('clip %s ' % folders + 'is processed.')
    np.save(save_path + 'input_raw_data.npy', data)
    print('input_raw_data.npy is saved in path:%s' % save_path)
    print('shape:', data.shape)
    print('type:', type(data[0][0][0][0]))

if mode == 'train':
    gen_npy_clips(train_frame_nums, save_path=npy_save_path)
    gen_npy_dims(frame_size, save_path=npy_save_path)
    gen_raw_data(img_path=train_dir, img_size=frame_size, save_path=npy_save_path)
    gen_npz_data(npy_save_path)

if mode == 'valid':
    gen_npy_clips(val_frame_nums, save_path=npy_save_path)
    gen_npy_dims(frame_size, save_path=npy_save_path)
    gen_raw_data(img_path=valid_dir, img_size=frame_size, save_path=npy_save_path)
    gen_npz_data(npy_save_path)
else:
    print('Error and out.')
