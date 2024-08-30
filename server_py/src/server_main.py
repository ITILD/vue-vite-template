# self
from config.log import console
from config.fastapi_config import app
# import config
from config import db,fastapi_config,path,log,index

from controller import index,user,utils,ws
# lib

console.log("...依赖引入完成")

if __name__ == "__main__":
    print('pc_main',path.path_html,__name__)
    # 发布时server  开发时在.vscode目录下launch.json配置
    import uvicorn
    console.log("server:starting port")
    uvicorn.run(app, host="127.0.0.1", port=1767)
    # uvicorn.run(app, host="0.0.0.0", port=1767)
