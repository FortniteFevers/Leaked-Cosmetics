import requests
from colorama import *
import shutil
import os
import time
import math
from PIL import Image, ImageFont, ImageDraw, ImageChops
from os import listdir
init()

#-----------------------#

apikey = 'b8f04d76-413b547e-15425588-111d0274'

filepath = 'C:/Users/User/Desktop/Leaked Cosmetics'
# PUT FILE PATH UP HERE ^


language = 'en'

#-----------------------#

headers = {'Authorization': apikey}


print(Fore.GREEN + '----FORTNITE LEAKED COSMETICS GENERATOR!----')

print(Fore.CYAN + '\nDo you want to:')
print('(1) Grab all leaked cosmetics')
print('(2) Merge all leaked cosmetics')
print('(3) Delete all leaked cosmetics')

print(Fore.YELLOW)
ask = input('>> ')


if ask == '1':
    print('\nStarting bot...\n')
    response = requests.get(f'https://fortniteapi.io/v2/items/upcoming?lang={language}', headers=headers)

    item = response.json()['items']

    for i in item:
        print(f'{i["name"]}:')

        url = i["images"]["full_background"]
        r = requests.get(url, allow_redirects=True)
        try:
            open(f'{filepath}/items/{i["id"]}.png', 'wb').write(r.content)
            print('Saved Image!\n')
        except:
            print(Fore.RED + 'Could not save image.')
            pass
    print(Fore.GREEN + '\nDone!')
    time.sleep(5)
    exit()

if ask == '2':
    print(Fore.GREEN + '\nMerging images...')
    images = [file for file in listdir(f'{filepath}/items')]
    count = int(round(math.sqrt(len(images)+0.5), 0))
    #print(len(images), count)
    x = len(images)
    print(f'\nFound {x} images in "items" folder.')
    finalImg = Image.new("RGBA", (1024*count, 1024*count))
    #draw = ImageDraw.Draw(finalImg)
    x = 0
    y = 0
    counter = 0
    for img in images:
        tImg = Image.open(f'{filepath}/items/{img}')
        if counter >= count:
            y += 1024
            x = 0
            counter = 0
        finalImg.paste(tImg, (x, y), tImg)
        x += 1024
        counter += 1
    finalImg.show()
    finalImg.save(f'{filepath}/{x}.png')
    print('\nSaved image!')

    time.sleep(5)
    exit()

if ask == '3':
    print('Deleting contents of the items folder...')
    try:
        shutil.rmtree(f'{filepath}/items')
        os.makedirs(f'{filepath}/items')
    except:
        os.makedirs(f'{filepath}/items')
    print(Fore.GREEN + '\nCleared contents!')
    time.sleep(5)
    exit()

if ask != '1' or '2' or '3':
    print(Fore.RED + 'Please enter a number 1-3.')
