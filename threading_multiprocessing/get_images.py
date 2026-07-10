import concurrent.futures as cfutures
from img_downloader import img_downloader

imgs = [
    "https://images.unsplash.com/photo-1783321284120-61d9a47c92a1",
    "https://images.unsplash.com/photo-1783584731439-06cc9e1efbb2",
    "https://images.unsplash.com/photo-1783415367336-2fb0f2f476af",
    "https://images.unsplash.com/photo-1783497825305-38546053047c",
    "https://images.unsplash.com/photo-1783163685162-213197d55eab",
    "https://images.unsplash.com/photo-1782825955433-cce9fe38a62d",
    "https://images.unsplash.com/photo-1783002933130-a8505999aa5d",
    "https://plus.unsplash.com/premium_photo-1697778136905-c7b4eec8c603",
]


with cfutures.ThreadPoolExecutor() as executor:
    threads = executor.map(img_downloader, imgs)

# img_downloader(img_url=imgs[0])
