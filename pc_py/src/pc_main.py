# 把当前文件所在文件夹的父文件夹路径下main所在src加入到PYTHONPATH
import sys
import os
parent_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",".."))
sys.path.append(os.path.join(parent_path,'server_py','src'))
print(parent_path)

# 验证引入成功
from config.path import path_html
print(path_html,__name__)

# 启动
if __name__ == "__main__":
    '''server'''
    from main import *
    from main import app,console
    import uvicorn
    import threading
    from pc_util import port_ex
    port = port_ex.get_unused_port()
    # 启动FastAPI服务 daemon守护线程,整个python程序退出时自动卸载
    threading.Thread(target=uvicorn.run, args=(app,), kwargs={"host":"localhost","port": port,"reload":"True"},daemon=True).start()
    '''pc'''
    import webview
    webview.create_window('pc', f'http://localhost:{port}')
    webview.start()
    console.log("pc:启动器...{port}")


