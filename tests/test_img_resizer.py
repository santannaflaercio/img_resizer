import os
import unittest

from PIL import Image

from app import img_resizer


class TestImageResize(unittest.TestCase):

    def setUp(self):
        self.original_image_path = "img.png"
        self.resized_image_path = "resized_img.png"

    def test_image_resizer(self):
        # execute the img_resizer.py script
        img_resizer.main()

        # verify if the image was created
        self.assertTrue(os.path.exists(self.resized_image_path))

        # verify if the image was resized
        with Image.open(self.resized_image_path) as img:
            width, height = img.size
            self.assertEqual(width, 1920)
            self.assertTrue(height <= 1080)

    def tearDown(self):
        # remove the resized image after the test
        if os.path.exists(self.resized_image_path):
            os.remove(self.resized_image_path)


if __name__ == "__main__":
    unittest.main()
