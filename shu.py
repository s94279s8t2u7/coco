import shutil

def my_move(datadir,trainlistdir,vallistdir,traindir,valdir):
    # 打開txt
    fopen = open(trainlistdir,'r')
    # 讀取圖片名稱
    file_names = fopen.readlines()
    for file_name in file_names:
        file_name = file_name.strip('\n')

        # 圖片路徑
        traindata = datadir + file_name+'.jpg'

        shutil.move(traindata,traindir)

    fopen = open(vallistdir,'r')
    file_names = fopen.readlines()
    for file_name in file_names:
        file_name = file_name.strip('\n')

        # 圖片路徑
        valdata = datadir + file_name+'.jpg'

        shutil.move(valdata,valdir)
datadir='C:/Users/User/Desktop/coco/image/'
trainlistdir = 'C:/Users/User/Desktop/coco/txt/train_total.txt'
vallistdir = 'C:/Users/User/Desktop/coco/txt/val_total.txt'
traindir = 'C:/Users/User/Desktop/coco/train'
valdir = 'C:/Users/User/Desktop/coco/val'

my_move(datadir,trainlistdir,vallistdir,traindir,valdir)