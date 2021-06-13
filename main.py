import csv2sqlite3
import ken_alldl
import zipMethods

def main():
    while True:
        query_num = int(input("[ZIP Database] What do you want? type {0:quit, 1:pick up all, 2:select area, 3: download csv and create table}\n"))
        if query_num == 0:
            print("[ZIP Database] End. Bye-bye!\n")
            break
        """
        elif query_num == 1:
            print("[ZIP Database] Pick up all.\n")
            which_data = int(input("[ZIP Database] type {0:back, 1:weathers, 2:winds, 3:waves}\n"))
            if which_data == 0:
                print("[ZIP Database] Back.\n")
                continue
            elif which_data == 1:
                we.weathers_all(data)
            elif which_data == 2:
                we.winds_all(data)
            elif which_data == 3:
                we.waves_all(data)
            else:
                print("[ZIP Database] Query {} is not supported!\n".format(which_data))
                continue
        """
        """
        elif query_num == 2:
            area = input("[ZIP Database] Select Area.\n")
            which_data = int(input("[ZIP Database] type {0:back, 1:weathers, 2:winds, 3:waves}\n"))
            if which_data == 0:
                print("[ZIP Database] Back.\n")
                continue
            elif which_data == 1:
                we.weather_sel(data, area)
            elif which_data == 2:
                we.wind_sel(data, area)
            elif which_data == 3:
                we.wave_sel(data, area)
            else:
                print("[ZIP Database] Query {} is not supported!\n".format(which_data))
                continue
        """
        elif query_num == 3:
            ken_alldl.file_download_unzip()
            csv2sqlite3.make_sqlite3()

        else:
            print("[ZIP Database] Query {} is not supported!\n".format(query_num))

if __name__ == '__main__':
    main()