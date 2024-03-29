# %% set all packages
import glob
import os
import random
import shutil

import numpy as np

if __name__ == '__main__':
    # src directory
    src_dir = 'Z:/Marlen/datasets/beauty-and-beast/qupath_tiles/H.18.4262_only-H.vmic/size256_overlap64'
    allFileNames = glob.glob(src_dir + '/*.png')
    allFileNames = random.sample(allFileNames, len(allFileNames))

    # %% Creating Train / Val / Test folders (One time use)
    val_ratio = 0
    test_ratio = 0.4

    # % prepare the directories
    # train folder
    trainFolder = src_dir + '/train'
    if os.path.exists(trainFolder):
        shutil.rmtree(trainFolder)
    os.makedirs(trainFolder)
    # validation folder
    # valFolder = data_dir +'/val'
    # if os.path.exists(valFolder):
    #    shutil.rmtree(valFolder)
    # os.makedirs(data_dir +'/val')
    # test folder
    testFolder = src_dir + '/test'
    if os.path.exists(testFolder):
        shutil.rmtree(testFolder)
    os.makedirs(src_dir + '/test')

    # % prepare the data
    # Creating partitions of the data after shuffeling
    allFileNames = glob.glob(src_dir + '/*.tif')
    np.random.shuffle(allFileNames)
    # train_FileNames, val_FileNames, test_FileNames = np.split(np.array(
    # allFileNames), [int(len(allFileNames) * (1 - val_ratio + test_ratio)),
    # int(len(allFileNames) * (1 - test_ratio))])

    train_FileNames, test_FileNames = np.split(np.array(allFileNames), [
        int(len(allFileNames) * (1 - test_ratio))])

    train_FileNames = [name for name in train_FileNames.tolist()]
    # val_FileNames = [name for name in val_FileNames.tolist()]
    test_FileNames = [name for name in test_FileNames.tolist()]

    print('Total images: ', len(allFileNames))
    print('Training: ', len(train_FileNames))
    # print('Validation: ', len(val_FileNames))
    print('Testing: ', len(test_FileNames))

    # % Copy-pasting images
    for name in train_FileNames:
        shutil.copy(name, src_dir + '/train')

    # for name in val_FileNames:
    #    shutil.copy(name, data_dir + '/val')

    for name in test_FileNames:
        shutil.copy(name, src_dir + '/test')

    # % counter section
    print('Done!')
