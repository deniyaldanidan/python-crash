import concurrent.futures as cfutures
import time
from helpers import do_something


def main():

    start = time.perf_counter()

    with cfutures.ProcessPoolExecutor() as executor:
        # f1 = executor.submit(do_something, 1)
        # f2 = executor.submit(do_something, 2)
        # print(f1.result())
        # print(f2.result())

        # processes = [executor.submit(do_something, x) for x in range(6)]

        # for proc in processes:
        # print(proc.result())

        # for proc in cfutures.as_completed(processes):
        # print(proc.result())

        samples = list(range(6))
        processes = executor.map(do_something, samples)

        for result in processes:
            print(result)

    end = time.perf_counter()

    print(f"Total time = {round(end-start, 2)} seconds")


if __name__ == "__main__":
    main()
