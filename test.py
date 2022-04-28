import imp
import math
import sys
from os import rename

import requests

print(sys.version)
print(sys.executable)
r = requests.get("https://baidu.com")
print(r.status_code)


def greet(greet_words, name):
    test = "Test"
    print(greet_words, name)
