import os

path = "./data"
#制作字典映射
dic = {}

for name in os.listdir(path):
    for label in name[:-4]:
        if label not in dic:
            dic[label] = 1
with open("./dic.txt",'w') as f:
    for i in dic:
        f.write(i + "\n")