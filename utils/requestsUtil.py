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

    def send_request(self, method, url, datas=None, **kwargs):
        method = str(method).lower()  # 转换小写
        url = self.base_url + url
        # **kwargs是个dict
        # print(kwargs)
        res = RequestUtil.sess.request(method, url, json=kwargs)
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
