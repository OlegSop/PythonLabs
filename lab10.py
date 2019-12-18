import urllib.request
from threading import Thread


class Downloader(Thread):
    def __init__(self, file_url, file_path):
        Thread.__init__(self)
        self.file_url = file_url
        self.file_path = file_path

    def run(self):
        try:
            urllib.request.urlretrieve(self.file_url, self.file_path)
        finally:
            print("File downloaded")


if __name__ == '__main__':
    _url = input("Enter URL: ")
    _path1 = input("Enter first path: ")
    _path2 = input("Enter second path: ")
    Downloader(_url, _path1).start()
    Downloader(_url, _path2).start()
