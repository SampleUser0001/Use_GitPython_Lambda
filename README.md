# Use GitPython Lambda

AWS LambdaでGitPythonを使う。

## 準備

``` sh
pip install GitPython -t ./GitPython
pip install python-dotenv -t ./python-dotenv
```

## ローカルで動かす

lambda_function.pyの

ここを
``` python
  t = repo.head.commit.tree
  # print(repo.git.diff('HEAD^'))

  return {
    'statusCode': 200,
    'body': repo.git.diff('HEAD^')
  }
```

こう修正する。
``` python
  t = repo.head.commit.tree
  print(repo.git.diff('HEAD^'))

  # return {
  #   'statusCode': 200,
  #   'body': repo.git.diff('HEAD^')
  # }
```


``` sh
python3
```

``` python
from lambda_function import lambda_handler
lambda_handler(None, None)
```

## AWS Lambdaへリリース

### zip作成

repo配下に```.gitkeep```ファイル以外が存在しないことを確認しておくこと。

``` sh
zip -r upload.zip *
```

### Upload

1. アップロード元 -> .zipファイル -> 作成したupload.zipファイルをupload。
2. 環境変数設定
    - 設定 -> 環境変数 -> 編集を押下。
      - キー：GIT_PYTHON_REFRESH
      - 値：quiet

## 参考

- [Pythonからgitの操作:iMind Developers Blog](https://blog.imind.jp/entry/2020/01/18/065638)
- [【AWS】Lambdaでpipしたいと思ったときにすべきこと:Qiita](https://qiita.com/Hironsan/items/0eb5578f3321c72637b4)
