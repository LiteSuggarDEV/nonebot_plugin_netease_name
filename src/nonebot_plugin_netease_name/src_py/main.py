"""
Netease Minecraft Nickname Random by wangyupu
使用来自网易的词典
全部使用built-in库
可自定义
"""

from pathlib import Path
import random
import os
import hashlib
import time
import json

# 不要改啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
_version = 0.1
application_start_time = time.time()
# 获取目录
path = __file__
path = path[: len(path) - 7]
cwd = Path(path)
# print(f"当前目录:{path}")

# 处理db
dbfs = os.listdir(cwd / "db")
dbs = {}
f2s = {}
try:
    dbfs.remove(".DS_Store")
    dbfs.remove("字到音")
except:  # noqa: E722
    pass
##print(f"获取到的名称片段:{dbfs}")
# 写入变量
for filename in dbfs:
    with open(f"{path}db/{filename}", mode="r") as file:
        dbs[filename] = file.read().split("\n")

with open(f"{path}db/字到音", mode="r") as file:
    lines = file.read().split("\n")
    for item in lines:
        lineitems = item.split(",")
        f2s[lineitems[0]] = lineitems[1]

name_stru = {}
name_stru_keys = []
with open(f"{path}name_strus.json", mode="r") as file:
    name_stru = json.load(file)  # type: ignore

for k, v in name_stru.items():
    name_stru_keys.append(k)

##print("加载db成功")


# 主
def init_random():
    seed = (hashlib.sha512(str(time.time()).encode()).hexdigest())[:8]
    seed = int(seed, 16)
    ##print(f"初始化到种子{seed}")
    random.seed(seed)


def get_random_nickname():
    nickname_type = random.choice(name_stru_keys)
    nick = ""
    parts = []

    thisnickname_stru = (name_stru[nickname_type]).split("+")
    for item in thisnickname_stru:
        if str(item)[0] == "#":
            thispart = item[1:]
        else:
            thispart = random.choice(dbs[item])
        parts.append(thispart)
        nick = nick + thispart

    return nick
