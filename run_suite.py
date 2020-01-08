import time
import unittest
import app

# 导入登陆和员工管理
from script.login import Login
from script.test_emp import TestIHRMEmp

from script.test_login import TestIHRMLogin
from tools.HTMLTestRunner import HTMLTestRunner

# 1.初始化测试套件
suite = unittest.TestSuite()

# 2.将测试用例添加到测试套件

suite.addTest(unittest.makeSuite(Login))  # 添加 登陆测试用例
suite.addTest(unittest.makeSuite(TestIHRMEmp))  # 添加员工增删改查 用例

# suite.addTest(unittest.makeSuite(TestIHRMLogin))

# 3.使用HTMLtestRunner执行测试套件，生成测试报告
# report_path = app.BASE_DIR + "/report/ihrm{}.html".format(time.strftime('%Y%m%d %H%M%S'))
 report_path = app.BASE_DIR + "/report/ihrm.html")
with open(report_path, mode='wb') as f:
    # 初始化HTMLtestRunner
    runner = HTMLTestRunner(f, verbosity=1, title="IHRM人力资源接口测试", description="V1.0.0")
    # 使用runner运行测试套件
    runner.run(suite)
