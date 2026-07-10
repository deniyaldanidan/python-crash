import time


def do_something(n):
    print(f"do_something{n}: Sleeping for 2 seconds")
    time.sleep(2)
    print(f"do_something{n}: woken up")
    return f"do_something{n}: is DONE"
