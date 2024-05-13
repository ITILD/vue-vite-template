import webview
class Api:
    def select_dir(self):  # 选择目录
        result = window.create_file_dialog(webview.FOLDER_DIALOG)
        print(result)
        return result[0] if result else ''

    def select_file(self):  # 选择文件
        file_types = ('Image Files (*.bmp;*.jpg;*.gif;*.png)', 'All files (*.*)')
        result = window.create_file_dialog(webview.OPEN_DIALOG, allow_multiple=True, file_types=file_types)
        print(result)
        return result[0] if result else ''

    def test_argcs(self, arg1, arg2, arg3):  # 测试传入多参数，模拟耗时请求
        print(arg1, arg2, arg3)
        import time
        time.sleep(3)

        return '返回结果：{0},{1},{2}'.format(arg1, arg2, arg3)
api = Api()
window = webview.create_window('pywebview中html和python交互的例子', 'dist_ui/index.html', js_api=api)
webview.start(ssl=True)
