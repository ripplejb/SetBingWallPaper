#! /usr/bin/python3

import urllib3
import json
from gi.repository import Gio

baseUrl = "https://www.bing.com"
imageDataUrl = "/HPImageArchive.aspx?format=js&idx=0&n=1&mkt=en-US"
fileLocation = "/home/ripal/Pictures/bing.jpg"

def getImageUrl(url):
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    data = json.loads(response.data.decode("utf-8"))
    return data["images"][0]["url"]

def downloadAndSaveImageData(url,filepath):
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    with open(filepath, "w+b") as file:
        file.write(response.data)


def setImageAsWallPaper(filepath):
    gsettings = Gio.Settings.new('org.gnome.desktop.background')
    gsettings.set_string("picture-uri", "file://"+filepath)

url = getImageUrl(baseUrl + imageDataUrl)
downloadAndSaveImageData(baseUrl+url, fileLocation)
setImageAsWallPaper(fileLocation)

