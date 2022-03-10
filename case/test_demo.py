import json
from uuid import uuid4

import pytest

from config.conf import ConfigReader
from utils.AssertUtil import AssertUtil
from utils.requestsUtil import RequestUtil


# url = 'https://v2test.tsepcn.com/api/access/pb/cmd/GetBannerList'

class TestGetBannerList():
    # self.log = my_log(log_name="TestGetBannerList")

    def test_GetBannerList(self):
        url = ConfigReader().get_conf_url()
        path = ConfigReader().get_conf_path()
        token = ConfigReader().get_conf_token()
        body = ConfigReader().get_conf_body()
        body['body']['cmd'] = "GetBannerList"
        body['body']['token'] = token
        body['body']['payload'] = {
            "entry_type": 1,
            "page_index": 1,
            "page_size": 10
        }

        rsp = RequestUtil().visit(method="POST", url=url+path, json=body)
        rsp = json.loads(rsp.text)
        AssertUtil().assertCommon(rsp)
