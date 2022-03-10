from utils.AssertUtil import AssertUtil
from utils.LogUtil import Mylog

class Base:
    def init_log(self,name):
        self.log = Mylog().mylog(name)
        return self.log