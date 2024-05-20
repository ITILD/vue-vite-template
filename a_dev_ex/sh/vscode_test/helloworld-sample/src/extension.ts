// The module 'vscode' contains the VS Code extensibility API
// Import the module and reference it with the alias vscode in your code below
import * as vscode from "vscode";

// this method is called when your extension is activated
// your extension is activated the very first time the command is executed
export function activate(context: vscode.ExtensionContext) {
  // Use the console to output diagnostic information (console.log) and errors (console.error)
  // This line of code will only be executed once when your extension is activated
  console.log(
    'Congratulations, your extension "helloworld-sample" is now active!'
  );

  // The command has been defined in the package.json file
  // Now provide the implementation of the command with registerCommand
  // The commandId parameter must match the command field in package.json
  const disposable = vscode.commands.registerCommand(
    "extension.helloWorld",
    () => {
      // The code you place here will be executed every time your command is executed

      // Display a message box to the user
      vscode.window.showInformationMessage("Hello World!!");
    }
  );
  openFileAndInsertText();
  context.subscriptions.push(disposable);
}

async function openFileAndInsertText() {
  const filePath = "D:/github/geogpu/code-template/a_dev_ex/sh/vscode_test/helloworld-sample/src/test.js";

  const uri = vscode.Uri.file(filePath);
  const doc = await vscode.workspace.openTextDocument(uri);
  await vscode.window.showTextDocument(doc);

  // 获取当前文档
  const activeEditor = vscode.window.activeTextEditor;
  if (activeEditor) {
    const document = activeEditor.document;

    // 创建修改编辑器内容的操作
    const edit = new vscode.WorkspaceEdit();

    // 在指定位置插入文本
    const position = new vscode.Position(0, 0); // 在第一行第一列插入
    edit.insert(document.uri, position, "插入的文本");

    // 应用操作
    await vscode.workspace.applyEdit(edit);
  }
}
