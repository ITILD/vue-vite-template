import webview

html = """
<!doctype html>
<html lang="en">
	<head>
		<meta charset="utf-8">
        <title>Test app</title>
        <style>
            .frame {
                width: 100%;
                height: 100%;
                background-color: rgba(255, 255, 255);
                border: none;
                padding: 0;
                margin: 0;
            }
          
        </style>
	</head>
	<body>
        <div class="frame">test</div>
        <div class='frame pywebview-drag-region'>This div element can be used to moved or drag your window like a native OS window</div>
	</body>
</html>
"""

if __name__ == '__main__':
    # Create a transparent webview window
    # webview.create_window('Transparent window', html=html, transparent=True, frameless=True)
    webview.create_window('Transparent window', 
                          html=html, frameless=True, easy_drag=False,on_top=True
                        #   transparent=True,#   windows无效,无法点击
        )
    # webview.create_window('Transparent window', html=html, transparent=True)
    webview.start()