#!/usr/bin/env python3

import re
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url)
html = page.read().decode("utf=8")
print(html)
pattern = "<h2.*?>.*?</h2.*?>"
match = re.search(pattern, html, re.IGNORECASE)
name = match.group()
name = re.sub("<.*?>", "", name)
print(name)
pattern2 = ""
color = re.findall("Favorite Color:", html)
print(color)