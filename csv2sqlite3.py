import csv, sqlite3

def make_sqlite3():
  # SQLite3のデータベースを開く
  conn = sqlite3.connect('zip.sqlite3')
  c = conn.cursor()
  # テーブルを作る
  # テーブルを作成
  c.execute("SELECT * FROM sqlite_master WHERE type='table' and name='zip'")
  if not c.fetchone():
    c.execute('''CREATE TABLE zip (
        zipno text, ken text, shi text, cho text)''')
    c.execute('begin')
    # CSVファイルを開く
    with open('KEN_ALL.CSV', 'rt', encoding='Shift_JIS') as fp:
      # CSVを読み込む
      reader = csv.reader(fp)
      # 一行ずつ処理する
      for row in reader:
        zipno = row[2] # 郵便番号
        ken = row[6] # 都道府県
        shi = row[7] # 市区
        cho = row[8] # 市区以下
        if cho == '以下に掲載がない場合': cho = ''
        # SQLiteに追加
        c.execute('''INSERT INTO zip (zipno,ken,shi,cho)
          VALUES(?,?,?,?)''', (zipno,ken,shi,cho))
    # データベースを閉じる
    c.execute('commit')
    conn.close()
  print("[ZIP Database] zip.sqlite3 has got ready!\n")