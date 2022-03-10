#封装请求方法
import json

import requests

from utils.LogUtil import Mylog


class RequestUtil():

    def __init__(self):
        # self.log = Mylog(log_name="RequestUtil").getLog()
        self.session = requests.session()

    # def request_get(self,url,data):
    #     self.log.info("开始get请求")
    #     r = requests.get(url=url,data=data)
    #     try:
    #         if r.status_code == 200:
    #             res = r.json()
    #             return res
    #         else:
    #             return None
    #     except requests.RequestException:
    #         print("请求失败")
    #         return None
    #
    # def request_post(self,url,data):
    #     self.log.info("开始post请求")
    #     r = requests.post(url=url,data=data)
    #     try:
    #         if r.status_code == 200:
    #             res = r.json()
    #             return res
    #         else:
    #             return None
    #     except requests.RequestException:
    #         print("请求失败")
    #         return None
    #
    # def api_request(self,method,url,data):
    #     if method == "GET":
    #         res = self.request_get(url=url,data=data)
    #     elif method == "POST":
    #         res = self.request_post(url=url,data=data)
    #     else:
    #         raise
    #     return res

    def visit(self,method,url,params=None,data=None,json=None,headers=None,**kwargs):
        return self.session.request(method=method,url=url,params=params,data=data,json=json,headers=headers,**kwargs)

    def close_session(self):
        self.session.close()
