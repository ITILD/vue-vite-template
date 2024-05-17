# 获取当前脚本文件的绝对路径
import os

current_script_path = os.path.abspath(__file__)

# 获取当前脚本所在目录的父目录的父目录的路径
path_base = os.path.dirname(os.path.dirname(os.path.dirname(current_script_path)))

# config 
path_config = os.path.join(path_base, 'source','config','logging.ini' )

# html
path_html = os.path.join(path_base, 'source','html')