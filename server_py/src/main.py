# self
from config.log import console
from config.fastapi_config import app
# import config
from config import *
from controller import *
# lib

console.log("...依赖引入完成")

if __name__ == "__main__":
    # 发布时server  开发时在.vscode目录下launch.json配置
    import uvicorn
    console.log("starting port")
    uvicorn.run(app, host="127.0.0.1", port=1667)
