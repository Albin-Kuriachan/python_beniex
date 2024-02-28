"""Create a program that attempts to connect to a website and prints the HTML content if successful.
 Use a try-except-else block to handle the requests.exceptions.RequestException exception and display an
 error message if the connection fails."""

import requests

def website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print(f"Error connecting to {url}")
    else:
        print(f"Connected to {url} successfully!")
        print("HTML Content:")
        print(response.text)

url = input("Please enter a URL to connect: ")
website_content(url)
