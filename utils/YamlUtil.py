import os

import yaml


def read_testcase(yaml_name):
    with open(os.getcwd() + "\\" + yaml_name) as f:
        res = yaml.load(f, yaml.FullLoader)
        return res


class YamlUtil:
    # 初始化yaml文件，判断存在
    def __init__(self):
        self._data = None
        self._data_all = None

    def read_yaml(self, yamlf):
        if os.path.exists(yamlf):
            self.yamlf = yamlf
        else:
            raise FileNotFoundError("文件不存在")
        with open(self.yamlf, "rb") as f:
            self._data = yaml.safe_load(f)
            return self._data

    # 写入
    def write_yaml(self, data):
        with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='a') as f:
            yaml.dump(data, stream=f, allow_unicode=True)

    # 清除
    def clear_yaml(self):
        with open(os.getcwd() + '/extract.yaml', encoding='utf-8', mode='w') as f:
            f.truncate()

    # 读yaml文件  读取单文档
    def data(self):
        if not self._data:
            with open(self.yamlf, "rb") as f:
                self._data = yaml.safe_load(f)
                return self._data

    # 读取多文档
    def data_all(self):
        if not self._data_all:
            with open(self.yamlf, "rb") as f:
                self._data_all = list(yaml.safe_load_all(f))
                return self._data_all
