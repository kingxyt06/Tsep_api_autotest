import json

import allure
import pytest

from config.conf import ConfigReader
from utils.AssertUtil import AssertUtil
from utils.requestsUtil import RequestUtil


@allure.feature("标签管理")
class TestGetLabelClass():
    @allure.title("查询标签分类列表")
    @allure.severity("nomal")
    def test_GetLabelClass(self, req_url, req_token):
        body = ConfigReader().get_conf_body()
        body['body']['cmd'] = "GetLabelClass"
        body['body']['token'] = req_token
        body['body']['payload'] = {}
        # print(body)
        rsp = RequestUtil().visit(method="POST", url=req_url, json=body)
        rsp = json.loads(rsp.text)
        AssertUtil().assertCommon(rsp)
