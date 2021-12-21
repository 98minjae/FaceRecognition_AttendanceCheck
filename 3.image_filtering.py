import os
import shutil
import face_recognition

# 디렉터리 생성
pwd = os.getcwd()
filter_directory = os.path.join(pwd, "filtered_images")
if not os.path.exists(filter_directory):
    os.makedirs(filter_directory)

# 명단
names = ['지석진', '유재석', '김종국', '하하', '양세찬', '전소민']

title_images = [
    '지석진.png',
    '유재석.jpeg',
    '김종국.jpeg',
    '하하.jpeg',
    '양세찬.jpeg',
    '전소민.jpeg'
]

# 출연진 명단을 통해서 한명식 얼굴을 비교하기
for i, name in enumerate(names):
    print(f'[{name}] 얼굴 비교 시작')

    # 이름 디렉터리 생성
    name_directory = os.path.join(filter_directory, name)
    if not os.path.exists(name_directory):
        os.makedirs(name_directory)

    # 대표 이미지
    title_image_path = os.path.join("title_images", title_images[i])
    title_image = face_recognition.load_image_file(title_image_path)
    title_image_encoding = face_recognition.face_encodings(title_image)[0]

    known_encodings = [title_image_encoding]

    # 비교할 이미지
    count = 1
    file_list = os.listdir(os.path.join("cropped_images", name))
    for file in file_list:
        try:
            sample_image_path = os.path.join("cropped_images", name, file)
            sample_image = face_recognition.load_image_file(sample_image_path)
            sample_image_encoding = face_recognition.face_encodings(sample_image)[0]
            distance = face_recognition.face_distance(known_encodings, sample_image_encoding)

            # distance가 0.5 미만일때만 파일을 복사
            if distance < 0.5:
                shutil.copy(sample_image_path, f"{name_directory}/{count}.jpg")
                print(f"[{name}] {count}개 저장완료")
                count = count + 1

                if count > 550:
                    break
        except:
            pass
