from PIL import Image

try:
    image_to_resize = Image.open("img.jpg")
except FileNotFoundError:
    print("Image file not found.")
    exit(1)

# check the original dimensions of the image
original_width, original_height = image_to_resize.size

# calculate the new height preserving the aspect ratio
new_width = 1920
new_height = round((1920 * original_height) / original_width)

# if the calculated new height is greater than 1080, we need to fit the height into 1080p
# and then calculate the width to maintain the aspect ratio
if new_height > 1080:
    new_height = 1080
    new_width = round((1080 * original_width) / original_height)

# resize the image while maintaining the aspect ratio
resized_image_aspect = image_to_resize.resize((new_width, new_height), Image.Resampling.LANCZOS)

# now we create a new blank image with the target resolution
# in this case, we want a 1920x1080 image
new_img = Image.new("RGBA", (1920, 1080))

# calculate the position to paste the resized image on the blank image
x_offset = (1920 - new_width) // 2
y_offset = (1080 - new_height) // 2

# paste the resized image onto the blank image
new_img.paste(resized_image_aspect, (x_offset, y_offset))

# save the rezised image
resized_image_path_1920x1080 = 'resized_img.png'
new_img.save(resized_image_path_1920x1080, "PNG")