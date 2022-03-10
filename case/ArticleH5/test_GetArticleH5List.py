import json

import allure
import pytest

from config.conf import ConfigReader
from utils.AssertUtil import AssertUtil
from utils.requestsUtil import RequestUtil


@allure.feature("H5文章管理")
class TestGetArticleH5List():
    @allure.title("读取h5列表")
    @allure.severity("nomal")
    def test_GetArticleH5List(self, req_url, req_token):
        body = ConfigReader().get_conf_body()
        body['body']['cmd'] = "GetArticleH5List"
        body['body']['token'] = req_token
        body['body']['payload'] = {
            "status": 0,
            "keyword": "",
            "page_index": 1,
            "page_size": 10
        }
        # print(body)
        rsp = RequestUtil().visit(method="POST", url=req_url, json=body)
        rsp = json.loads(rsp.text)
        AssertUtil().assertCommon(rsp)
