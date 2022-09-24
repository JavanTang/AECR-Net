# png to h5py

from PIL import Image
import h5py
import numpy as np
import glob
import os

def hazy_clear_pair(dir_path):
    # generate hazy and clear pair
    clear_path = os.path.join(dir_path, 'clear')
    hazy_path = os.path.join(dir_path, 'hazy')
    files = glob.glob(hazy_path + '/*.png')
    for i, file in enumerate(files):
        clear_png = os.path.join(clear_path, os.path.basename(file).split('_')[0] + '.png')
        hazy_png = os.path.join(hazy_path, os.path.basename(file))
        yield clear_png, hazy_png

def png_to_h5py(dir_path, h5path):
    # convert png to h5py
    # h5py_file = h5py.File(h5path, 'w')
    for i, (clear_png, hazy_png) in enumerate(hazy_clear_pair(dir_path)):
        clear = Image.open(clear_png)
        hazy = Image.open(hazy_png)
        h5py_file = h5py.File(os.path.join(h5path, str(i)+'.h5'), 'w')
        h5py_file.create_dataset('haze', data=hazy)
        h5py_file.create_dataset('gt', data=clear)
        h5py_file.close()

def split_h5data_train_test(h5_dir, dataset_path) -> None:
    files = glob.glob(h5_dir + '/*.h5')
    files = list(files)
    np.random.shuffle(files)
    train_files = files[:int(len(files)*0.8)]
    test_files = files[int(len(files)*0.8):]

    # move dataset_path
    for i, h5_file_name in enumerate(train_files):
        os.replace(h5_file_name, os.path.join(dataset_path, 'ITS_train',str(i)+'.h5'))
    
    for i, h5_file_name in enumerate(test_files):
        os.replace(h5_file_name, os.path.join(dataset_path, 'ITS_test',str(i)+'.h5'))
    


if __name__ == '__main__':
    # 1. images to h5 file
    png_to_h5py('/home/tangzhifeng/codes/AECR-Net/ITS_v2', '/home/tangzhifeng/codes/AECR-Net/h5/')
    # 2. spliting h5 datas becames train datas and test datas
    split_h5data_train_test('/home/tangzhifeng/codes/AECR-Net/h5/','/home/tangzhifeng/codes/AECR-Net/datasets')
