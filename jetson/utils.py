import numpy as np
from collections import defaultdict

from PIL import Image


def read_png_or_tiff(image_path):
    return np.array(Image.open(image_path).convert("RGB")).astype(np.uint8)


def read_bgr888_or_rgb888(image_path, image_height, image_width):
    with open(image_path, "rb") as infile:
        data = infile.read()
        arr = np.frombuffer(data, dtype=np.uint8)
        return arr.reshape(image_height, image_width, 3)


def _parse_class(s):
    """
    Parse a key, value pair, separated by '='

    On the command line (argparse) a declaration will typically look like:
        foo=hello
    or
        foo="hello world"
    """
    items = s.split('=')
    key = items[0].strip()  # we remove blanks around keys, as is logical
    if len(items) > 1:
        # rejoin the rest:
        value = '='.join(items[1:])
    return (key, value)


def parse_classes(items, default_dict_generator=None):
    """
    Parse a series of key-value pairs and return a dictionary
    """
    d = defaultdict(default_dict_generator)

    if items:
        for item in items:
            key, value = _parse_class(item)
            d[key] = value
    return d
