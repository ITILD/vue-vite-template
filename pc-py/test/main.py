import webview

class Api:
    def getMessage(self):
        return 'Hello from the Python backend!'

def main():
    api = Api()
    webview.create_window('Pywebview Example', 'index.html', js_api=api, width=800, height=600)
    webview.start()

if __name__ == '__main__':
    main()
