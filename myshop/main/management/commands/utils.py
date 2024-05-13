from PIL import Image


def convert_image(unconverted_image: Image, fixed_image_size: int = 480) -> Image:
    """
    Resize immage with fixed size
    """
    width, height = unconverted_image.size
    new_image = Image.new('RGB', (fixed_image_size, fixed_image_size), (255, 255, 255))

    if width >= height:
        width_percent = (fixed_image_size / float(unconverted_image.size[0]))
        width_size = int((float(unconverted_image.size[0]) * float(width_percent)))
        height_size = int((float(unconverted_image.size[1]) * float(width_percent)))
        temp_image = unconverted_image.resize((width_size, height_size))
        new_image.paste(temp_image, (0, int(fixed_image_size / 2 - temp_image.size[1] / 2)))

    elif width < height:
        height_percent = (fixed_image_size / float(unconverted_image.size[1]))
        width_size = int((float(unconverted_image.size[0]) * float(height_percent)))
        height_size = int((float(unconverted_image.size[1]) * float(height_percent)))
        temp_image = unconverted_image.resize((width_size, height_size))
        new_image.paste(temp_image, (int(fixed_image_size / 2 - temp_image.size[0] / 2), 0))

    return new_image