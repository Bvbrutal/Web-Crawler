# -*- coding: UTF-8 -*-
from PIL import Image, ImageDraw, ImageFont
import random
import string


# 生成随机字符
def generate_random_string(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))


# 创建验证码图像
def create_captcha(text, width=200, height=80):
    # 创建白色背景图像
    image = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(image)

    # 选择字体和大小（根据需要替换字体文件的路径）
    font = ImageFont.truetype('static/Fonts/ARLRDBD.TTF',size=40)

    # 添加随机字符到图像
    draw.text((10, 10), text, fill='black', font=font)

    # 添加一些噪点
    for _ in range(100):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        draw.point((x, y), fill='gray')

    # 添加一些线条
    for _ in range(5):
        x1 = random.randint(0, width - 1)
        x2 = random.randint(0, width - 1)
        y1 = random.randint(0, height - 1)
        y2 = random.randint(0, height - 1)
        draw.line((x1, y1, x2, y2), fill='gray')

    return image


if __name__ == "__main__":
    captcha_text = generate_random_string()
    captcha_image = create_captcha(captcha_text)
    captcha_image.save('captcha.png')  # 保存验证码图像
    captcha_image.show()  # 显示验证码图像
