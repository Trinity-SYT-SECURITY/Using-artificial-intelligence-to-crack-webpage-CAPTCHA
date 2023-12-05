from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import pytesseract
import time

# convert image to char
def ocr_char(img):
    tess_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=o123456789abcdefg'
    char = pytesseract.image_to_string(image=img, config=tess_config)
    char = char.replace("\n","").replace(" ","").replace("o","0")
    if len(char) == 0:
        char = "8"
    return char
  
# reduce noises in image
def denoise_img(img):
    img = img.astype(float) / 255
    brightness = 1 - np.max(img, axis=2)
    brightness = (255 * brightness).astype(np.uint8)
    binaryThresh = 230
    # image_show_debug("test", brightness)
    filtered = cv2.threshold(brightness, binaryThresh, 255, cv2.THRESH_BINARY)[1]
    # image_show_debug("test", filtered)
    return filtered

# split the image by chars
def split_img(img):
	img = img[20:35,49:160]
	x_px_indx = 1
	result = [] 
	for i in range(1,7):
		result.append(img[2:16, x_px_indx:x_px_indx+9])
		x_px_indx += 20
	return result

# convert image to string
def decode(captcha_img):
    # image_show_debug("test", captcha_img)
    result = ""
    splited_text_img = split_img(denoise_img(captcha_img))
    for i in splited_text_img:
      	result += ocr_char(i)
    return result


def main():
    # initalizing the browser
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://siliconexam.com/st-register.php")

    # getting the captcha image
    w, h = 800,700
    driver.set_window_size(w, h)
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    document_height = driver.execute_script("return document.body.scrollHeight")
    driver.save_screenshot('bottom.png')

    captchaimage = driver.find_element(By.CLASS_NAME,"tp")
    captchaimage = driver.find_element(By.XPATH,'//img[@id="chkimg"]')

    left = captchaimage.location['x']
    right = left + captchaimage.size['width']
    top = h - (document_height - captchaimage.location['y'])
    bottom = top + captchaimage.size['height']

    # save to png file
    img = Image.open('bottom.png')
    captcha = img.crop((left, top, right, bottom))
    captcha.save('captcha.png')

    # appling ocr functions
    img = cv2.imread('captcha.png')
    result = decode(img)

    # write back to website
    input_element = driver.find_element(By.NAME,"rvcode")
    input_element.send_keys(result)

    # save tests result to folder
    file_suffix = -1
    pathtofile = ""
    while True:
        file_suffix += 1
        pathtofile = f"results/test{str(file_suffix)}.png"
        if (not os.path.exists(pathtofile)):
            break

    driver.save_screenshot(pathtofile)

    cv2.imshow(f"ocr result : {result}", img)
    cv2.waitKey(5000)


for i in range(0,10):
    main()