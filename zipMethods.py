import sqlite3

# データベースを開く
conn = sqlite3.connect('zip.sqlite3')
cur = conn.cursor()

# 郵便番号から関数
def zip2addr(zipno_in):
    cur.execute('SELECT * FROM zip WHERE zipno=?', [zipno_in])
    r = cur.fetchone()
    return r

def addr2zip(ken_in, shi_in, cho_in):
    cur.execute('SELECT * FROM zip WHERE ken=? AND shi=? AND cho=?', [ken_in, shi_in, cho_in])
    r = cur.fetchone()
    return r

"""
# デバッグ用
if __name__ == '__main__':
    print(zip2addr('8190385')) 
    print(addr2zip('東京都', '港区', '芝公園'))
"""