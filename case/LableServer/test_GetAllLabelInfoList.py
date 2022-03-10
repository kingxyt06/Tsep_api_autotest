import json

import allure
import pytest

from config.conf import ConfigReader
from utils.AssertUtil import AssertUtil
from utils.requestsUtil import RequestUtil


@allure.feature("标签管理")
class TestGetAllLabelInfoList():
    @allure.title("获取全部标签列表信息")
    @allure.description("""
    这是一个@allure.description装饰器
    没有特别的用处
    """)
    @allure.severity("normal")
    def test_GetAllLabelInfoList(self, req_url, req_token):
        body = ConfigReader().get_conf_body()
        body['body']['cmd'] = "GetAllLabelInfoList"
        body['body']['token'] = req_token
        body['body']['payload'] = {}
        # print(body)
        rsp = RequestUtil().visit(method="POST", url=req_url, json=body)
        rsp = json.loads(rsp.text)
        AssertUtil().assertCommon(rsp)



