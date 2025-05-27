'''
Netease Minecraft Nickname Random by wangyupu
使用来自网易的词典
全部使用built-in库
可自定义
'''
import random
import os
import hashlib
import time
import json

# 名称的结构 可配置
# 前缀、人名、人物、动词、形容、物品 填入为随机
# 以+分割
# 比如 "前缀+人名+动词" 就是随机从前缀、人名、动词中选词再拼接
# 如果要强制制定词，可使用 "#字词"，比如："前缀+#的"就是随机的前缀拼接一个"的"字
# 格式是python字典，不可缺逗号
# 如果在末尾留下了+号会报错，注意格式
# 没有使用eval、exec之类的不安全实现
#
# default:
# name_stru = {1:"前缀+人名+动词",2:"前缀+人物+动词",
#           3:"前缀+人物+动词",4:"前缀+形容+人名",
#           5:"前缀+动词+人物",6:"前缀+动词+人名",
#           7:"人名+#的+前缀+物品",}

# 不要改啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊
_version = 0.1
application_start_time = time.time()
# 获取目录
path = __file__
path = path[:len(path)-7]
os.chdir(path)
#print(f"当前目录:{path}")

# 处理db
dbfs = os.listdir("./db/")
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
    with open(f"{path}db/{filename}",mode='r') as file:
        dbs[filename] = file.read().split("\n")

with open(f"{path}db/字到音",mode='r') as file:
    lines = file.read().split('\n')
    for item in lines:
        lineitems = item.split(',')
        f2s[lineitems[0]] = lineitems[1]

name_stru = {}
name_stru_keys = []
with open(f"{path}name_strus.json",mode='r') as file:
    name_stru = json.load(file) # type: ignore

for k,v in name_stru.items():
    name_stru_keys.append(k)

##print("加载db成功")

# 主
def init_random():
    seed = (hashlib.sha512(str(time.time()).encode()).hexdigest())[:8]
    seed = int(seed,16)
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
        nick = nick+thispart

    return nick


