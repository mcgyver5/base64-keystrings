import subprocess
import unittest
import os

class Base64Tests(unittest.TestCase):

    def test_isupper(self):
        self.assertTrue('FOOL'.isupper())

    def test_base64(self):
        self.assertTrue(5 > 4)
    def test_hello(self):
        proc = subprocess.Popen("python base64-keystrings.py -f plain.txt", stdout=subprocess.PIPE, shell=True)
        (out,err) = proc.communicate()
        lines = out.splitlines()
        self.assertEqual(lines[0],"U3RyaW5nIHBhc3N3b3JkID0gIkhPUlNFIFNUQVBMRSBCQVRURVJZIjsK")
if __name__ == '__main__':
    unittest.main()
