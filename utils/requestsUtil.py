# 封装请求方法
import json
import re

import requests

from config.conf import ConfigReader
from utils.YamlUtil import YamlUtil


class RequestUtil:
    sess = requests.session()

    def __init__(self):
        self.base_url = ConfigReader().get_conf_url()
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method=method, url=url, params=params, data=data, json=json, headers=headers,
                                    **kwargs)

    def replace_str(self, data):
        data_type = type(data)
        # print(data_type)
        if isinstance(data, list) or isinstance(data, dict):
            str_data = json.dumps(data)
        else:
            str_data = str(data)
        for i in range(1, str_data.count('${') + 1):
            if "${" in str_data and "}" in str_data:
                start_index = str_data.index("${")
                end_index = str_data.index("}")
                old_value = str_data[start_index:end_index + 1]
                new_value = YamlUtil().read_yaml(old_value[2:-1])
                str_data = str_data.replace(old_value, new_value)
                # print(f"参数{old_value}进行替换后的值:{new_value}")
        # 还原数据类型
        if isinstance(data, dict) or isinstance(data, list):
            data = json.loads(str_data)
            for k, v in data.items():
                if isinstance(v, str) and v.isdigit():
                    data[k] = int(v)
        else:
            data = data_type(str_data)
        return data

    def send_request(self, method, url, datas=None, **kwargs):
        method = str(method).lower()  # 转换小写
        url = self.base_url + url
        # print(kwargs)  **kwargs是个dict
        for key, value in kwargs.items():
            if key in ['body', 'header']:
                kwargs['body']['payload'] = self.replace_str(kwargs['body']['payload'])
        if method == 'post':
            res = RequestUtil.sess.request(method, url, json=kwargs)
        else:
            res = RequestUtil.sess.request(method, url, params=kwargs)
        # print(res.request.body)
        return res

    def standard_yaml(self, caseinfo):
        caseinfo_keys = caseinfo.keys()
        if 'method' in caseinfo_keys and 'body' in caseinfo_keys:
            body_keys = caseinfo['body']['body'].keys()
            if 'cmd' in body_keys and 'client' in body_keys and 'payload' in body_keys:
                print("yaml文件结构检查正确")
                method = caseinfo['method']
                cmd = caseinfo['body']['body']['cmd']
                res = self.send_request(method=method, url=cmd, **caseinfo['body'])
                return_text = res.text
                if 'extract' in caseinfo.keys():
                    for k, v in caseinfo['extract'].items():
                        if "(.*?)" in v or "(.+?)" in v or "(\\d+)" in v:
                            zz_value = re.search(v, return_text)
                            if zz_value:
                                extract_value = {k: zz_value.group(1)}
                                YamlUtil().write_yaml(extract_value)

        res_text = json.loads(return_text)
        return res_text

    def close_session(self):
        self.session.close()
