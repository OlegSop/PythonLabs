import os
import hashlib
import math
import threading


def find_duplicates(directory, thread_num):
    duplicates = {}
    files_list = []
    threads = []
    dir_files(directory, files_list)
    slide = math.ceil(len(files_list) / thread_num)
    start = -slide
    while True:
        start += slide
        end = start + slide
        if end > len(files_list):
            end = len(files_list)
        thread = threading.Thread(target=get_duplicates, args=[duplicates, files_list, start, end, 65536])
        thread.start()
        threads.append(thread)
        if end == len(files_list):
            break
    for thread in threads:
        thread.join()
    res = []
    for k in duplicates:
        if len(duplicates[k]) > 1:
            res.append(duplicates[k])
    return res


def dir_files(directory, f_list):
    for _dir in os.walk(directory):
        for i in _dir[2]:
            f_list.append(_dir[0] + "/" + i)


def get_duplicates(duplicate_files, f_list, start, end, block_size):
    for i in range(start, end):
        _hash = hashlib.sha256()
        with open(f_list[i], "rb") as f:
            buffer = f.read(block_size)
            while len(buffer) > 0:
                _hash.update(buffer)
                buffer = f.read(block_size)
            data = _hash.hexdigest()
        if data in duplicate_files:
            duplicate_files[data].append(f_list[i])
        else:
            duplicate_files[data] = [f_list[i]]


if __name__ == '__main__':
    _path = input("Enter path:")
    _threads = input("Enter thread number:")
    print(*find_duplicates(_path, float(_threads)))
