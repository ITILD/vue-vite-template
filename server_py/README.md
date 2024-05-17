## server

## 开发备注

### conda 环境

```sh
conda env list
# 添加源
conda config --append channels conda-forge

# 初始环境
conda create -n server_py python=3.10 

# 进入环境
conda activate server_py
```

### lib

```sh
# server
conda install uvicorn
# web框架
conda install fastapi
# 数据库对象和程序对象序列化反序列化关联    SQLModel 基于 Pydantic(自动安装) 和 SQLAlchemy(自动安装)
conda install sqlmodel
# 上传文件等
conda install python-multipart
# 异步sqlite aiofiles
conda install aiosqlite aiofiles
# full server
conda install uvicorn fastapi sqlmodel python-multipart aiosqlite aiofiles

# 导出
conda env export > environment.yaml
```

### 设置 launch.json debug

```sh
# 进入环境
conda activate server_py
# 查看python 路径 
which python # linux
where.exe python # windows
```
路径放在.vscode/launch.json下python

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: FastAPI",
            "type": "python",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "src.main:app", "--reload","--port", "1667"
            ],
            "python":"/opt/conda/envs/server_py/bin/python",
            "jinja": true,
            "justMyCode": true,
            "env": {"PYTHONPATH": "${workspaceRoot}/src"}
        }
    ]
}
```

### 调试

vscode debug
或
npm activate_env
