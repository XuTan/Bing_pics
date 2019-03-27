#### Python3 script.


# -*-encoding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import os

if __name__ == "__main__":
    try:
        xml_url = "https://cn.bing.com/HPImageArchive.aspx?idx=0&n=1"
        html = requests.get(xml_url)
        soup = BeautifulSoup(html.text, "lxml")
        image_url = soup.find("url").get_text()
        image_file = requests.get("https://cn.bing.com/" + image_url)
        with open(os.path.join(os.path.expanduser("~"), "Pictures","Saved Pictures","Bing_pics",
                               image_url.split("/")[-1].split(".")[1] + ".jpg"),
                  'wb') as image:
            image.write(image_file.content)
    except BaseException as e:
        print(e)
    else:
        print("Download", image_url.split("/")[-1], "done")
