import os
import hashlib
from contextlib import contextmanager


def hash_file(folder_path, block_size=65536):
    try:
        with open(folder_path, 'rb') as a_file:
            print(f"Open file: {a_file.name}")
            hashes = hashlib.md5()
            buf = a_file.read(block_size)
            while len(buf) > 0:
                hashes.update(buf)
                buf = a_file.read(block_size)
            return hashes.hexdigest()
    except OSError:
        print("Error!")
    finally:
        print("Closing file.")


def find_duplicates(folder):
    duplicates = {}
    for dir_name, subdir, file_list in os.walk(folder):
        print(f"Scan {dir_name}...")
        for file_name in file_list:
            folder_path = os.path.join(dir_name, file_name)
            file_hash = hash_file(folder_path)
            if file_hash in duplicates:
                duplicates[file_hash].append(folder_path)
            else:
                duplicates[file_hash] = [folder_path]
    return duplicates


def results(dictionary):
    res = list(filter(lambda x: len(x) > 1, dictionary.values()))
    if len(res) > 0:
        print("Duplicates found:")
        print("The following files identical.")
        print("____________________")
        for res in res:
            for sub_res in res:
                print(f'\t\t{sub_res}')
                print("____________________")
    else:
        print("No duplicate files.")


if __name__ == '__main__':
    path = input("Enter path to folder: ")
    duplicate = find_duplicates(path)
    results(duplicate)
