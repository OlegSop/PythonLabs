from threading import Lock, Thread
from contextlib import contextmanager


class RWLock(object):
    def __init__(self):
        self.wr_lock = Lock()
        self.re_num_lock = Lock()
        self.re_num = 0

    # Methods for reading
    # ----------------------------------------
    def read_acquire(self):
        self.re_num_lock.acquire()
        self.re_num += 1
        if self.re_num == 1:
            self.wr_lock.acquire()
        self.re_num_lock.release()

    def read_release(self):
        assert self.re_num > 0
        self.re_num_lock.acquire()
        self.re_num -= 1
        if self.re_num == 0:
            self.wr_lock.release()
        self.re_num_lock.release()

    @contextmanager
    def read_locked(self):
        try:
            self.read_acquire()
            yield
        finally:
            self.read_release()

    # ----------------------------------------

    # Methods for writing
    # ----------------------------------------
    def write_acquire(self):
        self.wr_lock.acquire()

    def write_release(self):
        self.wr_lock.release()

    @contextmanager
    def write_locked(self):
        try:
            self.write_acquire()
            yield
        finally:
            self.write_release()
    # ----------------------------------------


rwlock = RWLock()


def read_list(num, lst):
    lst_id = num
    with rwlock.read_locked():
        print(f'Reader {str(num)})', 'cars:', lst[lst_id])


def write_list(num, lst):
    with rwlock.write_locked():
        lst_id = num + 2
        print(f'Writer {str(num)})', 'cars:', lst[lst_id])


if __name__ == '__main__':
    cars = ['Tesla', 'Peugeot', 'Porsche', 'Renault', 'Mitsubishi', 'Nissan', 'Mercedes-Benz', 'Mazda', 'Lexus',
            'Honda', 'Fiat', 'Ford']
    for i in range(10):
        Thread(target=read_list, args=(i, cars,)).start()
    for i in range(10):
        Thread(target=write_list, args=(i, cars,)).start()
