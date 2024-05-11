
import os
def run(self):
    """
    开始构建
    :return:
    """
    upx_path = os.path.abspath("tools/upx")
    cmd = f"nuitka3 --mingw64  --clang --show-progress --disable-ccache --plugin-enable=pyqt5,upx --upx-binary={upx_path} --output-dir=out  --include-package=model main5.py"
    print(cmd)
    if int(os.system(cmd)) == 0:
        print("构建成功")
    else:
        print("构建失败")
        exit(5)
