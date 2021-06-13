import zipfile
import urllib.error
import urllib.request
import os
 
# 指定URL（第1引数）からファイルを取得して、指定パス（第2引数）に保存する
def file_download_unzip():
    url = "https://www.post.japanpost.jp/zipcode/dl/kogaki/zip/ken_all.zip"
    data_dir_path = "./"
    save_path = data_dir_path + "download.zip"
    try:
        """
        if os.path.exists('KEN_ALL.CSV'):
            os.remove('./KEN_ALL.CSV')
        """
        with urllib.request.urlopen(url) as download_file:
            data = download_file.read()
            with open(save_path, mode='wb') as save_file:
                save_file.write(data)
            with zipfile.ZipFile('download.zip', 'r')as f:
                f.extractall()
            os.remove('./download.zip')
            print("[ZIP Database] KEN_ALL.CSV has been downloaded!\n")

    except urllib.error.URLError as e:
        print(e)

"""
# デバッグ用
if __name__ == "__main__":
 
    data_dir_path = "./"
    zip_file_path = data_dir_path + "download.zip"
 
    # zip取得
    file_download_unzip()
"""