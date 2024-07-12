import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    print(full_name)
    urllib.request.urlretrieve(url, full_name)

download_web_image("https://avatars2.githubusercontent.com/u/8547538?s=400&u=8a4be84ff4870a332fe94c11fca02b432fb9f83e&v=4")