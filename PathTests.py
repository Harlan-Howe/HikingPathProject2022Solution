import unittest
import cv2
import numpy as np
from PathMakerFile import PathMaker, MAP_FILENAME

class MyTestCase(unittest.TestCase):
    def test_display_path(self):

        pm = PathMaker(filename="40x40Gray.jpg")
        pm.show_map()
        cv2.waitKey(0)
        cv2.destroyAllWindows()


        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
