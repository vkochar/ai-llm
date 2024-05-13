import requests
from bs4 import BeautifulSoup
import os

def download_images(query, num_images):
    # Create a directory to save the images
    if not os.path.exists(query):
        os.makedirs(query)

    # Bing image search URL
    url = f"https://www.bing.com/images/search?q={query}&qft=+filterui:imagesize-large&FORM=IRFLTR"

    # Requesting the search page
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting image URLs
    image_urls = []
    for img in soup.find_all('img', class_='mimg'):
        if 'data-src' in img.attrs:
            image_urls.append(img['data-src'])

    # Download images
    for i, img_url in enumerate(image_urls[:num_images]):
        try:
            response = requests.get(img_url)
            if response.status_code == 200:
                with open(os.path.join(query, f"{query}_{i}.jpg"), 'wb') as f:
                    f.write(response.content)
        except Exception as e:
            print(f"Error downloading image {i + 1}: {str(e)}")

if __name__ == "__main__":
    query = "suv"
    num_images = 75
    download_images(query, num_images)
