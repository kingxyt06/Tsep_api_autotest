import datetime
import logging
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
print(rootPath)
sys.path.append(rootPath)
from config.conf import BASE_DIR, ConfigReader

log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


# 封装日志类
class Mylog():
    # 初始化方法，传入初始化日志记录器所需要的参数，级别，格式等
    def __init__(self,
                 log_name='root'
                 ):

        self.log_name = log_name
        log_path = BASE_DIR + os.sep + 'logs'
        current_time = datetime.datetime.now().strftime("%Y-%m-%d")
        conf = ConfigReader().get_conf_all()
        file_extension = conf['BASE']['log']['file_extension']
        self.log_file = os.path.join(log_path, current_time + file_extension)
        self.log_level = conf['BASE']['log']['level']
        self.log_format = conf['BASE']['log']['format']


        # 设置日志收集器
        self.logger = logging.getLogger(self.log_name)
        self.logger.setLevel(log_l[self.log_level])

        f1 = logging.Formatter(self.log_format)
        # 如果文件存在，设置文件处理器输入日志到文件
        if self.log_file:
            file_handler = logging.FileHandler(filename=self.log_file, encoding='utf-8')
            file_handler.setFormatter(f1)
            file_handler.setLevel(log_l[self.log_level])
            self.logger.addHandler(file_handler)

        # 设置输出日志到控制台
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(log_l[self.log_level])
        stream_handler.setFormatter(f1)
        self.logger.addHandler(stream_handler)

    def getLog(self):
        return self.logger


# 获取日志文件的路径
# log_path = BASE_DIR + os.sep + 'logs'
# current_time = datetime.datetime.now().strftime("%Y-%m-%d")
# conf = ConfigReader().get_conf_all()
# file_extension = conf['BASE']['log']['file_extension']
# log_file = os.path.join(log_path,current_time+file_extension)
# log_level = conf['BASE']['log']['level']
# log_format = conf['BASE']['log']['format']
# def my_log(log_name=__file__):
#     return Mylog(log_name=log_name,log_level=log_level,log_format=log_format,log_file=log_file).logger

# #读取yaml中的日志配置
# conf = ConfigReader().get_conf_all()
# name = conf['BASE']['log']['name']
# level = conf['BASE']['log']['level']
# format = conf['BASE']['log']['format']
# #供外部直接调用
# mylog = Mylog(name=name,level=level,format=format,file=log_file)


if __name__ == "__main__":
    test_log = Mylog(log_name="test")
    test_log.getLog().info("好了吗")
    print(test_log.log_file)
    # res = ConfigReader().get_conf_all()
    # name = res['BASE']['log']['name']
    # level = res['BASE']['log']['level']
    # format = res['BASE']['log']['format']
    #
    # mylog = Mylog(name,level,format=format,file=log_file)
    # mylog.info("1------info------")
    # mylog.debug("2------debug------")
