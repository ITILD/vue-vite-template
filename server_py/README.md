## server

## 开发备注

### conda 环境

```sh
conda env list
# 添加源
conda config --append channels conda-forge

# 初始环境
conda create -n test_all python=3.10 

# 进入环境
conda activate test_all
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
# 导入 test_all
conda env create -f environment.yml -n test_all
# 把环境 rcnn 重命名成 tf
conda create -n tf --clone rcnn
conda remove -n rcnn --all 

```

### 设置 launch.json debug

```sh
# 进入环境
conda activate test_all
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
            // linux
            "python":"/opt/conda/envs/test_all/bin/python",
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
