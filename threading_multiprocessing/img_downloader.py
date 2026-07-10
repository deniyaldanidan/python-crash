import requests


def img_downloader(img_url):
    print(f"downloading {img_url}")
    img_bytes = requests.get(img_url, timeout=3).content
    img_name = img_url.split("/")[3]
    img_name = f"{img_name}.jpg"
    img_path = f"outputs/{img_name}"
    print(img_path)
    # print(img_bytes)
    with open(img_path, "wb") as img_file:
        print(f"Start writing {img_path}")
        img_file.write(img_bytes)
        print(f"Image downloaded in {f"outputs/{img_name}"}")
