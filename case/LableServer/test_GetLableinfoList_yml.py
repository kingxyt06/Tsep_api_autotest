import pytest
from utils.AssertUtil import AssertUtil
from utils.YamlUtil import read_testcase
from utils.requestsUtil import RequestUtil


class TestGetAllLabelInfoList:
    pass
    # 标签列表接口
    # @pytest.mark.parametrize("caseinfo", read_testcase("GetLabelInfoList.yaml"))
    # def test_GetLabelInfoList_yml(self, caseinfo):
    #     rsp = RequestUtil().standard_yaml(caseinfo)
    #     AssertUtil().assertCommon(rsp)
    #
    # # 标签详情接口
    # @pytest.mark.parametrize("caseinfo", read_testcase("GetLabelDetail.yaml"))
    # def test_GetLabelDetail(self, caseinfo):
    #     rsp = RequestUtil().standard_yaml(caseinfo)
    #     AssertUtil().assertCommon(rsp)
