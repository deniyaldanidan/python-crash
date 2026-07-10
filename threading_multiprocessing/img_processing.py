from pathlib import Path
import concurrent.futures as cfutures
from img_modifier import img_modifier
import time

IMGS_DIR = Path("images_to_process/").iterdir()

# for x in IMGS_DIR:
# print(x.name)


def main():
    with cfutures.ProcessPoolExecutor() as executor:
        processes = [executor.submit(img_modifier, x) for x in IMGS_DIR]

        for proc in cfutures.as_completed(processes):
            print(proc.result())


if __name__ == "__main__":
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    print(f"Total time = {round(end-start, 2)} seconds")
