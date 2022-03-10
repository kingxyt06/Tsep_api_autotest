import json
import time

import allure
import pytest

from config.conf import ConfigReader
from utils.AssertUtil import AssertUtil
from utils.requestsUtil import RequestUtil


@allure.feature("标签管理")
class TestGetLabelInfoList():
    @allure.title("查询标签列表")
    @allure.severity("normal")
    def test_GetLabelInfoList(self, req_url, req_token):
        body = ConfigReader().get_conf_body()
        body['body']['cmd'] = "GetLabelInfoList"
        body['body']['token'] = req_token
        body['body']['payload'] = {
            "label_name": "30",
            "label_type": "30",
            "status": "30",
            "page_index": 1,
            "page_size": 9999
        }
        # print(body)
        rsp = RequestUtil().visit(method="POST", url=req_url, json=body)
        rsp = json.loads(rsp.text)
        AssertUtil().assertCommon(rsp)
