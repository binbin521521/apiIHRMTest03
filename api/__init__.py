import app
import logging

# 初始化日志
# 为什么要在 api.__init__.py 中初始化日志？
# 这是因为，我们后面进行接口测试时，都会调用封装的 API 接口，调用时，会自动运行 __init__.py
# 从而实现，自动初始化日志的功能
app.init_logging()

logging.info("TEST日志器能不能正常工作")
