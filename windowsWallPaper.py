import urllib3
import json
import os

baseUrl = "https://www.bing.com"
imageDataUrl = "/HPImageArchive.aspx?format=js&idx=0&n=6&mkt=en-US"
fileLocation = os.path.expanduser('~') + "\\pictures\\wallpapers\\"

imageList = []
imageList.append("1.jpg") 
imageList.append("2.jpg") 
imageList.append("3.jpg") 
imageList.append("4.jpg") 
imageList.append("5.jpg") 
imageList.append("6.jpg") 

def getImageUrl(url):
    timeout=urllib3.Timeout(connect=2.0, read=7.0)
    http = urllib3.PoolManager(timeout=timeout)
    response = http.request("GET", url)
    return json.loads(response.data.decode("utf-8"))

def downloadAndSaveImageData(url,filepath):
    if not os.path.exists(fileLocation):
        os.makedirs(fileLocation)
    timeout=urllib3.Timeout(connect=2.0, read=15.0)
    http = urllib3.PoolManager(timeout=timeout)
    response = http.request("GET", url)
    with open(filepath, "w+b") as file:
        file.write(response.data)

data = getImageUrl(baseUrl + imageDataUrl)

i = 0
for image in data["images"]:
    if (i < len(imageList)):
        downloadAndSaveImageData(baseUrl+image["url"], fileLocation + imageList[i])
    i = i + 1

