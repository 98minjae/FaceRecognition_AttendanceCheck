import os
import shutil


pwd = os.getcwd()

# train 디렉터리 생성
train_datasets_directory = os.path.join(pwd, "datasets/train")
if not os.path.exists(train_datasets_directory):
    os.makedirs(train_datasets_directory)

# test 디렉터리 생성
test_datasets_directory = os.path.join(pwd, "datasets/test")
if not os.path.exists(test_datasets_directory):
    os.makedirs(test_datasets_directory)

# 명단
names = ['지석진', '유재석', '김종국', '하하', '양세찬', '전소민']

for i, name in enumerate(names):
    # train 디렉터리 생성
    train_datasets_directory_name = os.path.join(train_datasets_directory, name)
    if not os.path.exists(train_datasets_directory_name):
        os.makedirs(train_datasets_directory_name)

    # test 디렉터리 생성
    test_datasets_directory_name = os.path.join(test_datasets_directory, name)
    if not os.path.exists(test_datasets_directory_name):
        os.makedirs(test_datasets_directory_name)

    count = 1
    file_list = os.listdir(os.path.join("filtered_images", name))
    for file in file_list:
        source_file = os.path.join("filtered_images", name, file)

        if count > 200:
            shutil.copy(source_file, f"{test_datasets_directory_name}/{count}.jpg")
        else:
            shutil.copy(source_file, f"{train_datasets_directory_name}/{count}.jpg")
        count = count + 1
