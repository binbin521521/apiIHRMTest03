import requests
import app


class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        # 注意：如果我们调用员工管理模块的相关接口时，先调用 login.py 接口
        # 获取到的 app.HEADERS 才会是 {'Content-Type': 'application/json', 'Authorization': 'Bearer xxxx-xxx-xxxxx'}
        self.headers = app.HEADERS

    def add_emp(self, username, mobile):
        """ 封装 添加员工接口 """
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-07",
            "formOfEmployment": 1,
            "workNumber": "67679879",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-01-29T16:00:00.000Z",
        }
        # 发送 添加员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回添加员工接口的响应数据
        return response

    # 封装查询员工接口
    # def query_emp(self):
    #     url = self.emp_url+app.EMP_ID
    #     return requests.get(url)

    def query_emp(self):
        """ 封装 查询员工接口 """

        # 查询员工接口的 URL 结构是 http://182.92.81.159/api/sys/user/12344343221
        # 所以 拼接 URL 时需要加上 “ / "
        url = self.emp_url + "/" + app.EMP_ID
        # 返回查询的结果，headers是 {'Content-Type': 'application/json', 'Authorization': 'Bearer xxxx-xxx-xxxxx'}
        return requests.get(url, headers=self.headers)

    def modify_emp(self, username):
        """ 封装 修改员工接口 """

        # 修改员工的 URL 应该和查询员工是一样的，所以拼接的时候也需要加上 " / "
        #  URL 结构是 http://182.92.81.159/api/sys/user/12344343221

        url = self.emp_url + "/" + app.EMP_ID
        # 从外部接收要修改的 username ，拼接成 json 数据
        data = {
            "username": username
        }
        # 返回 查询 的结果，headers是 {'Content-Type': 'application/json', 'Authorization': 'Bearer xxxx-xxx-xxxxx'}
        return requests.put(url,
                            json=data,
                            headers=self.headers)

    def delete_emp(self):
        # 封装 删除员工接口

        # 删除员工的 URL 应该和查询员工是一样的，所以拼接的时候也需要加上 " / "
        #  URL 结构是 http://182.92.81.159/api/sys/user/12344343221

        url = self.emp_url + "/" + app.EMP_ID

        # 调用删除的 HTTP 接口 并返回
        return requests.delete(url, headers=self.headers)
