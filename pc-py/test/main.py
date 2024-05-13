import webview

if __name__ == '__main__':
    # Create a resizable webview window with minimum size constraints
    webview.create_window('Frameless window', 'http://pywebview.flowrl.com/hello',
                          frameless=True, easy_drag=True)
    webview.start()