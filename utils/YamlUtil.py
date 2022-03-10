import os

import yaml


class YamlReader:
#初始化yaml文件，判断存在
    def __init__(self,yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        self._data = None
        self._data_all = None
#读yaml文件
    #读取单文档
    def data(self):
        if not self._data:
            with open(self.yamlf,"rb") as f:
                self._data = yaml.safe_load(f)
                return self._data
    #读取多文档
    def data_all(self):
        if not self._data_all:
            with open(self.yamlf,"rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
                return self._data_all

