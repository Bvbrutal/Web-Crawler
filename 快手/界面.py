import jieba

import os

import pandas as pd

jieba.setLogLevel(jieba.logging.INFO)
# directory-主路径
# fileType-指定文件类型
# fileList-目标类型文件列表（路径+文件名）
def SearchFiles(directory, fileType):
    fileList=[]
    for root, subDirs, files in os.walk(directory):
        for fileName in files:
            if fileName.endswith(fileType):
                fileList.append(os.path.join(root,fileName))
    return fileList

def keyword(path):
    filenames = SearchFiles(path,'.txt')
    for filename in filenames:
        file = open(filename, "r", encoding='utf-8')
        txt = file.read()
        words = jieba.lcut(txt)
        count = {}
        for word in words:  # 使用 for 循环遍历每个词语并统计个数
            if len(word) <= 1:  # 排除单个字的干扰，使得输出结果为词语
                continue
            else:
                count[word] = count.get(word, 0) + 1  # 如果字典里键为 word 的值存在，则返回键的值并加一，如果不存在键word，则返回0再加上1

        exclude = ["可以", "@", ".", "、", "[", "]", "'", " ", "的", "我", "（", "）", "。", "_", "-", "这样", '~', '吧', '？', '…',
                   '吗', ',', '，', 'ㅤ', '·', '你', '᭄', '～', '了', '666', 'Hi', 'N95', 'airdrop', 'almostcry', 'alpaca',
                   'angry', 'arranged', 'awkard', 'awkward', 'balloon', 'banger', 'boom', 'boss', 'brick', 'bro', 'bye',
                   'cake', 'camera', 'cat', 'celebrate', 'celebrity', 'cheers', 'clap', 'cool', 'crazy', 'crown',
                   'cryLaugh', 'cry', 'curious', 'curse', 'dance', 'despise', 'dignose', 'dirtytalk', 'disdain', 'dizzy',
                   'dog', 'dogfood', 'double', 'dragon', 'eatmelon', 'explosion', 'facepalm', 'fade', 'fighting', 'fire',
                   'fireworks', 'flirting', 'follow', 'fortune', 'fossil', 'frown', 'gamepad', 'ghost', 'gold', 'good',
                   'grin', 'handheart', 'happy', 'hard', 'heart', 'helmet', 'hitface', 'hole', 'hug', 'kiss', 'kitty',
                   'knee', 'knife', 'latern', 'laughcry', 'left', 'leftfist', 'like', 'lion', 'lipstick', 'love', 'loveu',
                   'makeup', 'microphone', 'minus', 'mirror', 'money', 'mouse', 'muscle', 'nail', 'naughty', 'nice',
                   'nolisten', 'nolook', 'nosebleed', 'nospeak', 'nostrils', 'oh', 'omg', 'oops', 'pan', 'party', 'pat',
                   'pig', 'pigfoot', 'pignose', 'please', 'pollution', 'poor', 'pout', 'pray', 'prickekheart', 'quiet',
                   'rainbow', 'redface', 'redpacket', 'rich', 'rightFist', 'right', 'rose', 'rotate', 'sad', 'scared',
                   'shiba', 'shit', 'shutup', 'shy', 'simper', 'skeleton', 'sleep', 'sleepy', 'smile', 'sneak', 'snicker',
                   'snort', 'sophisticated', 'sour', 'starryeyed', 'stunned', 'stupid', 'surprised', 'sweat', 'sweaty',
                   'tears', 'tease', 'thanks', 'titter', 'touch', 'treacherous', 'vomit', 'vomitblood', 'waiting',
                   'wanttoeat', 'washhands', 'watergun', 'welcome', 'what', 'win', 'wipenose', 'wronged', 'yawn', '不听',
                   '不看', '不聽', '不說', '不说', '乾杯', '亲亲', '优秀', '偷瞄', '偷笑', '優秀', '元宝', '元寶', '八倍鏡', '八倍镜', '再見', '再见', '冷汗',
                   '减1', '出魂儿', '出魂兒', '加油', '勤洗手', '化妆', '化妝', '南', '双鸡', '发', '口紅', '口红', '可怜', '可憐', '右哼哼', '右拳', '吃瓜',
                   '吐彩虹', '吐血', '呆住', '呕吐', '哈欠', '哦', '哭笑', '哼', '嘔吐', '嘘', '嘣', '囧', '困', '坏笑', '坑', '塗指甲', '壞笑', '大便',
                   '大哥', '大哭', '大鼻孔', '天啊', '头盔', '奸笑', '委屈', '安排', '尴尬', '尷尬', '左哼哼', '左拳', '干杯', '平底鍋', '平底锅', '庆祝', '微笑',
                   '心心', '必勝', '必胜', '快哭了', '怒言', '惊恐', '惊讶', '想吃', '愉快', '愛你', '愛心', '慶祝', '憨笑', '我愛你', '我爱你', '戴口罩', '手柄',
                   '扎心', '打招呼', '打脸', '打臉', '抓狂', '抠鼻', '抱抱', '拍一拍', '拜托', '拜託', '挑逗', '捂脸', '捂臉', '摄像机', '摳鼻', '摸头', '摸頭',
                   '撇嘴', '擦鼻涕', '攝像機', '旋轉', '旋转', '星星眼', '晕', '暈', '暴汗', '期待', '板砖', '板磚', '柴犬', '欢迎', '歡迎', '比心', '气球',
                   '氣球', '水枪', '水槍', '汗', '流鼻血', '涂指甲', '減1', '火', '灯笼', '点点关注', '点赞', '烟花', '煙花', '燈籠', '爆炸', '爱你', '爱心',
                   '狗', '狗粮', '狗糧', '狮子', '猪头', '猪蹄', '猪鼻子', '猫', '獅子', '玫瑰', '生气', '生氣', '疑問', '疑问', '發', '白眼', '皇冠', '皱眉',
                   '皺眉', '睡覺', '睡觉', '石化', '礼花', '祈祷', '祈禱', '福字', '禮花', '空投', '笑哭', '紅包', '紅臉蛋', '網紅', '網紅貓', '红包', '红脸蛋',
                   '网红', '网红猫', '罵你', '羊駝', '羊驼', '羞涩', '羞澀', '老司机', '老司機', '老鐵', '老铁', '老鼠', '肌肉', '色', '花謝了', '花谢了', '菜刀',
                   '落泪', '落淚', '蛋糕', '装傻', '裝傻', '親親', '調皮', '讚', '调皮', '豬蹄', '豬頭', '豬鼻子', '貓', '赞', '跪下', '跳舞', '鄙視', '鄙视',
                   '酷', '酸了', '錢', '钱', '閉嘴', '闭嘴', '难过', '雙雞', '難過', '雾霾', '霧霾', '鞭炮', '頭盔', '驚恐', '驚訝', '骂你', '骷髅', '骷髏',
                   '麥克風', '麦克风', '黑脸问', '黑臉問', '點贊', '點點關注', '鼓掌', '齜牙', '龇牙', '龍', '龙']  # 建立无关词语列表
        for key in list(count.keys()):  # 遍历字典的所有键，即所有word
            if key in exclude:
                del count[key]  # 删除字典中键为无关词语的键值对
        lists = list(count.items())  # 将字典的所有键值对转化为列表
        lists.sort(key=lambda x: x[1], reverse=True)  # 对列表按照词频从大到小的顺序排序
        wcc=filename.replace('.txt','')
        with open(f"{wcc}--关键词.txt", 'w', encoding='utf-8') as f:
            for i in range(50):  # 此处统计排名前五的单词，所以range(5)
                word, number = lists[i]
                fs = "关键字：'{0:6}'频次：{1}\n".format(word, number)
                f.write(fs)
                print(fs)
    return 0

def re_read(path):
    filenames=SearchFiles(path,'.csv')
    for i in filenames:
        r=pd.read_csv(i)
        print(r)
        r.to_csv(i, index=False, sep=',',encoding='utf-8-sig')

keyword('笨熊/')