# 导入streamlit库
import streamlit as st
import os
from PIL import Image
import random
import pandas as pd
# 导入datetime库，用于计算恋爱天数
import datetime

# 加载留言数据
# @st.cache_data
def load_messages():
    try:
        messages = pd.read_csv("messages.csv")
    except FileNotFoundError:
        messages = pd.DataFrame(columns=["留言内容"])
    return messages


# 保存留言数据
def save_messages(messages):
    messages.to_csv("messages.csv", index=False)

# 添加留言
def add_message(message, messages):
    message_data = {"留言内容": message}
    messages = messages.append(message_data, ignore_index=True)
    return messages
# 设置网页标题和图标

st.set_page_config(page_title="小杰大宝", page_icon="❤️", layout="centered", initial_sidebar_state="expanded")
 # 使用HTML和CSS创建浪漫的鼠标特效
custom_html = '''
 <html lang="en">
    <head>
        <style>
            .bubble {
                position: absolute;
                font-family: "Arial", sans-serif; /* 修改为特定的字体 */
                color: red; /* 修改为特定的颜色 */
                animation: moveUp 5s infinite;
            }

            @keyframes moveUp {
                0% {
                    transform: translateY(0);
                    opacity: 1;
                }
                100% {
                    transform: translateY(-100vh);
                    opacity: 0;
                }
            }
        </style>
    </head>
    <body>
        <script>
            function createBubble() {
                let content = ["❤一起闯天下❤", "❤小杰和大宝❤", , , "❤爱就一个字❤",
                    "❤星辰大海❤", "❤千千万万❤", "❤小杰❤",  "❤带你回家❤", "❤晚星❤", "大宝&小杰",
                   "❤所念皆星河❤"
                ] //自定义内容的数组
                const bubble = document.createElement("div");
                bubble.textContent = content[Math.ceil(Math.random() * content.length)];
                bubble.className = "bubble";
                bubble.style.left = Math.random() * window.innerWidth + "px";
                document.body.appendChild(bubble);

                setTimeout(() => {
                    bubble.remove();
                }, 5000);
            }

            setInterval(createBubble, 1000);
        </script>
    </body>
    </html>
'''
messages = load_messages()  # 声明为全局变量

# 设置背景音乐，这里使用了一首甜蜜的歌曲《让我留在你身边》
audio_file = open("./data/rwlznsb.mp3", "rb")
audio_bytes = audio_file.read()
st.audio(audio_bytes, format="audio/mp3")

# 设置网页标题和副标题
# 主要内容
st.title("亲爱的苏有理（小杰），我错了")
st.markdown("这是一个专门为你准备的道歉网站，表达我的真诚歉意。")
# st.markdown("我们已经在一起的天数：")
# start_date = datetime.date(year=2022, month=10, day=9)  # 将开始日期替换成您们的纪念日
# days_together = (datetime.date.today() - start_date).days
# st.markdown(f"## {days_together}天")

# 显示一个心形气球的图片，上面写着“对不起”
st.image("./data/OIG.talYn.7qiTrbkFfA4fTg.jpg", use_column_width=True)

# 甜言蜜语
sweet_words = [
    "你是我的阳光，让我的世界绽放。",
    "你的微笑是我每天最美的风景。",
    "爱上你是我这辈子最好的决定。",
    "和你在一起的时光是我最想珍藏的宝藏。",
    "你的温柔让我感到无比幸福。",
]

# 随机显示一个甜言蜜语
sweet_word = random.choice(sweet_words)
st.markdown(f"## {sweet_word}")

# 道歉语
apology_message = """
亲爱的，我真的很抱歉让你伤心了，
我没有考虑到你的感受，
我希望你能原谅我并给我一个机会重新做好。
你对我非常重要，我愿意付出努力来弥补我的错误。
请原谅我，我真的爱你。
"""

st.markdown(f"## **大宝想说：**")
st.markdown(apology_message)


# 写一些甜言蜜语，表达你的歉意和爱意
st.write("""
亲爱的，我知道我这次做得很不对，让你伤心生气了。
我真的很后悔，我不该对你发脾气吵你（明知道你是对我好）。
你是我最爱的人，没有你我无法想象我的生活。
你给了我无数的快乐和温暖，你是我的天使，我喜欢看你笑，和你一起闯天下。
请原谅我这一次的错误，给我一个机会重新开始。
我会好好珍惜你，好好对待你，好好爱护你。
请相信我，我是真心真意地爱着你。
""")

# 显示一个恋爱天数计时器，用于提醒你们相爱的时间
start_date = st.date_input("相恋的日期", datetime.date(2022, 10, 9))
today = datetime.date.today()
delta = today - start_date
st.write(f"我们已经相爱了{delta.days}天了")
st.write("每一天都是我们的纪念日")


# 显示一个图片长廊，展示你们之前的点点滴滴
# 获取photos文件夹下所有的图片文件名
photos = os.listdir("./data/images")
# 创建一个空列表，用于存放图片对象
images = []
# 遍历每个图片文件名
for photo in photos:
    # 打开图片文件，并将其添加到列表中
    image = Image.open(os.path.join("./data/images", photo))
    images.append(image)
st.image(images,width=120)
    



# 显示一个按钮，用于发送短信给你的对象
if st.button("原谅你啦"):
    st.success("爱你噢")
    st.balloons()
st.balloons()

# 留言输入框
new_message = st.text_input("小杰大宝的留言板:")
if st.button("留言"):
    if new_message:
        messages = add_message(new_message, messages)
        save_messages(messages)
        st.success("留言成功！")

# 显示最新的留言

if len(messages) > 0:
    st.subheader("最新留言：")
    for message in messages["留言内容"][::-1]:
        st.write(message)
else:
    st.write("暂无留言")

st.components.v1.html(custom_html)
