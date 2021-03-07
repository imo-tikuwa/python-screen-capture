# python-screen-capture
PowerAutomateで呼び出すプログラム

## 環境構築
クローンしたらvenvの環境構築
```
python -m venv venv
.\venv\Scripts\activate.bat
pip install -r requirements.txt
.\venv\Scripts\deactivate.bat
```

## 動作確認
以下のような感じでスクリーンショット取れてればOK
```
.\venv\Scripts\activate.bat
python app.py C:\temp "0, 0, 646, 509"
```

## メモ
PowerAutomateでタスクを実行する際、他のプロセスでvenvは起動してない方がいいかもしれない？？
