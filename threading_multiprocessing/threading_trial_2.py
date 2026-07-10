import concurrent.futures as cfutures
import time
from helpers import do_something

# * Start of Code
start = time.perf_counter()

# with cfutures.ThreadPoolExecutor() as executor:
#     f1 = executor.submit(do_something, 1)
#     f2 = executor.submit(do_something, 2)
#     print(f1.result())
#     print(f2.result())

# with cfutures.ThreadPoolExecutor() as executor:
#     threads = [executor.submit(do_something, x) for x in range(1, 6)]

#     for f in cfutures.as_completed(threads):
#         print(f.result())

with cfutures.ThreadPoolExecutor() as executor:
    values = [1, 2, 3, 4, 5]
    threads = executor.map(do_something, values)

    # for thread in threads:
    #   print(thread)

# * End of Code
end = time.perf_counter()

print(f"Finished in {round(end - start, 2)} seconds")
