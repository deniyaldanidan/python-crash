import threading
import time
from helpers import do_something

# * Start of Code
start = time.perf_counter()


# t1 = threading.Thread(target=do_something, args=(1,))
# t2 = threading.Thread(target=do_something, args=(2,))

# t1.start()
# t2.start()
# t1.join()
# t2.join()

threads = []

for x in range(1, 6):
    thread = threading.Thread(target=do_something, args=(x,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()

# * End of Code
finish = time.perf_counter()

print(f"Finished in {round(finish - start, 2)} seconds")
