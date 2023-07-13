import os  # os: ファイルパスや環境変数など、オペレーティングシステムに依存する機能を提供するモジュール。
from playhouse.db_url import connect  # データベースのURL形式で接続するためのユーティリティ関数を提供。playhouseにはpeeweeで使う便利関数が入っている
from dotenv import load_dotenv  # .envファイルから環境変数を読み込むためのライブラリです。
from peewee import Model, IntegerField, CharField

# .envの読み込み
load_dotenv()

# データベースへの接続設定、.envファイルに設定されている環境変数DATABASEの値を取得
db = connect(os.environ.get("DATABASE"))

# 接続NGの場合はメッセージを表示
if not db.connect():
    print("接続NG")
    exit()


# ユーザーテーブルのモデル
class User(Model):
    """User Model"""

    id = IntegerField(primary_key=True)
    user = CharField()
    age = IntegerField()

    class Meta:
        database = db  # database属性に、先に定義したデータベースオブジェクトdbを指定
        table_name = "users"  # table_name属性にテーブルの名前を指定


db.create_tables([User])  # データベース内にUserモデルに対応するテーブルを作成
