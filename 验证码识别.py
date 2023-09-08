# -*- coding: UTF-8 -*-
import pytesseract
from PIL import Image

image = Image.open('static/img/code153.jpg')
text = pytesseract.image_to_string(image,lang='eng',config='--psm 13 --oem 3')

# 3. 打印识别结果
print(text)