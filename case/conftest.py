import pytest

import allure

from config.conf import ConfigReader
from utils.YamlUtil import YamlUtil
from utils.requestsUtil import RequestUtil

token = ConfigReader().get_conf_token()
url = ConfigReader().get_conf_url()
path = ConfigReader().get_conf_path()


#在所有的接口请求之前执行
# @pytest.fixture(scope="session",autouse=True)
# def clear_extract():
#     YamlUtil().clear_yaml()

@allure.title("前置步骤----开始获取请求域名")
@pytest.fixture(scope="module")
def req_url():
    print("\n前置步骤----开始获取请求域名")
    url = ConfigReader().get_conf_url()
    # path = ConfigReader().get_conf_path()
    # req_url = url + path
    return url


@allure.title("前置步骤----开始获取token")
@pytest.fixture(scope="module")
def req_token():
    print("\n前置步骤----开始获取token")
    token = ConfigReader().get_conf_token()
    return token


@pytest.fixture(scope="function")
@allure.title("\n前置步骤----获取标签id")
def get_label_id():
    print("\n前置步骤----获取标签id")
    req_body = {
        "header": {
            "version": 2,
            "flag": 0
        },
        "body": {
            "seq": 0,
            "cmd": "GetAllLabelInfoList",
            "token": token,
            "traceid": "b28fd0bb-8203-4300-8143-e83e1a4cee05",
            "client": {
                "platform": 1,
                "os": 0,
                "env": "",
                "isTourist": 49,
                "adtag": "tsep.test",
                "product": "12",
                "vnk": "1646729529888"
            },
            "payload": {}
        }
    }
    rsp = RequestUtil().visit(method="POST", url=url, json=req_body)
    rsp = rsp.json()
    print(rsp)
    labelid = rsp['body']['payload']['LabelGroupList'][0]['LabelList'][0]['Id']
    return labelid



