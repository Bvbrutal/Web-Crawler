# -*- coding: utf-8 -*-

# 确保Python文件的编码方式为utf-8，以支持特殊字符

# 直接在字符串中包含emoji
message = "Hello, 🌍 World! 😃"
print(message)

# 使用Unicode转义序列插入emoji
emoji = "\U0001F604"  # 笑脸emoji的Unicode码点
print("This is a smiley face:", emoji)

# 处理包含特殊字符的文本文件
with open('file_with_emoji.txt', 'w', encoding='utf-8') as file:
    file.write("This is a text with emoji: 😎")

with open('file_with_emoji.txt', 'r', encoding='utf-8') as file:
    content = file.read()
    print("File content:", content)
