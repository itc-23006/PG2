import sys, requests, bs4, re, os

def download_images(keyword, max_images=10, save_dir='images'):
    os.makedirs(save_dir, exist_ok=True)

    res = requests.get('https://www.flickr.com/search/?text=' + keyword)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')                                      
    imgs = soup.select('.photo-list-photo-view img')

    for i in range(min(max_images, len(imgs))):
        img_url = imgs[i].get('src')
        if img_url.startswith('//'):
            img_url = 'https:' + img_url
        elif not img_url.startswith('http'):
            img_url = 'https://' + img_url
        print(img_url)

        img_res = requests.get(img_url)
        img_res.raise_for_status()
        img_file = open(os.path.join(save_dir, os.path.basename(img_url)), 'wb')
        for chunk in img_res.iter_content(100000):
            img_file.write(chunk)
        img_file.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('''使い方: python flickrloader.py キーワード ...
例）python flickrloader.py white cat
''')
    
    keyword = ' '.join(sys.argv[1:])
    download_images(keyword)