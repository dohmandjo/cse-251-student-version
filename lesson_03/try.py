
import threading
import multiprocessing as mp

global_var = 0

def func(name):
    global global_var
    global_var = 123456
    print(f'{name}: {global_var}')

if __name__ == '__main__':

    print(f'Before process global_var = {global_var}')
    p = mp.Process(target=func, args=('bob',))
    p.start()
    p.join()
    print(f'After process global_var = {global_var}')

    print()

    print(f'Before thread global_var = {global_var}')
    t = threading.Thread(target=func, args=('bob',))
    t.start()
    t.join()
    print(f'After thread global_var = {global_var}')