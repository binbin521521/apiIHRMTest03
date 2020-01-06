# 编写初始化日志的函数
import logging
import os
from logging import handlers

# 相当于 postman 的全局变量，文件地址优化
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type": "application/json"}
EMP_ID = " "


def init_logging():
    # 创建日志器
    logger = logging.getLogger()
    # 设置日志等级
    logger.setLevel(logging.INFO)
    # 设置处理器
    # 设置控制台处理器
    sh = logging.StreamHandler()
    # 设置文件处理器
    # TimedRotatingFileHandler 可以用来帮助我们切分日志：按照时间来设置日志
    # __file__ :在哪个文件夹就表示当前文件 的 绝对路径
    filename = BASE_DIR + "/log/ihrm.log"
    # （when="M" ：分   interval=1 ：间隔时间 生成新文件   backupCount=7 :文件数量 ）：最大积累到7个文件时，最后一个覆盖第一个
    fh = logging.handlers.TimedRotatingFileHandler(filename, when="M", interval=1, backupCount=7)
    # 设置格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器当中
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)
