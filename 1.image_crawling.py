import os
import time
import urllib
from selenium import webdriver
from urllib.request import urlopen
from selenium.webdriver.common.keys import Keys

# chromedriver 불러오기
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('C:\chrome\chromedriver.exe', options=chrome_options)

# 디렉터리 생성
pwd = os.getcwd()
image_directory = os.path.join(pwd, "crawling_images")
if not os.path.exists(image_directory):
    os.makedirs(image_directory)

# 명단
names = ['지석진', '유재석', '김종국', '하하', '양세찬','전소민']

# 출연진 명단을 통해서 한명식 이미지를 클롤링
for name in names:
    print(f'[{name}] 이미지 크롤링 시작')

    # 이름 디렉터리 생성
    name_directory = os.path.join(pwd, "crawling_images", name)
    if not os.path.exists(name_directory):
        os.makedirs(name_directory)

    # 이미지 크롤링
    driver.get("https://www.google.co.kr/imghp?hl=ko&ogbl")
    query = driver.find_element_by_name("q")
    query.send_keys(name)
    query.send_keys(Keys.RETURN)

    # 이미지를 최대로 찾기 위해서 스크롤을 계속 아래로 내림
    last_height = driver.execute_script("return document.body.scrollHeight") # 마지막 시점의 창 높이 저장
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # 창 높이까지 스크롤
        time.sleep(2) # 스크롤 후 창이 로딩될때까지 2초를 기다리겠다는 명령어
        new_height = driver.execute_script("return document.body.scrollHeight") # 스크롤이 된 후의 창 높이를 새로운 높이로 저장

        if new_height == last_height: # 새로운 높이가 이전 높이와 변하지 않았으면 스크롤 종료
            try:
                driver.find_element_by_css_selector(".mye4qd").click()
            except:
                break
        last_height = new_height

    # 이미지 태그 클래스
    images = driver.find_elements_by_css_selector(".rg_i.Q4LuWd")

    # 이미지 다운로드
    count = 1
    for image in images:
        try:
            image.click()
            image_url = driver.find_element_by_xpath(
                "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img").get_attribute(
                "src")

            # 이미지 저장
            urllib.request.urlretrieve(image_url, f"{name_directory}/{count}.jpg")
            print(f"[{name}] {count}개 저장완료")
            count = count + 1
        except:
            pass

        if count > 5000:
            break

    print(f"[{name}] 다운로드 완료")
