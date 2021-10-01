import time
from bs4 import BeautifulSoup
import requests
import random
import os
list_images_num=[]
# getting the number of images
for i in range(2,):
          r=random.randint(4,1000)
          #making sure same image would not be downloaded twice
          if r not in list_images_num: list_images_num.append(r)
def image_down():
    #looping through the images
    for image_number in list_images_num:
        url = 'http://xkcd.com/{}/'.format(image_number)
        url_get = requests.get(url)
        soup = BeautifulSoup(url_get.content, 'lxml')
        link = soup.find('div', id='comic').find('img').get('src')
        link = link.replace('//', 'https://')
        #show link
        print(link)
        #download every one hour
        img_name = os.path.basename(link)
        # Download image
        try:
            img = requests.get(link)
            with open(img_name, 'wb') as f:
                f.write(img.content)
        except:
            pass
        # run every one hour
        time.sleep(3600)
image_down()















