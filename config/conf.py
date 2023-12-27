import os

# 获取当前文件目录
from utils.YamlUtil import YamlUtil

current_path = os.path.abspath(__file__)
# print(current_path)
BASE_DIR = os.path.dirname(os.path.dirname(current_path))
# print(BASE_DIR)
# 获取配置文件目录
config_path = BASE_DIR + os.sep + "config"
# print(config_path)
# 定义config文件路径
config_file = config_path + os.sep + "conf.yaml"


#获取配置文件目录
def get_config_path():
    return config_path

#获取配置文件
def get_config_file():
    return config_file

# 读取配置文件
class ConfigReader:
    #初始化读取配置
    def __init__(self):
        self.config = YamlUtil().read_yaml(get_config_file())

    #获取全部配置项
    def get_conf_all(self):
        return self.config

    #获取url
    def get_conf_url(self):
        return self.config['BASE']['test']['url']

    # 获取path
    def get_conf_path(self):
        return self.config['BASE']['test']['path']

    #获取token
    def get_conf_token(self):
        return self.config['BASE']['test']['token']

    #获取请求体body格式
    def get_conf_body(self):
        return self.config['BASE']['body']

if __name__ == "__main__":
    r = ConfigReader()
    print(r.get_conf_body())
