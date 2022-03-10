import json

import allure

from utils.LogUtil import Mylog


class AssertUtil(object):
    # def __init__(self):
    #     self.log = Mylog(log_name="AssertUtil").getLog()
    log = Mylog(log_name="AssertUtil").getLog()

    def assertCommon(self, rsp):
        try:
            assert rsp['body']['bizcode'] == 0
            assert rsp['body']['retcode'] == 0
            self.log.info("响应json======⬇️⬇️ \n" + json.dumps(rsp).encode('utf-8').decode('unicode_escape') + '\n')
        except:
            self.log.error("公共断言失败,接口返回码错误")
            raise AssertionError
