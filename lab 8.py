import os
import hashlib


def hash_file(path, block_size=65536):
    a_file = open(path, 'rb')
    hashes = hashlib.md5()
    buf = a_file.read(block_size)
    while len(buf) > 0:
        hashes.update(buf)
        buf = a_file.read(block_size)
    a_file.close()
    return hashes.hexdigest()


def find_duplicates(folder):
    duplicates = {}
    for dir_name, subdir, file_list in os.walk(folder):
        print(f"Scan {dir_name}...")
        for file in file_list:
            path = os.path.join(dir_name, file)
            file_hash = hash_file(path)
            if file_hash in duplicates:
                duplicates[file_hash].append(path)
            else:
                duplicates[file_hash] = [path]
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
