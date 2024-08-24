import httpx
from selectolax.parser import HTMLParser

def scrape_images(url):
    try:
        # Make an HTTP request to the website
        response = httpx.get(url)
        response.raise_for_status()

        # Parse the HTML content
        parser = HTMLParser(response.text)

        # Find all image tags
        img_tags = parser.css("img.fx-image")

        # Extract image URLs
        image_urls = [tag.attributes["src"] for tag in img_tags if "src" in tag.attributes]

        return image_urls

    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    target_url = "https://www.thomann.co.uk/all-products-from-the-category-electric-guitars.html?ls=25&pg=4"
    image_urls = scrape_images(target_url)

    for i, url in enumerate(image_urls, start=1):
        print(f"Image {i}: {url}")
