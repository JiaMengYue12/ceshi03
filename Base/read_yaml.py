import os,sys
sys.path.append(os.getcwd())
import yaml

def read_yaml():
    with open(os.getcwd()+os.sep+"Data"+os.sep+"data.yaml","r",encoding="utf-8") as f:
        return yaml.load(f)

# print(os.getcwd())
print(read_yaml())



# 调试方法
# def read_yaml():
#     with open("../Data/data.yaml","r",encoding="utf-8") as f:
#         return yaml.load(f)
#
# if __name__ == '__main__':
#     print(read_yaml())