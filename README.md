# Use GitPython Lambda

AWS LambdaでGitPythonを使う。

## 準備

``` sh
pip install GitPython -t ./GitPython
pip install python-dotenv -t ./python-dotenv
```

## 動作確認

``` sh
python3
```

``` python
from lambda_function import lambda_handler
lambda_handler(None, None)
```

## zip作成

``` sh
zip -r upload.zip *
```

## 参考

- [Pythonからgitの操作:iMind Developers Blog](https://blog.imind.jp/entry/2020/01/18/065638)
- [【AWS】Lambdaでpipしたいと思ったときにすべきこと:Qiita](https://qiita.com/Hironsan/items/0eb5578f3321c72637b4)
