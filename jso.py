from glob import glob
import random

patch_fn_list = glob('C:/Users/User/Desktop/coco/train/*.jpg')


patch_fn_list = [fn.split('\\')[-1][:-4] for fn in patch_fn_list]

# 打亂圖片順序
random.shuffle(patch_fn_list)

train_num = int(0.7 * len(patch_fn_list))
train_patch_list = patch_fn_list[:train_num]
print(train_patch_list)
valid_patch_list = patch_fn_list[train_num:]

split = ['train_total','val_total','trainval_total']

for s in split:
    print(s)
    save_path = 'C:/Users/User/Desktop/coco/txt/'+ s +'.txt'

    if s =='train_total':
        with open(save_path,'w')as f:
            for fn in train_patch_list :
                f.write("%s\n" %fn)
    elif s =='val_total':
        with open(save_path,'w')as f:
            for fn in valid_patch_list:
                f.write("%s\n" %fn)           
    elif s == 'trainval_total':
        with open(save_path,'w')as f:
            for fn in patch_fn_list:
                f.write("%s\n" %fn)
    print("finish %s to %s" % (s, save_path))

