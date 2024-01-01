from PIL import Image


def open_image(image_path):
    try:
        return Image.open(image_path)
    except FileNotFoundError:
        print(f"Image file {image_path} not found.")
        return None


def calculate_new_dimensions(original_width, original_height):
    new_width = 1920
    new_height = round((1920 * original_height) / original_width)

    if new_height > 1080:
        new_height = 1080
        new_width = round((1080 * original_width) / original_height)

    return new_width, new_height


def resize_image(image, new_width, new_height):
    # resize the image in two steps for better performance
    intermediate_image = image.resize((new_width * 2, new_height * 2), Image.BILINEAR)
    return intermediate_image.resize((new_width, new_height), Image.LANCZOS)


def create_new_image(resized_image, new_width, new_height):
    new_image = Image.new("RGBA", (1920, 1080))
    x_offset = (1920 - new_width) // 2
    y_offset = (1080 - new_height) // 2
    new_image.paste(resized_image, (x_offset, y_offset))
    return new_image


def main():
    image_path = "tests/img.png"
    image = open_image(image_path)

    if image is not None:
        original_width, original_height = image.size
        new_width, new_height = calculate_new_dimensions(original_width, original_height)
        resized_image = resize_image(image, new_width, new_height)
        new_image = create_new_image(resized_image, new_width, new_height)
        new_image.save('resized_img.png', "PNG")


if __name__ == "__main__":
    main()
