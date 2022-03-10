import json

import allure
import pytest

from config.conf import ConfigReader
from utils.AssertUtil import AssertUtil
from utils.requestsUtil import RequestUtil


@allure.feature("标签管理")
class TestGetLabelDetail():

    @allure.title("标签详情")
    @allure.severity("normal")
    def test_GetLabelDetail(self, req_url, req_token, get_label_id):
        body = ConfigReader().get_conf_body()
        body['body']['cmd'] = "GetLabelDetail"
        body['body']['token'] = req_token
        body['body']['payload'] = {'id': get_label_id}
        rsp = RequestUtil().visit(method="POST", url=req_url, json=body)
        rsp = json.loads(rsp.text)
        AssertUtil().assertCommon(rsp)
