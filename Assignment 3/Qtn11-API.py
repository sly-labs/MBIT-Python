import requests

# Define the API endpoint
url = "https://jsonplaceholder.typicode.com/posts/1"

try:
    # Send a GET request
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    response.raise_for_status()  # Raises an HTTPError for bad responses (4xx, 5xx)

    # Parse the JSON response
    data = response.json()

    # Print the result
    print("Title:", data['title'])
    print("Body:", data['body'])

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")