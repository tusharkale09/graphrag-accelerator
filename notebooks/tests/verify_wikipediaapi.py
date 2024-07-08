import wikipediaapi
import requests

# Define your user agent string
user_agent = 'CBIPPOCBOT/1.0 (https://cbippocjune2024.azure-api.net/; tushar.kale@scania.com)'

# Create a requests session and set the user agent
session = requests.Session()
session.headers.update({'User-Agent': user_agent})

# Create Wikipedia API object with the custom session
wiki_wiki = wikipediaapi.Wikipedia('en', requests=session)

# Fetch a Wikipedia page
page_py = wiki_wiki.page('Python (programming language)')

# Print the page title and a short summary
print("Page Title: %s" % page_py.title)
print("Page Summary: %s" % page_py.summary[:60])

