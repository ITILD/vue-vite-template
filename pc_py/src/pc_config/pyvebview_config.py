'''webview初始化'''
# self
from pc_util.port_ex import port_no_used
# pc_api
from pc_util.routes import Api
# lib
import webview

#  pc路由
api = Api()
window = webview.create_window('pc', f'http://localhost:{port_no_used}',js_api=api)



print('...pc服务配置完成')