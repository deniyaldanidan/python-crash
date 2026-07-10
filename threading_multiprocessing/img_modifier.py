from PIL import Image, ImageFilter

SIZE = (1200, 1200)

OUTDIR = "modified_images/"


def img_modifier(img_name):
    print(img_name)
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(SIZE)

    img.save(f"{OUTDIR}{img_name.name}")
    return f"{img_name} is saved to {OUTDIR}{img_name.name}"
