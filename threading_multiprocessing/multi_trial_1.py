import multiprocessing
import time
from helpers import do_something


def main():

    start = time.perf_counter()

    # p1 = multiprocessing.Process(target=do_something, args=(1,))
    # p2 = multiprocessing.Process(target=do_something, args=(2,))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()
    processes = []

    for x in range(10):
        pr = multiprocessing.Process(target=do_something, args=(x,))
        pr.start()
        processes.append(pr)

    for i in processes:
        i.join()

    end = time.perf_counter()

    print(f"Total time = {round(end-start, 2)} seconds")


if __name__ == "__main__":
    main()
