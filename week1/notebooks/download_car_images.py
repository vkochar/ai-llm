from fastbook import *

def download_images_ddg(query, max_images=100):
    "Download images using DuckDuckGo search"
    dest = f'images/{query}'
    results = search_images_ddg(query, max_images=max_images)
    download_images(dest, urls=results)

# Specify the query and maximum number of images to download
query = 'car'
max_images = 75

# Download images
download_images_ddg(query, max_images)