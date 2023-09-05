import matplotlib.pyplot as plt
import jieba
import wordcloud
import os


def SearchFiles(directory, fileType):
    fileList = []
    for root, subDirs, files in os.walk(directory):
        for fileName in files:
            if fileName.endswith(fileType):
                fileList.append(os.path.join(root, fileName))
    return fileList


def wordclound(path):
    lists = SearchFiles(path, '.txt')
    print(lists)
    for title in lists:
        lil={}
        # SearchFiles(path,'.txt')
        # 1.读入txt文本数据
        text = open(title, "r", encoding="UTF-8").read()
        # print(text)
        # 2.结巴中文分词，生成字符串，默认精确模式，如果不通过分词，无法直接生成正确的中文词云
        words = jieba.lcut(text)
        count = []
        for word in words:  # 使用 for 循环遍历每个词语并统计个数
            if len(word) <= 1:  # 排除单个字的干扰，使得输出结果为词语
                continue
            else:
                count.append(word)
        exclude = ["可以", "@", ".", "、", "[", "]", "'", " ", "的", "我", "（", "）", "。", "_", "-", "这样", '~', '吧', '？', '…',
                   '吗', ',', '，', 'ㅤ', '·', '你', '᭄', '～', '了', '666', 'Hi', 'N95', 'airdrop', 'almostcry', 'alpaca',
                   'angry', 'arranged', 'awkard', 'awkward', 'balloon', 'banger', 'boom', 'boss', 'brick', 'bro', 'bye',
                   'cake', 'camera', 'cat', 'celebrate', 'celebrity', 'cheers', 'clap', 'cool', 'crazy', 'crown',
                   'cryLaugh', 'cry', 'curious', 'curse', 'dance', 'despise', 'dignose', 'dirtytalk', 'disdain',
                   'dizzy','dog', 'dogfood', 'double', 'dragon', 'eatmelon', 'explosion', 'facepalm', 'fade', 'fighting',
                   'fire','fireworks', 'flirting', 'follow', 'fortune', 'fossil', 'frown', 'gamepad', 'ghost', 'gold', 'good',
                   'grin', 'handheart', 'happy', 'hard', 'heart', 'helmet', 'hitface', 'hole', 'hug', 'kiss', 'kitty',
                   'knee', 'knife', 'latern', 'laughcry', 'left', 'leftfist', 'like', 'lion', 'lipstick', 'love',
                   'loveu','makeup', 'microphone', 'minus', 'mirror', 'money', 'mouse', 'muscle', 'nail', 'naughty', 'nice',
                   'nolisten', 'nolook', 'nosebleed', 'nospeak', 'nostrils', 'oh', 'omg', 'oops', 'pan', 'party', 'pat',
                   'pig', 'pigfoot', 'pignose', 'please', 'pollution', 'poor', 'pout', 'pray', 'prickekheart', 'quiet',
                   'rainbow', 'redface', 'redpacket', 'rich', 'rightFist', 'right', 'rose', 'rotate', 'sad', 'scared',
                   'shiba', 'shit', 'shutup', 'shy', 'simper', 'skeleton', 'sleep', 'sleepy', 'smile', 'sneak',
                   'snicker','snort', 'sophisticated', 'sour', 'starryeyed', 'stunned', 'stupid', 'surprised', 'sweat', 'sweaty',
                   'tears', 'tease', 'thanks', 'titter', 'touch', 'treacherous', 'vomit', 'vomitblood', 'waiting',
                   'wanttoeat', 'washhands', 'watergun', 'welcome', 'what', 'win', 'wipenose', 'wronged', 'yawn', '不听',
                   '不看', '不聽', '不說', '不说', '乾杯', '亲亲', '优秀', '偷瞄', '偷笑', '優秀', '元宝', '元寶', '八倍鏡', '八倍镜', '再見', '再见',
                   '冷汗', '减1', '出魂儿', '出魂兒', '加油', '勤洗手', '化妆', '化妝', '南', '双鸡', '发', '口紅', '口红', '可怜', '可憐', '右哼哼', '右拳',
                   '吃瓜','吐彩虹', '吐血', '呆住', '呕吐', '哈欠', '哦', '哭笑', '哼', '嘔吐', '嘘', '嘣', '囧', '困', '坏笑', '坑', '塗指甲', '壞笑',
                   '大便','大哥', '大哭', '大鼻孔', '天啊', '头盔', '奸笑', '委屈', '安排', '尴尬', '尷尬', '左哼哼', '左拳', '干杯', '平底鍋', '平底锅', '庆祝',
                   '微笑','心心', '必勝', '必胜', '快哭了', '怒言', '惊恐', '惊讶', '想吃', '愉快', '愛你', '愛心', '慶祝', '憨笑', '我愛你', '我爱你', '戴口罩',
                   '手柄','扎心', '打招呼', '打脸', '打臉', '抓狂', '抠鼻', '抱抱', '拍一拍', '拜托', '拜託', '挑逗', '捂脸', '捂臉', '摄像机', '摳鼻', '摸头',
                   '摸頭','撇嘴', '擦鼻涕', '攝像機', '旋轉', '旋转', '星星眼', '晕', '暈', '暴汗', '期待', '板砖', '板磚', '柴犬', '欢迎', '歡迎', '比心',
                   '气球','氣球', '水枪', '水槍', '汗', '流鼻血', '涂指甲', '減1', '火', '灯笼', '点点关注', '点赞', '烟花', '煙花', '燈籠', '爆炸', '爱你',
                   '爱心','狗', '狗粮', '狗糧', '狮子', '猪头', '猪蹄', '猪鼻子', '猫', '獅子', '玫瑰', '生气', '生氣', '疑問', '疑问', '發', '白眼', '皇冠',
                   '皱眉','皺眉', '睡覺', '睡觉', '石化', '礼花', '祈祷', '祈禱', '福字', '禮花', '空投', '笑哭', '紅包', '紅臉蛋', '網紅', '網紅貓', '红包',
                   '红脸蛋','网红', '网红猫', '罵你', '羊駝', '羊驼', '羞涩', '羞澀', '老司机', '老司機', '老鐵', '老铁', '老鼠', '肌肉', '色', '花謝了', '花谢了',
                   '菜刀','落泪', '落淚', '蛋糕', '装傻', '裝傻', '親親', '調皮', '讚', '调皮', '豬蹄', '豬頭', '豬鼻子', '貓', '赞', '跪下', '跳舞', '鄙視',
                   '鄙视','酷', '酸了', '錢', '钱', '閉嘴', '闭嘴', '难过', '雙雞', '難過', '雾霾', '霧霾', '鞭炮', '頭盔', '驚恐', '驚訝', '骂你', '骷髅',
                   '骷髏','麥克風', '麦克风', '黑脸问', '黑臉問', '點贊', '點點關注', '鼓掌', '齜牙', '龇牙', '龍', '龙']  # 建立无关词语列表
        for key in count:
                if key in exclude:
                    lil[key] = lil.get(key, 0) + 1
        for n in list(lil.keys()):
            for m in range(lil[n]):
                count.remove(n)
        # print(type(cut_text))
        # 必须给个符号分隔开分词结果来形成字符串,否则不能绘制词云
        result = " ".join(count)
        # print(result)
        # 3.生成词云图，这里需要注意的是WordCloud默认不支持中文，所以这里需已下载好的中文字库
        # 无自定义背景图：需要指定生成词云图的像素大小，默认背景颜色为黑色,统一文字颜色：mode='RGBA'和colormap='pink'
        wc = wordcloud.WordCloud(
            font_path='simhei.ttf',
            # 设置字体，不指定就会出现乱码
            # 设置背景色
            background_color='white',
            # 设置背景宽
            width=300,
            # 设置背景高
            height=250,
            # 最大字体
            max_font_size=50,
            # 最小字体
            min_font_size=10,
            mode='RGBA'
            # colormap='pink'
        )
        # 产生词云
        wc.generate(result)
        # 保存图片
        wcs=title.replace('.txt','')
        wc.to_file(f"{wcs}.png")  # 按照设置的像素宽高度保存绘制好的词云图，比下面程序显示更清晰
        # 4.显示图片
        # 指定所绘图名称
        plt.figure("jay")
        # 以图片的形式显示词云
        plt.imshow(wc)
        # 关闭图像坐标系
        plt.axis("off")


wordclound('笨熊/')
