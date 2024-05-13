from duckduckgo_search import DDGS
import requests

# Initialize the DDGS class
ddgs = DDGS()

# Search for images (replace 'kittens' with your desired query)
image_results = ddgs.images(keywords='white cars', max_results=15)

# Process the image results (e.g., download the images)
i = 0
for result in image_results:
    i+=1
    image_url = result['image']
    # Your code to download the image goes here
    print(f"Downloaded image: {image_url}")
    response = requests.get(image_url)
    image_data = response.content

    # Save the image to a file (e.g., img.jpg)
    with open("new/white-{}.jpg".format(i), "wb") as f:
        f.write(image_data)

