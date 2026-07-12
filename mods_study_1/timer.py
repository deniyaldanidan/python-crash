from time import sleep


def timer():
    print("Time has started")
    for i in range(5):
        print(f"\r{i} sec  ", end="", flush=True)
        sleep(1)
    print("\rTimer has finished\n")


if __name__ == "__main__":
    timer()
