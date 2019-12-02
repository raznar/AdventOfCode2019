import urllib.request
import ssl

context = ssl._create_unverified_context()
page = urllib.request.urlopen('https://adventofcode.com/2019/day/1/input', context=context)


print(page.read())