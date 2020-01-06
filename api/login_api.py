import requests
import app


class LoginApi:
    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    # 从外部接收 mobile password
    # 为什么这么写？  这是因为如果写成一个参数 data 来接收字典数据的话
    # 那么后续进行参数化时，会很不方便，所以改成接收 两个变量
    def login(self, mobile, password):
        # 使用 data 来接收外部传入的 Mobile 和 password，拼接成要发送的数据
        data = {
            "mobile": mobile,
            "password": password
        }
        # 发送登陆请求
        response = requests.post(self.login_url,
                                 json=data,
                                 headers=self.headers)
        # 返回响应数据
        return response
