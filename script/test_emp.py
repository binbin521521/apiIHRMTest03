import logging
import unittest

import pymysql

import app
from api.emp_api import EmpApi
from utils import assert_common, DBUtils
from utils import read_add_emp_data, read_query_emp_data
from utils import read_modify_emp_data, read_delete_emp_data

from parameterized.parameterized import parameterized


class TestIHRMEmp(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化员工表
        cls.emp_api = EmpApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self, username, mobile, success, code, message, http_code):
        """ 增加新员工 """

        # 调用添加员工接口
        response = self.emp_api.add_emp(username, mobile)
        jsonData = response.json()
        # 输出 json 数据
        logging.info("添加员工接口返回的数据为:{}".format(jsonData))

        # 获取 员工ID 保存在全局变量
        app.EMP_ID = jsonData.get("data").get("id")
        logging.info("员工ID： {}".format(app.EMP_ID))

        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_query_emp_data)
    def test02_query_emp(self, success, code, message, http_code):
        """ 查询新员工 """

        # 调用添加员工接口
        response = self.emp_api.query_emp()
        # 获取 查询员工接口的返回 json 数据
        jsonData = response.json()
        # 输出 json 数据
        logging.info("查询员工接口的返回数据为:{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_modify_emp_data)
    def test03_modify_emp(self, username, success, code, message, http_code):
        """ 修改新员工 """

        # 调用添加员工接口
        response = self.emp_api.modify_emp(username)
        # 获取 修改 员工接口的返回 json 数据
        jsonData = response.json()
        # 输出 json 数据
        logging.info("修改员工接口的返回数据为:{}".format(jsonData))

        # # 建立连接
        # conn = pymysql.connect("182.92.81.159", "readuser", "iHRM_user_2019", 'ihrm')
        # # 获取游标
        # cursor = conn.cursor()
        # # 执行查询语句，查询出添加的员工的 username 是不是修改的 username
        # sql = "select username from bs_user where id={}".format(app.EMP_ID)
        # cursor.execute(sql)
        # # 获取执行结果
        # result = cursor.fetchone()[0]
        # logging.info("从数据库中查询出的员工的用户名是:{}".format(result))
        # self.assertEqual(username, result)

        with DBUtils() as db_utils:
            # 执行查询语句，查询出添加的员工的 username 是不是修改的 username
            sql = "select username from bs_user where id={}".format(app.EMP_ID)
            db_utils.execute(sql)
            # # 获取执行结果
            result = db_utils.fetchone()[0]
            logging.info("从数据库中查询出的员工的用户名是:{}".format(result))

            # 断言
            assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_query_emp_data)
    def test04_query_emp(self, success, code, message, http_code):
        """ 查询 修改后 新员工名字 """

        # 调用添加员工接口
        response = self.emp_api.query_emp()
        # 获取 查询员工接口的返回 json 数据
        jsonData = response.json()
        # 输出 json 数据
        logging.info("查询员工接口的返回数据为:{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(read_delete_emp_data)
    def test05_delete_emp(self, success, code, message, http_code):
        """ 删除 新员工 """

        # 调用添加员工接口
        response = self.emp_api.delete_emp()
        # 获取 修改 员工接口的返回 json 数据
        jsonData = response.json()
        # 输出 json 数据
        logging.info("删除员工接口的返回数据为:{}".format(jsonData))
        # 断言
        assert_common(self, response, http_code, success, code, message)
