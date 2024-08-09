import requests
from requests_html import HTMLSession

url = 'https://blog.webdevsimplified.com/'

session = HTMLSession()
response = session.get(url)

# Use a more general XPath expression to find all <h2> elements
data = response.html.xpath('//h2')

# Create a list to store the text content of each <h2> element
h2_texts = [h2_element.text for h2_element in data]

# Write the data to a .txt file
with open('headers.txt', 'w') as file:
    for h2_text in h2_texts:
        file.write(h2_text + '\n')

print("Data saved to 'headers.txt' successfully!")
