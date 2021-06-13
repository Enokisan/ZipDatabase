import csv2sqlite3
import ken_alldl
import zipMethods

def main():
    while True:
        query_num = int(input("[ZIP Database] What do you want? type {0:quit, 1:search from zipcode, 2:seacrh from area, 3:download csv and create table}\n"))
        if query_num == 0:
            print("[ZIP Database] End. Bye-bye!\n")
            break
        
        elif query_num == 1:
            print("[ZIP Database] Search from zipcode.\n")
            which_data = int(input("[ZIP Database] type zipcode number or {0:back}\n"))
            if which_data == 0:
                print("[ZIP Database] Back.\n")
                continue
            elif len(str(which_data)) == 1:
                print("[ZIP Database] Query {} is not supported!\n".format(which_data))
                continue
            else:
                print("[ZIP Database] "+str(zipMethods.zip2addr(which_data))+"\n")
        
        elif query_num == 2:
            print("[ZIP Database] Search from area. type or {0:back}\n")
            which_data = list(input("[ZIP Database] (EXAMPLE INPUT->) 東京都 港区 芝公園\n").split())
            if "0" in which_data:
                print("[ZIP Database] Back.\n")
                continue
            elif len(which_data) == 1:
                print("[ZIP Database] Wait for update!\n")
            elif len(which_data) == 2:
                print("[ZIP Database] Wait for update!\n")
            elif len(which_data) == 3:
                print("[ZIP Database] "+str(zipMethods.addr2zip(which_data[0], which_data[1], which_data[2]))+"\n")
            else:
                print("[ZIP Database] Query {} is not supported!\n".format(which_data))
                continue
        
        elif query_num == 3:
            ken_alldl.file_download_unzip()
            csv2sqlite3.make_sqlite3()

        else:
            print("[ZIP Database] Query {} is not supported!\n".format(query_num))

if __name__ == '__main__':
    main()