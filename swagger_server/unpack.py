import os
import sys
import zipfile

import rarfile


def un_zip(src_dir_path):
    """unzip zip file"""
    zip_file = zipfile.ZipFile(src_dir_path)
    cur_dir = os.getcwd()
    target_path = os.path.join(cur_dir, 'developer')
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    zip_file.extractall(target_path)
    zip_file.close()
    print("unpack zip success")
    return src_dir_path

def un_rar(src_dir_path):
    """unzip rar file"""
    # print(src_dir_path)
    rar_file = rarfile.RarFile(src_dir_path)
    cur_dir = os.getcwd()
    target_path = os.path.join(cur_dir, 'developer')
    if not os.path.exists(target_path):
        os.makedirs(target_path)
    rar_file.extractall(target_path)
    rar_file.close()
    print("unpack rar success")
    return src_dir_path

def main():
    src_dir_path = sys.argv[1]
    unpack_type = src_dir_path.split('.')[1]
    if "zip" == unpack_type:
        un_zip(src_dir_path)
    elif "rar" == unpack_type:
        un_rar(src_dir_path)
    else:
        print("not supported type")


if __name__ == '__main__':
    main()