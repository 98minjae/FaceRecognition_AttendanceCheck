import os
import face_recognition
from PIL import Image


# 디렉터리 생성
pwd = os.getcwd()
crop_directory = os.path.join(pwd, "cropped_images")
if not os.path.exists(crop_directory):
    os.makedirs(crop_directory)

# 명단
names = ['지석진', '유재석', '김종국', '하하', '양세찬', '전소민']

# 명단을 통해서 한명식 얼굴을 잘라내기
for name in names:
    print(f'[{name}] 이미지 얼굴 잘라내기 시작')

    # 이름 디렉터리 생성
    name_directory = os.path.join(crop_directory, name)
    if not os.path.exists(name_directory):
        os.makedirs(name_directory)

    no = 1
    for i in range(1, 1001):
        image_path = os.path.join("crawling_images", name, f"{i}.jpg")

        if os.path.exists(image_path):
            try:
                # 얼굴 검출
                image = face_recognition.load_image_file(image_path)
                face_locations = face_recognition.face_locations(image)

                for face_location in face_locations:
                    top, right, bottom, left = face_location
                    face_image = image[top:bottom, left:right]
                    pil_image = Image.fromarray(face_image)
                    pil_image.save(f"{name_directory}/{no}.jpg")
                    print(f"[{name}] {no}개 저장완료")
                    no = no + 1
            except:
                pass
    print(f"[{name}] 저장 완료")
